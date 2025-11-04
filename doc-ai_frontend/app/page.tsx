"use client";

import { useState, useEffect } from "react";
import { v4 as uuidv4 } from "uuid";

export default function Page() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [sessionId, setSessionId] = useState(null);
  const [followUpOptions, setFollowUpOptions] = useState([]);

  // Initialize session ID
  useEffect(() => {
    const storedId = localStorage.getItem("session_id");
    if (storedId) {
      setSessionId(storedId);
    } else {
      const newId = uuidv4();
      setSessionId(newId);
      localStorage.setItem("session_id", newId);
    }
  }, []);

  const sendMessage = async (text) => {
    if (!text.trim()) return;

    // Add user message
    setMessages((prev) => [...prev, { sender: "user", text }]);
    setInput("");
    setFollowUpOptions([]); // clear any previous follow-ups

    // Call backend
    try {
      const res = await fetch("http://localhost:8000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ session_id: sessionId, text }),
      });
      const data = await res.json();

      setMessages((prev) => [
        ...prev,
        { sender: "bot", text: data.bot_message },
      ]);

      // Handle follow-up if uncertain
      if (data.status === "uncertain" && data.follow_up) {
        setFollowUpOptions(data.follow_up);
      }
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { sender: "bot", text: "⚠️ Error connecting to the backend." },
      ]);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter") sendMessage(input);
  };

  const handleFollowUpClick = (option) => {
    sendMessage(option);
  };

  return (
    <div style={{ maxWidth: "600px", margin: "2rem auto", fontFamily: "sans-serif" }}>
      <h1>Doc-AI Chatbot</h1>

      <div
        style={{
          border: "1px solid #ccc",
          padding: "1rem",
          minHeight: "400px",
          overflowY: "auto",
        }}
      >
        {messages.map((msg, idx) => (
          <div
            key={idx}
            style={{
              textAlign: msg.sender === "user" ? "right" : "left",
              margin: "0.5rem 0",
            }}
          >
            <span
              style={{
                display: "inline-block",
                padding: "0.5rem 1rem",
                borderRadius: "12px",
                background: msg.sender === "user" ? "#0070f3" : "#eaeaea",
                color: msg.sender === "user" ? "#fff" : "#000",
              }}
            >
              {msg.text}
            </span>
          </div>
        ))}

        {/* Follow-up options */}
        {followUpOptions.length > 0 && (
          <div style={{ marginTop: "1rem" }}>
            <p>🤔 Can you clarify?</p>
            {followUpOptions.map((option, idx) => (
              <button
                key={idx}
                onClick={() => handleFollowUpClick(option)}
                style={{
                  margin: "0.25rem",
                  padding: "0.5rem 1rem",
                  borderRadius: "8px",
                  border: "1px solid #0070f3",
                  background: "#fff",
                  cursor: "pointer",
                }}
              >
                {option}
              </button>
            ))}
          </div>
        )}
      </div>

      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyPress={handleKeyPress}
        placeholder="Type your symptoms..."
        style={{ width: "100%", padding: "0.5rem", marginTop: "1rem" }}
      />
      <button
        onClick={() => sendMessage(input)}
        style={{ marginTop: "0.5rem", width: "100%" }}
      >
        Send
      </button>

      <p style={{ marginTop: "1rem", fontSize: "0.8rem" }}>
        ⚠️ Disclaimer: Doc-AI provides informational support only, not a medical diagnosis.
      </p>
    </div>
  );
}
