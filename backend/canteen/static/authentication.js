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

document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('registration-form');

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        const formData = new FormData(form);

        fetch('/register/', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            }
            throw new Error('Network response was not ok.');
        })
        .then(data => {
            console.log("Data received:", data); // Log the data to console
            if (data.message === 'User registered successfully') {
                openPopup(data.message);
                setTimeout(() => {
                    window.location.reload(); // Reload the page after showing the popup
                }, 2000); // Reload after 2 seconds (adjust as needed)
            } else {
                openPopup(data.message);
            }
        })
        .catch(error => {
            console.error('There was an error!', error);
            openPopup(data.message);
        });

        // Optionally, clear the form fields after submission
        form.reset();
    });
});


