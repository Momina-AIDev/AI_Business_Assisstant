import MessageBubble from "./MessageBubble";

function ChatWindow({ messages, loading, chatEndRef }) {
  return (
    <div className="chat">
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
          text="Thinking..."
        />
      )}

      <div ref={chatEndRef}></div>
    </div>
  );
}

export default ChatWindow;