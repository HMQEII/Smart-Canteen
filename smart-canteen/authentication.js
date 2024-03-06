function openPopup(message) {
    const popup = document.getElementById("popup");
    const popupMessage = document.getElementById("popup-message");
    popupMessage.textContent = message;
    popup.style.display = "block";
}

// Function to close the popup
function closePopup() {
    const popup = document.getElementById("popup");
    popup.style.display = "none";
}

function selectUser(button) {
    // Deselect all buttons
    var buttons = document.querySelectorAll('.userselec button');
    buttons.forEach(function(btn) {
        btn.classList.remove('selected');
    });
    
    // Select the clicked button
    button.classList.add('selected');
}