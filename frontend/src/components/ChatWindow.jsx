import MessageBubble from "./MessageBubble";

function ChatWindow({ messages, loading, chatEndRef }) {
  return (
    <div className="chat">

      {messages.length === 0 && (
        <div className="welcome-card">
          <h2>👋 Welcome to Demo Restaurant</h2>

          <p>
            I'm your AI Assistant.
          </p>

          <ul>
            <li>🍽 Reserve a table</li>
            <li>📋 View our menu</li>
            <li>🕒 Check opening hours</li>
            <li>📍 Find our location</li>
            <li>📞 Contact the restaurant</li>
          </ul>
        </div>
      )}

      {messages.map((msg, index) => (
        <MessageBubble
          key={index}
          sender={msg.sender}
          text={msg.text}
        />
      ))}

      {loading && (
        <MessageBubble
          sender="ai"
          text="AI is typing..."
        />
      )}

      <div ref={chatEndRef}></div>

    </div>
  );
}

export default ChatWindow;