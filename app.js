// --- PERSON D SETUP FOR PERSON C ---
// Elements already selected for Person C:
const chatForm = document.getElementById("chat-form");
const chatInput = document.getElementById("chat-input");
const chatWindow = document.getElementById("chat-window");

// Helper Function: Appends a message bubble to the chat log
function appendMessage(text, className) {
  const messageElement = document.createElement("div");
  messageElement.className = `message ${className}`;
  messageElement.textContent = text;

  chatWindow.appendChild(messageElement);
  // Auto-scroll to the bottom of the chat
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

// Form Submission Handler
chatForm.addEventListener("submit", async (e) => {
  e.preventDefault();

  const userText = chatInput.value.trim();
  if (!userText) return;

  // 1. Display User Message on UI
  appendMessage(userText, "user-message");
  chatInput.value = "";

  // -------------------------------------------------------------
  // TODO (PERSON C): CONNECT TO PERSON B'S BACKEND CHAT ENDPOINT
  // -------------------------------------------------------------
  try {
    const response = await fetch("http://localhost:3000/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: userText }),
    });

    const data = await response.json();

    // 2. Display Bot Response from Backend
    appendMessage(data.reply, "bot-message");
  } catch (error) {
    appendMessage("Sorry, I am unable to connect right now.", "bot-message");
  }
});
