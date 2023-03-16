// scrolling feature
		
var prevScrollPos = window.pageYOffset;
var bottomNav = document.getElementById("bottomNav");
var delay = 500; // Delay time in milliseconds
var timeoutId;

window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollPos < currentScrollPos) {
    bottomNav.classList.add("hide-nav");
  } else {
    bottomNav.classList.remove("hide-nav");
     // If the user stops scrolling, show the nav after a delay
     
  }
  prevScrollPos = currentScrollPos;
 
};


// search modal

var modal = document.querySelector(".search-modal-wrapper");
var triggerDesktop = document.querySelector(".trigger-desktop");
var closeButton = document.querySelector(".close-button");

function toggleModal() {
    modal.classList.toggle("show-modal");
    if (modal.classList.contains("show-modal")) {
        document.body.classList.add("no-scroll");
      } else {
        document.body.classList.remove("no-scroll");
      }
}

function windowOnClick(event) {
    if (event.currentTarget === closeButton) {
        toggleModal();
    }
}

triggerDesktop.addEventListener("click", toggleModal);
closeButton.addEventListener("click", toggleModal);
window.addEventListener("click", windowOnClick);

// price range
const priceRange = document.getElementById("price-range");
const minPrice = document.querySelector(".min-price");
const maxPrice = document.querySelector(".max-price");

// Update the min and max price labels when the user slides the range input
priceRange.addEventListener("input", () => {
  maxPrice.textContent = getMaxPrice(priceRange.value);
});

// Function to calculate the max price based on the current value of the range input
function getMaxPrice(currentValue) {
  const max = parseInt(priceRange.max);
  const percentage = parseInt(currentValue) / max;
  const maxPriceValue = Math.floor(percentage * 10000);
  return `${maxPriceValue}`;
}

// price range ends


