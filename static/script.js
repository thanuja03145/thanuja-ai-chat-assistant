/* Custom JavaScript for Thanuja AI Chat Assistant */
function sendMessage() {
    console.log("Chat system initialized successfully.");
    const input = document.getElementById('userInput');
    const text = input.value.trim();
    if (text !== "") {
        input.value = "";
    }
}
