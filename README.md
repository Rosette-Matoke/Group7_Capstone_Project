# DOC AI : An AI-Powered Conversational Assistant for Disease Prediction and Patient Guidance”
<p align="center">
  <img src="AI.jpg" alt="AI IMAGE" width="1000" height="700"/>
</p>

## 👥 GROUP MEMBERS
💻 VICKER IVY

📊 VICTOR ONGAKI

🧠 ROSE MATOKE

🤖 FELIX MUSAU

🧩 DAISY KERUBO THOMAS

# 🚀 PROJECT SUMMARY
This project developed an intelligent medical chatbot system designed to improve patient guidance and streamline the disease diagnosis process. Using a comprehensive Disease and Symptoms Dataset, the chatbot leverages natural language processing (NLP) and machine learning to classify diseases based on user-reported symptoms.

Several models including Logistic Regression, Random Forest, XGBoost, Naive Bayes, and Neural Network classifiers were trained and evaluated using key metrics such as Accuracy, Precision, Recall, F1-score, and Log Loss. After comparison, the Word2Vec Neural Network model was selected for deployment due to its strong balance between performance, scalability, and ability to process natural language symptom descriptions effectively.

The deployed chatbot enables users to describe symptoms in free text, predicts likely disease categories, and suggests the appropriate medical specialist for consultation.Overall, this project demonstrates how the integration of AI, NLP, and deep learning can enhance healthcare accessibility, improve pre_diagnosis efficiency, and support informed medical decision-making.

