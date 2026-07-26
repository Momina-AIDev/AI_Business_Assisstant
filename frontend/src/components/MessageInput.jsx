function MessageInput({
  message,
  setMessage,
  sendMessage,
  loading,
}) {
  return (
    <div className="input-area">

      <input
        type="text"
        placeholder="Type your message..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter") {
            sendMessage();
          }
        }}
      />

      <button
        onClick={sendMessage}
        disabled={loading}
      >
        {loading ? "Sending..." : "Send"}
      </button>

    </div>
  );
}

export default MessageInput;