import { useState, useRef, useEffect } from "react";
import "./App.css";

import Header from "./components/Header";
import ChatWindow from "./components/ChatWindow";
import MessageInput from "./components/MessageInput";
import QuickActions from "./components/QuickActions";

function App() {
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const chatEndRef = useRef(null);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages, loading]);

  async function sendMessage(customMessage = null) {
    const userMessage = customMessage || message;

    if (!userMessage.trim()) return;

    const updatedMessages = [
      ...messages,
      {
        sender: "user",
        text: userMessage,
      },
    ];

    setMessages(updatedMessages);

    setMessage("");

    setLoading(true);

    try {
      const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          messages: updatedMessages.map((msg) => ({
            role: msg.sender === "user" ? "user" : "assistant",
            content: msg.text,
          })),
        }),
      });

      const data = await response.json();

      setMessages((prev) => [
        ...prev,
        {
          sender: "ai",
          text: data.reply,
        },
      ]);
    } catch (error) {
      console.error(error);

      setMessages((prev) => [
        ...prev,
        {
          sender: "ai",
          text: "❌ Unable to connect to the server.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  }

  function sendQuickMessage(text) {
    sendMessage(text);
  }

  return (
    <div className="app">

      <Header />

      <ChatWindow
        messages={messages}
        loading={loading}
        chatEndRef={chatEndRef}
      />

      <QuickActions
        sendQuickMessage={sendQuickMessage}
      />

      <MessageInput
        message={message}
        setMessage={setMessage}
        sendMessage={sendMessage}
        loading={loading}
      />

    </div>
  );
}

export default App;