This link leads to the [Tableau Presentation](https://public.tableau.com/views/Capstone_Tableau_17623360435140/DiseaseandSymptomsDatasetDashboard?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
This is the link to our[Non-technical presentation](https://github.com/Rosette-Matoke/Group7_Capstone_Project/blob/DAISY2/Presentation.pdf)

# 👔  1. BUSINESS UNDERSTANDING
According to [Rabin Matin](https://rabinmartin.com/insights/how-do-we-shape-a-more-inclusive-future-in-digital-health/?gad_source=1&gad_campaignid=20222258766&gbraid=0AAAAApYg6NJEwMSRw_2i3aRx_Yxow4-0V&gclid=EAIaIQobChMImJjdy6nakAMVeZJQBh1NAgf-EAAYAiAAEgJ3XPD_BwE) article written in November 2024. We can say that in the healthcare sector, patient–doctor communication plays a crucial role in ensuring timely diagnosis, effective treatment, and overall patient satisfaction. However, doctors often face high workloads and limited consultation time, while patients struggle to access reliable medical advice promptly. This imbalance between healthcare demand and availability creates a significant gap in early diagnosis and patient support.

To bridge this gap, the development of a medical chatbot offers a practical and innovative solution. The chatbot functions as a virtual health assistant, capable of providing patients with instant, preliminary health guidance, symptom analysis, and responses to common medical questions. By doing so, it enhances accessibility to healthcare information and supports both patients and professionals in improving communication, efficiency, and care outcomes.

The introduction of a medical chatbot comes with several advantages. It provides 24/7 accessibility, ensuring that patients can receive guidance at any time, even outside normal clinic hours. It also helps reduce the workload for healthcare professionals by handling repetitive and low-complexity interactions, allowing doctors to focus on more critical cases. Additionally, the chatbot contributes to faster preliminary diagnoses by collecting patient symptoms ahead of consultation, and it improves cost efficiency by reducing the need for constant human involvement in basic queries. Moreover, it can collect valuable data on patient interactions for use in research and healthcare system improvements. Importantly, chatbots deliver consistent and standardized information, ensuring accuracy and eliminating human variability in responses.

Despite these benefits, several limitations must be acknowledged. Chatbots possess limited diagnostic accuracy, as they cannot fully understand a patient’s medical history or complex symptom combinations. They also lack emotional intelligence, meaning they cannot replicate the empathy and reassurance that human healthcare providers offer. Data privacy and security risks pose additional challenges since medical data is highly sensitive and must be protected from unauthorized access. Furthermore, internet dependence can limit accessibility in low-connectivity areas, and regulatory concerns arise from the need to ensure compliance with medical and ethical standards. Lastly, the chatbot may struggle with language nuances or contextual understanding, particularly in diverse linguistic environments.

To mitigate these challenges, a range of strategies will be implemented. The chatbot will combine rule-based and machine learning techniques to balance accuracy with control, and it will clearly communicate that its responses are for informational purposes only. Predefined empathetic response patterns will be incorporated to enhance user experience, while data encryption and anonymization protocols will safeguard user privacy. To improve accessibility, an offline or SMS-based version may be developed for users in low-bandwidth regions. Compliance with medical and data protection regulations such as HIPAA and GDPR will be ensured through close collaboration with medical experts. Finally, the chatbot will be trained on diverse and localized text datasets to improve language comprehension and contextual relevance.

Through these measures, the medical chatbot will provide an accessible, cost-effective, and secure digital healthcare assistant that enhances patient engagement while maintaining ethical, safe, and reliable healthcare delivery.

# ✍️ 2. BUSINESS PROBLEM
Despite advancements in healthcare technology, many patients still face barriers to timely and accurate medical assistance. Overcrowded hospitals, limited access to medical professionals, and the high cost of consultations often delay the delivery of essential care. At the same time, doctors are overwhelmed with repetitive, non-critical inquiries that consume valuable time which could be devoted to more complex cases.

Additionally, patients frequently turn to unreliable online sources for self-diagnosis, leading to misinformation, anxiety, and in some cases, delayed professional treatment. This information gap has created an urgent need for an automated, intelligent, and reliable communication channel that can provide immediate preliminary support while guiding patients toward appropriate medical action.

A well-designed conversational medical chatbot aims to address these issues by providing round-the-clock health assistance, reducing the administrative burden on doctors, and improving early health intervention ultimately contributing to better patient outcomes, increased operational efficiency, and enhanced satisfaction across the healthcare ecosystem.

# 📋 3. OBJECTIVES
## 🎯3.1 Main objective
To develop and implement a  conversational medical chatbot system within a hospital setting that enhances healthcare guidance for patients and efficiently routes cases to the appropriate healthcare professionals by categorizing patient diseases based on their symptoms.

## 🧩3.2 Specific objective
1. To provide 24/7 automated medical support to help patients get quick answers to patient diseases based on symptoms even outside normal working hours.
2. To reduce the workload of nurses, doctors’ and receptionists by handling routine tasks and FAQs.
3. To enhance patient experience and engagement by delivering empathetic, accurate, and easy-to-understand responses that improve patient trust and satisfaction within the hospital ecosystem.
4. To efficiently collect patient information and symptoms through a user-friendly interface, potentially reducing wait times and improving patient experience.

## 🔎 3.3 Research Questions
1. How effectively can a medical chatbot provide accurate and timely 24/7 responses to common patient diseases based on symptoms compared to traditional hospital information access methods?
2. To what extent does the medical chatbot reduce the workload of healthcare staff (nurses, doctors, and receptionists) by automating routine inquiries and frequently asked questions?
3. How does the use of an empathetic and user-friendly medical chatbot impact patient engagement, satisfaction, and trust in hospital services?
4. How efficiently can the medical chatbot collect patient symptoms and information through its interface, and how does this impact wait times and the overall patient intake process?

5. ## 👍3.4 Metric of success
Develop a model that has a > 85% accuracy score, recall ,f1_score and precision score to enable disease prediction.
A conversational chatbot which can accurately classify patient diseases based on symptoms.
# 📊 4. DATA UNDERSTANDING
Our data was downloaded from [Mendeley Data](https://data.mendeley.com/datasets/2cxccsxydc/1) published on 3 March 2025. The dataset contains disease names along with the symptoms faced by the respective patient. There are a total of 773 unique diseases and 377 symptoms, with approximately 246,000 rows. The dataset was artificially generated, preserving Symptom Severity and Disease Occurrence Possibility.
Several distinct groups of symptoms might all be indicators of the same disease. There may even be one single symptom contributing to a disease in a row or sample. This is an indicator of a very high correlation between the symptom and that particular disease.
A larger number of rows for a particular disease corresponds to its higher probability of occurrence in the real world. Similarly, in a row, if the feature vector has the occurrence of a single symptom, it implies that this symptom has more correlation to classify the disease than any one symptom of a feature vector with multiple symptoms in another sample.

citation:
Stark, Bran (2025), “Disease and symptoms dataset 2023”, Mendeley Data, V1, doi: 10.17632/2cxccsxydc.1

##  🚧 4.1 Data Limitation
1. Computationaly expensive- It's large size makes it hard for our CPU's to work with locally this takes a lot of time and resources.

2. Data imbalance — some diseases have far more samples than others.

3. Some symptom descriptions are ambiguous or overlap across diseases.

4. The dataset may not cover all diseases or symptom variations.

#🧭 5. DATA EXPLORATION¶

5.1 Loading a dataset

5.2 Data cleaning

5.3 feature engineering

# 🧠 6. EXPLORATORY DATA ANALYSIS (EDA)
## 6.1 Distribution of diseases
   6.1.2 Top 10 diseases
   6.1.3 Bottom 10 diseases
## 6.2 Wordcloud for disease distribution
<img width="950" height="589" alt="download" src="https://github.com/user-attachments/assets/222e46dc-5e93-4d55-b60d-998694e03c53" />


## 6.3 Symptom Co-occurrence Network
## 6.4 Top Symptoms per Diseas
e
## 6.5 Disease classification

### **Below is a table of Diseases group into various categories**

|  **#** | **Category**                               | **Examples / Diseases**                                                                                                                                                                                                                                                                                                                | **Description**                                    |
| :----: | :----------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------- |
|  **1** | **Infectious Diseases**                    | tuberculosis, dengue fever, cryptococcosis, cysticercosis, mononucleosis, infectious gastroenteritis, herpangina, hepatitis, pneumonia, abscess of lung, empyema, otitis media, conjunctivitis, chorioretinitis, cornea infection, cellulitis, mastoiditis, cholangitis, cholesteatoma, peritonitis, cholesteatoma, infection of wound | Caused by bacteria, viruses, fungi, or parasites   |
|  **2** | **Respiratory Diseases**                   | asthma, COPD, emphysema, chronic sinusitis, acute sinusitis, bronchitis, pulmonary embolism, pulmonary congestion, atelectasis, thoracic injury, pulmonary eosinophilia                                                                                                                                                                | Affect lungs and breathing                         |
|  **3** | **Cardiovascular Diseases**                | hypertension, ischemic heart disease, heart block, atrial fibrillation, pericarditis, coronary atherosclerosis, thoracic aortic aneurysm, HOCM, vasculitis, deep vein thrombosis (DVT), thrombophlebitis, varicose veins, hemorrhage, anemia, von Willebrand disease, coagulation disorder                                             | Disorders of the heart and blood vessels           |
|  **4** | **Endocrine & Metabolic Disorders**        | diabetes, hypothyroidism, Hashimoto thyroiditis, obesity, hyperkalemia, hypokalemia, magnesium deficiency, vitamin B12 deficiency, metabolic disorder, Cushing’s syndrome, Addison’s disease, pituitary adenoma                                                                                                                        | Hormonal and metabolic imbalances                  |
|  **5** | **Neurological Disorders**                 | epilepsy, stroke, Parkinson’s, multiple sclerosis, myasthenia, neuralgia, migraine, dizziness, myoclonus, restless leg syndrome, normal pressure hydrocephalus, cerebral palsy, tic disorder, concussion                                                                                                                               | Brain, nerve, and coordination disorders           |
|  **6** | **Psychiatric / Mental Health Disorders**  | depression, anxiety, panic disorder, bipolar disorder, ADHD, psychotic disorder, substance-related mental disorder, insomnia, primary insomnia, conversion disorder, postpartum depression, chronic pain disorder, eating disorder, stuttering, nervousness                                                                            | Mental, mood, or behavioral health                 |
|  **7** | **Musculoskeletal Disorders**              | spondylosis, spondylitis, osteochondrosis, bursitis, gout, arthritis, back pain, osteoporosis, bone spur, flat feet, Tietze syndrome                                                                                                                                                                                                   | Disorders of bones, joints, or muscles             |
|  **8** | **Gastrointestinal Diseases**              | GERD, gastritis, ulcerative colitis, intestinal malabsorption, pancreatitis, choledocholithiasis, liver disease, cirrhosis, cholangitis, cholesteatoma, peritonitis, diarrhea, indigestion, colonic polyp, volvulus, pyloric stenosis, empyema of gallbladder                                                                          | Affect the stomach, intestines, liver, or pancreas |
|  **9** | **Reproductive & Genitourinary Disorders** | endometriosis, vaginitis, atrophic vaginitis, vulvodynia, pelvic organ prolapse, infertility, ovarian torsion, uterine fibroids, cryptorchidism, urethral valves, cystitis, pyelonephritis, bladder disorder, priapism, pregnancy complications                                                                                        | Disorders of reproductive or urinary organs        |
| **10** | **Cancers / Neoplasms**                    | liver cancer, breast cancer, leukemia, lymphoma, pituitary adenoma, melanoma, esophageal cancer, brain cancer                                                                                                                                                                                                                          | Malignant and benign tumors                        |
| **11** | **Dermatological Disorders**               | eczema, psoriasis, seborrheic dermatitis, seborrheic keratosis, actinic keratosis, alopecia, dermatitis, skin abscess, viral warts, fungal infection, hyperhidrosis                                                                                                                                                                    | Affect skin, hair, or nails                        |
| **12** | **Hematologic Disorders**                  | anemia, von Willebrand disease, coagulation disorders, hemarthrosis, polycythemia, bleeding disorder                                                                                                                                                                                                                                   | Blood or bone marrow diseases                      |
| **13** | **Congenital & Genetic Disorders**         | Down syndrome, Turner syndrome, tuberous sclerosis, spina bifida, cysticercosis, fetal alcohol syndrome, cryptorchidism                                                                                                                                                                                                                | Present from birth or inherited                    |
| **14** | **Autoimmune Disorders**                   | lupus (SLE), rheumatoid arthritis, Hashimoto’s thyroiditis, vasculitis, psoriasis                                                                                                                                                                                                                                                      | Immune system attacks body tissues                 |
| **15** | **Chronic Pain & Functional Disorders**    | fibromyalgia, chronic back pain, irritable bowel syndrome (IBS), chronic fatigue, teething syndrome, pain disorder                                                                                                                                                                                                                     | Long-term pain and functional syndromes            |
| **16** | **Injuries & Trauma**                      | fractures (arm, rib, hand), dislocations, crushing injuries, open wounds (neck, back, mouth), contusions, concussion, thoracic injury                                                                                                                                                                                                  | Physical injuries to tissues or bones              |
| **17** | **Pregnancy & Perinatal Conditions**       | preeclampsia, gestational diabetes, ectopic pregnancy, postpartum depression, problem during pregnancy, induced abortion                                                                                                                                                                                                               | Conditions affecting pregnancy or childbirth       |
| **18** | **Eye Disorders**                          | glaucoma, cataract, corneal disorders, conjunctivitis, chorioretinitis, endophthalmitis, cornea infection                                                                                                                                                                                                                              | Eye and vision-related diseases                    |
| **19** | **Ear, Nose, Throat (ENT)**                | otitis media, sinusitis, laryngitis, mastoiditis, otosclerosis, presbyacusis, tinnitus, nose deformity, sore in nose                                                                                                                                                                                                                   | ENT infections or disorders                        |
| **20** | **Other / Miscellaneous**                  | poisoning (antidepressants, analgesics, ethylene glycol), allergic reaction, vitamin deficiencies, drug intoxication, withdrawal syndrome, hyperhidrosis  | Conditions not fitting other categories            |

6.6 Disease Count per category

6.7 Top 5 Diseases category
<img width="1013" height="659" alt="download" src="https://github.com/user-attachments/assets/b1d0b1da-a20a-44ac-8310-5f59e484bf53" />

# 🤖 7. MODELLING

 ### 7.1 Logistic Regression Model(Baseline)
  7.1.2 Logistic regression Evaluation
   
 ### 7.2 RandomForestClassifier
  7.2.1 Random Forest Evaluation
  ### 7.3 XGBoost Classifier
  7.3.1 XGBOOST Evaluation
### 7.4 Naive Bayes
 7.4.1 NAIVE BAYES EVvaluation
# 7.5 DEEP LEARNING
   #### 7.5.1 NEURAL NETWORK CLASSIFIER
   7.5.2 Neural network Evaluation
# 7.6 NEURAL NETWORK (word vectorizer)
   7.6.1 word vectorizer Neural network  evaluation

# 📈 8.MODEL VALIDATION.

### 8.1 HOW DO WE DEFINE SUCCESS? (METRICS)
our model is a multi-class medical diagnosis classifier, predicting a disease based on symptoms.
In this kind of task, accuracy alone is not enough, because some classes (diseases) might have more samples than others and false negatives can be more dangerous than false positives.

**Healthcare & diagnosis require reliability over raw accuracy**

A model that’s 90% accurate but miss diagnoses 10% of real patients (low recall) is dangerous.
Hence, *recall (catching all true cases)* is a priority.

**Precision** ensures responsible predictions
You don’t want to label many healthy people as “infected” or “critical”.High precision ensures your model only flags a condition when it’s confident.

**F1-score** gives a fair balance
Especially if diseases are not equally represented, F1 helps ensure performance is consistent across all classes.

**Log Loss** validates trust
In a diagnostic setting, the confidence (probability) of prediction matters (for example, “90% malaria” vs “55% malaria”).
Low log loss means the model’s probability predictions are trustworthy and suitable for decision support.


**NB:** In our medical diagnosis model, the most important metrics are Recall, F1-score, Precision, and Log Loss.
Recall ensures that no true disease cases are missed, Precision ensures responsible predictions, F1-score maintains balance between both, and Log Loss validates the model’s confidence.
These metrics will drive our decision making when choosing a model to deploy.

<img width="1389" height="889" alt="download" src="https://github.com/user-attachments/assets/1567d0ae-5180-4382-afd5-acc524610fec" />


**Balanced and Consistent Performance**

The neural network achieves Accuracy = 0.8772, Precision = 0.8883, Recall = 0.8758, and F1 = 0.8740, all within a tight range.

This shows it is well-balanced — not biased toward precision or recall.

In comparison, models like Random Forest or XGBoost often show slightly higher training accuracy but drop more on test data (signs of mild overfitting).

The neural network generalizes well to unseen data, which is crucial for real-world deployment.
While overall Accuracy remains high(0.8772),it is the combination of high Recall and low Log Loss that makes this neural network the most dependable and deployment ready model for real-world use.


# 9.CONCLUSION
1. In this project, we developed a machine learning model capable of predicting potential diseases based on symptoms provided by a user. Using a dataset containing over 250,000 symptom–disease records spanning more than 400 disease categories, we trained and optimized a neural network model (best_nn_model).

2. Word2Vec NN performed competitively, achieving an accuracy of 0.8772, with strong precision and recall balance.It effectively captured semantic relationships in textual symptom data, outperforming traditional models on language understanding tasks.
3. Symptoms like `headache`,`vomiting` and `abdominal_pain` are the most influencial features across all the models.
4. Cystitis is the most leading disease by (1219 cases), followed very closely by nose disorder (1218) and vulvodynia (1218). Reproductive (vulvodynia, vaginal cyst) and neurological/musculoskeletal (spondylosis, pain syndrome) conditions are both represented this might suggest diversity in our dataset.
5. Highly Connected Symptoms (Hubs):Symptoms like fever, cough, and headache are in the center of many diseases they co-occur with many other symptoms.
6. Infectious diseases lead with the highest prevalence (25.9%),Gastrointestinal and cardiovascular diseases follow closely, reflecting the combined influence of lifestyle factors, nutrition, and aging populations on human health.

7. # 10.RECOMMENDATIONS
8. 1. Integrate with Trusted Medical Databases:
Connect the chatbot to verified and reputable medical databases such as the World Health Organization (WHO) and MedlinePlus. This will ensure that the system stays up to date with the latest medical research, treatment guidelines, and disease information, improving the accuracy and reliability of diagnoses.

2. Develop a Mobile or Web-Based Application:
Create a mobile or web version of the chatbot to enhance accessibility and user convenience. A user-friendly interface will allow patients and healthcare workers to interact with the system anytime and anywhere, promoting wider adoption and usability.

3. Incorporate Reinforcement Learning:
Implement reinforcement learning techniques to enable the model to learn from user interactions and feedback over time. This will allow the chatbot to continuously refine its predictions and improve decision-making accuracy as it gathers more data from real-world use.

4. Design Adaptive Conversational Flows:
Introduce a dynamic conversational structure that allows the chatbot to ask targeted follow-up questions when prediction confidence is low. This interactive approach enhances the model’s diagnostic precision and builds user trust through personalized, context-aware responses.

5. It is recommended that healthcare systems adopt integrated, preventive, and data-driven approaches that target both infectious and non-communicable diseases, with increased investment in public health awareness, early diagnosis, and mental health support to reduce the global disease burden.

6. Ensure Ethical and Data Privacy Compliance:
Adhere strictly to medical data protection laws and ethical AI standards, ensuring patient confidentiality, consent, and transparency. This will build user trust and compliance with healthcare regulations.

These improvements would transform the project from a prototype diagnostic model into a scalable, intelligent, and trustworthy medical assistant that evolves with data, adapts to user needs, and supports evidence-based healthcare decision-making.

