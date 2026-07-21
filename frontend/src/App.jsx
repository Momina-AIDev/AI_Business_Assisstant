import { useState } from "react";

function App() {
  const [message, setMessage] = useState("");
  const [reply, setReply] = useState("");

  async function sendMessage() {
    try {
      const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          message: message,
        }),
      });

      const data = await response.json();
      setReply(data.reply);
    } catch (error) {
      console.error(error);
      setReply("Error connecting to backend.");
    }
  }

  return (
    <div style={{ padding: "40px" }}>
      <h1>AI Business Assistant</h1>

      <input
        type="text"
        placeholder="Type your message..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        style={{
          width: "300px",
          padding: "10px",
          marginRight: "10px",
        }}
      />

      <button onClick={sendMessage}>Send</button>

      <h3>Response</h3>
      <p>{reply}</p>
    </div>
  );
}

export default App;