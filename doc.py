from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import joblib
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import re

# Initialize FastAPI 
app = FastAPI(title="Doc-AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model, tokenizer, and label encoder 
print("Loading model and preprocessors...")
model = tf.keras.models.load_model("medical_nn_model_v2.h5")
tokenizer = joblib.load("tokenizer.pkl")
label_encoder = joblib.load("label_encoder.pkl")
print("Model, tokenizer, and label encoder loaded successfully!")

# Greeting and fallback patterns 
GREETINGS = ["hi", "hello", "hey", "good morning", "good afternoon", "good evening", "what’s up", "heyy", "yo", "yoh", "how are you","Wassup","Wagwan"]
THANKS = ["thank you", "thanks", "appreciate", "grateful","Okay","Ok"]
BYE = ["bye", "goodbye", "see you", "talk later","later"]
EMERGENCY = ["over bleeding","bleeding","coughing blood","difficulty in breathing","asthma attack","broken"]

# Example follow-up questions based on symptoms
FOLLOW_UP_QUESTIONS = {
    "fever": ["Do you have a high temperature?", "Any chills or sweating?"],
    "headache": ["Is it a mild or severe headache?", "Do you have sensitivity to light?"],
    "cough": ["Is it dry or productive?", "Any shortness of breath?"],
    "rash": ["Is it itchy?", "Any swelling associated?"],
    "stomach": ["Is there nausea or vomiting?", "Any abdominal pain?"]
}

# Clean and preprocess text 
def clean_text(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text

def preprocess_text(text: str):
    seq = tokenizer.texts_to_sequences([text])
    if not seq or len(seq[0]) == 0:
        return None
    return pad_sequences(seq, maxlen=100)  

# Helper to generate follow-up questions
def generate_follow_up(user_input):
    follow_up = []
    for symptom, questions in FOLLOW_UP_QUESTIONS.items():
        if symptom in user_input:
            follow_up.extend(questions)
    # Default questions if no keyword matched
    if not follow_up:
        follow_up = [
            "Do you have a fever?", 
            "Any pain or discomfort?", 
            "Do you notice any rashes or skin changes?"
        ]
    return follow_up
# Main prediction route 
@app.post("/predict")
async def predict(request: Request):
    data = await request.json()
    user_input = clean_text(data.get("text", "").strip())

    if not user_input:
        return {
            "bot_message": "Please describe how you're feeling so I can help.",
            "status": "error"
        }

    # Emergency
    if any(e in user_input for e in EMERGENCY):
        return {
            "bot_message": "EMERGENCY: PLEASE SEEK HELP IMMEDIATELY.",
            "status": "emergency"
        }

    # Greetings
    if any(g in user_input for g in GREETINGS):
        return {
            "bot_message": (
                "👋 Hey there! I’m **Doc-AI**, your health companion.\n"
                "Feeling a bit off today? Tell me about your symptoms and I'll try to help."
            ),
            "status": "greeting"
        }

    # Thanks
    if any(t in user_input for t in THANKS):
        return {
            "bot_message": (
                "😊 You’re most welcome! I’m here to help. "
                "If you have more symptoms, just tell me."
            ),
            "status": "gratitude"
        }

    # Goodbye
    if any(b in user_input for b in BYE):
        return {
            "bot_message": (
                "👋 Take care of yourself! Remember, if symptoms persist, "
                "please visit a healthcare professional."
            ),
            "status": "goodbye"
        }

    # Predict
    X_input = preprocess_text(user_input)
    if X_input is None:
        follow_up = generate_follow_up(user_input)
        return {
            "bot_message": (
                "🤔 I couldn’t detect your condition; it might be out of my scope of expertise.\n"
                "Can you answer a few questions so I can try to help?"
            ),
            "status": "uncertain",
            "follow_up": follow_up
        }

    probs = model.predict(X_input, verbose=0)[0]
    top_indices = np.argsort(probs)[::-1][:2]
    main_idx, alt_idx = top_indices[0], top_indices[1]

    main_disease = label_encoder.inverse_transform([main_idx])[0]
    alt_disease = label_encoder.inverse_transform([alt_idx])[0]
    confidence = float(probs[main_idx])

    if confidence < 0.45:
        follow_up = generate_follow_up(user_input)
        return {
            "bot_message": (
                "I’m not entirely sure what condition this might be. "
                "It could be something mild, but answering a few questions may help."
            ),
            "status": "uncertain",
            "confidence": confidence,
            "follow_up": follow_up
        }

    bot_message = (
        f"Based on your symptoms, you’re **most likely** experiencing:\n\n"
        f"**{main_disease.replace('_', ' ')}** ({confidence:.1%} confidence)\n\n"
        f"It could also be **{alt_disease.replace('_', ' ')}**.\n\n"
        f"**Next step**: See a doctor soon for confirmation."
    )

    return {
        "bot_message": bot_message,
        "main_prediction": main_disease,
        "alt_prediction": alt_disease,
        "confidence": confidence,
        "status": "ok"
    }

# Health check
@app.get("/")
def home():
    return {"message": "Doc-AI backend is LIVE! Ready for symptoms."}
