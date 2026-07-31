function MessageBubble({ sender, text }) {
  const isUser = sender === "user";

  return (
    <div className={`message-row ${isUser ? "user-row" : "ai-row"}`}>

      <div className="avatar">
        {isUser ? "👤" : "🤖"}
      </div>

      <div className={`message ${isUser ? "user" : "ai"}`}>
        {text}
      </div>

    </div>
  );
}

export default MessageBubble;