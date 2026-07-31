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
        placeholder="Ask about reservations, menu..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter" && !loading) {
            sendMessage();
          }
        }}
      />

      <button
        onClick={sendMessage}
        disabled={loading}
      >
        {loading ? "..." : "Send"}
      </button>

    </div>
  );
}

export default MessageInput;