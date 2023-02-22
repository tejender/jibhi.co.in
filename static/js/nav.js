// Get the search icon and search input elements
const searchIcon = document.getElementById("search-icon");
const searchInput = document.querySelector(".search-input");

// Add a click event listener to the search icon
searchIcon.addEventListener("click", function() {
// Toggle the 'search' and 'no-search' classes on the nav element
const nav = document.querySelector(".nav");
nav.classList.toggle("search");
nav.classList.toggle("no-search");

// Toggle the 'search-active' class on the search input element
searchInput.classList.toggle("search-active");
});

// Get the menu toggle button element
const menuToggle = document.querySelector(".menu-toggle");

// Add a click event listener to the menu toggle button
menuToggle.addEventListener("click", function() {
// Toggle the 'mobile-nav' class on the nav element
const nav = document.querySelector(".nav");
nav.classList.toggle("mobile-nav");

// Toggle the 'is-active' class on the menu toggle button
menuToggle.classList.toggle("is-active");
});
