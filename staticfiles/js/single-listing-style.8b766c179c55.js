var aboutModal = document.getElementById('about-listing-modal');
var openBtn = document.getElementById('read-more-btn');
var overlay = document.getElementById('overlay-wrapper')
console.log(openBtn);
var closeBtn = document.getElementById('close-modal');

openBtn.addEventListener('click', function() {
  aboutModal.classList.add('open');
  document.body.classList.add('no-scroll')
  setTimeout(function() {
    overlay.classList.add("overlay");
  }, 1000);
  

  
});

closeBtn.addEventListener('click', function() {
    document.body.classList.remove('no-scroll')
    overlay.classList.remove("overlay");
  setTimeout(function() {
    aboutModal.classList.remove('open');
  }, 100);
 
});



// listing galley

var galleryModal = document.getElementById('listing-gallery-modal');

var openGalleryBtn = document.getElementById('load-gallery');
var overlay = document.getElementById('overlay-wrapper')
var closeGalleryBtn = document.getElementById('close-gallery-modal');

openGalleryBtn.addEventListener('click', function() {
  galleryModal.classList.add('open');
  document.body.classList.add('no-scroll');
  
  setTimeout(function() {
    overlay.classList.add("overlay");
  }, 1000);
  

  
});

closeGalleryBtn.addEventListener('click', function() {
    document.body.classList.remove('no-scroll')
    overlay.classList.remove("overlay");
    console.log("hi");
  setTimeout(function() {
    galleryModal.classList.remove('open');
  }, 100);
 
});

// listing gallery ends

// datepicker

// Get the check-in and check-out date input elements
const checkinInput = document.getElementById('checkin-date');
const checkoutInput = document.getElementById('checkout-date');

// Set the minimum check-in and check-out dates to the current date
const currentDate = new Date().toISOString().split('T')[0];
checkinInput.min = currentDate;
checkoutInput.min = currentDate;

// When the check-in date changes, set the minimum checkout date to the check-in date
checkinInput.addEventListener('change', (event) => {
  checkoutInput.min = event.target.value;
});

// When the checkout date changes, set the maximum check-in date to the checkout date
checkoutInput.addEventListener('change', (event) => {
  checkinInput.max = event.target.value;
});// datepicker ends


// window.addEventListener("scroll", function() {
//   const navbar = document.querySelector(".nav-wrapper");
//   console.log(navbar);
//   navbar.classList.toggle("scrolled", window.scrollY > 0);
// });
// const navbar = document.querySelector(".nav-wrapper");
//   console.log(navbar);



// enquiry modal
var enquiryModal = document.getElementById('enquiry-modal');

var openEnquiryBtn = document.getElementById('enquiry-btn');

var closeEnquiryBtn = document.getElementById('close-enquiry-modal');

openEnquiryBtn.addEventListener('click', function() {
  enquiryModal.classList.add('open');
  document.body.classList.add('no-scroll');
  
 
  

  
});

closeEnquiryBtn.addEventListener('click', function() {
    document.body.classList.remove('no-scroll')
  setTimeout(function() {
    galleryModal.classList.remove('open');
  }, 100);
 
});

// emquiry-modal-ends
