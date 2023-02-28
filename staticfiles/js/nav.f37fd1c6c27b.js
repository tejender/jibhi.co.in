var prevScrollPos = window.pageYOffset;
var bottomNav = document.getElementById("bottomNav");

window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollPos < currentScrollPos) {
    bottomNav.classList.add("hide-nav");
  } else {
    bottomNav.classList.remove("hide-nav");
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
const rangeInput = document.querySelectorAll(".range-input input"),
  priceInput = document.querySelectorAll(".price-input input"),
  range = document.querySelector(".slider .progress");
let priceGap = 500;

priceInput.forEach((input) => {
  input.addEventListener("input", (e) => {
    let minPrice = parseInt(priceInput[0].value),
      maxPrice = parseInt(priceInput[1].value);

    if (maxPrice - minPrice >= priceGap && maxPrice <= rangeInput[1].max) {
      if (e.target.className === "input-min") {
        rangeInput[0].value = minPrice;
        range.style.left = (minPrice / rangeInput[0].max) * 100 + "%";
      } else {
        rangeInput[1].value = maxPrice;
        range.style.right = 100 - (maxPrice / rangeInput[1].max) * 100 + "%";
      }
    }
  });
});

rangeInput.forEach((input) => {
  input.addEventListener("input", (e) => {
    let minVal = parseInt(rangeInput[0].value),
      maxVal = parseInt(rangeInput[1].value);

    if (maxVal - minVal < priceGap) {
      if (e.target.className === "range-min") {
        rangeInput[0].value = maxVal - priceGap;
      } else {
        rangeInput[1].value = minVal + priceGap;
      }
    } else {
      priceInput[0].value = minVal;
      priceInput[1].value = maxVal;
      range.style.left = (minVal / rangeInput[0].max) * 100 + "%";
      range.style.right = 100 - (maxVal / rangeInput[1].max) * 100 + "%";
    }
  });
});

// price range ends


// datepicker

// Get the checkin and checkout date input elements
const checkinInput = document.getElementById('checkin-date');
const checkoutInput = document.getElementById('checkout-date');

// Set the minimum checkin date to the current date
checkinInput.min = new Date().toISOString().split('T')[0];

// When the checkin date changes, set the minimum checkout date to the checkin date
checkinInput.addEventListener('change', (event) => {
  checkoutInput.min = event.target.value;
});

// When the checkout date changes, set the maximum checkin date to the checkout date
checkoutInput.addEventListener('change', (event) => {
  checkinInput.max = event.target.value;
});

// datepicker ends