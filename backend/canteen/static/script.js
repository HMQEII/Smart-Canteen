
const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const ForgotPasswordLink = document.querySelector('.forgot-password-link');
const btnPopup = document.querySelector('.btnLogin-popup');
const tncPopup = document.querySelector('.tnc-popup');
const iconClose = document.querySelector('.icon-close');
const services = document.querySelector('.s_one');

registerLink.addEventListener('click', () => {
  wrapper.classList.remove('Factive');
  wrapper.classList.add('active'); // Add the 'active' class to the wrapper
});

ForgotPasswordLink.addEventListener('click', () => {
  wrapper.classList.remove('active');
  wrapper.classList.add('Factive'); // Add the 'active' class to the wrapper
});


loginLink.addEventListener('click', () => {
  wrapper.classList.remove('active');
  wrapper.classList.remove('Factive');
});

btnPopup.addEventListener('click', () => {
  wrapper.classList.add('active-popup');
});

tncPopup.addEventListener('click', () => {
  wrapper.classList.add('active-popup');
});

iconClose.addEventListener('click', () => {
  wrapper.classList.remove('active-popup');
});

window.onload = function () {
  window.scrollTo(0, 0);
};

// Function to handle smooth scrolling to the target element
function scrollToElement(target, offset) {
  const element = document.querySelector(target);
  if (element) {
    const offsetTop = element.offsetTop - offset;
    window.scrollTo({
      top: offsetTop,
      behavior: 'smooth',
    });
  }
}

// Add click event listeners to the links
const links = document.querySelectorAll('a[href^="#"]');
if (links) {
  links.forEach((link) => {
    link.addEventListener('click', function (event) {
      event.preventDefault(); // Prevent default link behavior
      const headerHeight = 100; // Replace this with the actual height of your header in pixels
      const targetId = this.getAttribute('href');
      scrollToElement(targetId, headerHeight);
    });
  });
}

function limitInputLength(element, maxLength) {
    if (element.value.length > maxLength) {
        element.value = element.value.slice(0, maxLength);
    }
}

setTimeout(function () {
  document.querySelector('.loading-screen').style.display = 'none';
  document.querySelector('.main-content').style.display = 'block';
}, 20);

const searchBox = document.getElementById('search-box');
const searchContainer = document.querySelector('.search-cont');

searchBox.addEventListener('focus', function () {
  searchContainer.classList.add('active');
});

searchBox.addEventListener('blur', function () {
  searchContainer.classList.remove('active');
});

// For search bar
const searchForm = document.querySelector('form');

searchForm.addEventListener('submit', function (event) {
  event.preventDefault();
  const searchTerm = searchBox.value.trim();
  // Perform your search logic here (for example, redirecting to the search URL)
  if (searchTerm) {
    window.location.href = `https://www.google.com/search?q=${encodeURIComponent(searchTerm)}`;
  }
  searchBox.value = ''; // Clear the search box after the search is performed
});

searchBox.addEventListener('input', function() {
  const searchTerm = this.value;
});

searchBox.addEventListener('keypress', function(event) {
  if (event.key === 'Enter') {
    const searchTerm = this.value;
    const searchUrl = 'https://www.google.com/search?q=' + encodeURIComponent(searchTerm);
    window.open(searchUrl, '_blank');
  }
});