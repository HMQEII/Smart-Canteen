function toggleChatbot() {
    var chatbotContainer = document.getElementById('chatbot-container');
    if (chatbotContainer.style.display === 'none') {
        chatbotContainer.style.display = 'block';
        // Load chatbot page content into container
        chatbotContainer.innerHTML = '<object type="text/html" data="http://127.0.0.1:8000/suggest_order/" width="100%" height="100%"></object>';
    } else {
        chatbotContainer.style.display = 'none';
    }
}