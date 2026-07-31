function QuickActions({ sendQuickMessage }) {
  const actions = [
    "🍽 Reserve a Table",
    "📋 Show Today's Menu",
    "🕒 Opening Hours",
    "📍 Get Directions",
    "📞 Contact Us ",
  ];

  return (
    <div className="quick-actions">
      {actions.map((action) => (
        <button
          key={action}
          className="quick-btn"
          onClick={() => sendQuickMessage(action)}
        >
          {action}
        </button>
      ))}
    </div>
  );
}

export default QuickActions;