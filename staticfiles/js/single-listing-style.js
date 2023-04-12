var aboutModal = document.getElementById('about-listing-modal');
var openBtn = document.getElementById('read-more-btn');
var overlay = document.getElementById('overlay-wrapper')

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
function setModalBehavior(modal, openBtn, closeBtn) {
  var overlay = document.getElementById('overlay-wrapper');
  
  openBtn.addEventListener('click', function() {
    modal.classList.add('open');
    document.body.classList.add('no-scroll');
    
    setTimeout(function() {
      overlay.classList.add('overlay');
    }, 1000);
  });
  
  closeBtn.addEventListener('click', function() {
    document.body.classList.remove('no-scroll');
    overlay.classList.remove('overlay');
    
    setTimeout(function() {
      modal.classList.remove('open');
    }, 100);
  });
}




var galleryModal = document.getElementById('listing-gallery-modal');

var openGalleryBtn = document.getElementById('load-gallery');
var overlay = document.getElementById('overlay-wrapper')
var closeGalleryBtn = document.getElementById('close-gallery-modal');
setModalBehavior(galleryModal, openGalleryBtn, closeGalleryBtn);

// listing gallery ends

//////////////////////////// datepicker desktop

// enquiry modal
var enquiryModal = document.getElementById('enquiry-modal');

var openEnquiryBtn = document.getElementById('enquiry-btn');

var closeEnquiryBtn = document.getElementById('close-enquiry-modal-mobile');



openEnquiryBtn.addEventListener('click', function() {
  enquiryModal.classList.add('open');
  document.body.classList.add('no-scroll');
  
  setTimeout(function() {
    overlay.classList.add("overlay");
  }, 700);
});

closeEnquiryBtn.addEventListener('click', function() {
    document.body.classList.remove('no-scroll');
    overlay.classList.remove("overlay");    
    setTimeout(function() {
      enquiryModal.classList.remove('open');
    }, 100);
 
});

// emquiry-modal-ends


// Get the checkin and checkout date input elements
const checkinInput = document.querySelector('#enquiry-form-desktop #checkin-date');
const checkoutInput = document.querySelector('#enquiry-form-desktop #checkout-date');


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



// datepicker mobile
// Get the checkin and checkout date input elements
const checkinInputMobile = document.querySelector('#enquiry-modal-content #checkin-date');
const checkoutInputMobile = document.querySelector('#enquiry-modal-content #checkout-date');


// Set the minimum checkin date to the current date
checkinInputMobile.min = new Date().toISOString().split('T')[0];

// When the checkin date changes, set the minimum checkout date to the checkin date
checkinInputMobile.addEventListener('change', (event) => {
  checkoutInputMobile.min = event.target.value;
});

// When the checkout date changes, set the maximum checkin date to the checkout date
checkoutInputMobile.addEventListener('change', (event) => {
  checkinInputMobile.max = event.target.value;
});

// datepicker mobile ends



// <!-- Initialize Swiper -->

  var screen_size = window.innerWidth
  if (screen_size < 500){
      var slidesPerView = 1
  }
  else{
      var slidesPerView = 3
  }
  
  var swiper = new Swiper(".ReviewSwiperListing", {
    slidesPerView: slidesPerView,
    spaceBetween: 50,
    
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
  });


// small modal share

  function setSmallModalBehavior(modal, openBtn, closeBtn) {
    var overlay = document.getElementById('overlay-wrapper');
    
    openBtn.addEventListener('click', function() {
      modal.classList.add('open');
      document.body.classList.add('no-scroll');
      
      setTimeout(function() {
        overlay.classList.add('overlay');
      }, 1000);
    });
    
    closeBtn.addEventListener('click', function() {
      document.body.classList.remove('no-scroll');
      overlay.classList.remove('overlay');
      
      setTimeout(function() {
        modal.classList.remove('open');
      }, 100);
    });
  }




// reusable modal

function reusableModal(triggerId, modalId, overlayId, closeId) {
  var trigger = document.getElementById(triggerId);
  var modal = document.getElementById(modalId);
  var overlay = document.getElementById(overlayId);
  var close = document.getElementById(closeId);
  
  trigger.addEventListener('click', function() {
    overlay.classList.add('is-visible');
    modal.classList.add('is-visible');
    document.body.classList.add('no-scroll')
   
  });

  close.addEventListener('click', function() {
    overlay.classList.remove('is-visible');
    modal.classList.remove('is-visible');
    document.body.classList.remove('no-scroll')
   
  });

  
}
reusableModal('btn-modal', 'share-modal', 'overlay', 'close-btn-share-modal');



// accomodation modal

function initModal(openBtnID, modalID, closeBtnID, overlayID, openClass, closeClass) {
  const modal = document.getElementById(modalID);
  const openBtn = document.getElementById(openBtnID);
  const closeBtn = document.getElementById(closeBtnID);
  const overlay = document.getElementById(overlayID);

  openBtn.addEventListener('click', function() {
    console.log('hii');
    modal.classList.add(openClass);
    // document.body.classList.add('no-scroll');
    setTimeout(function() {
      overlay.classList.add('overlay');
    }, 1000);
  });

  closeBtn.addEventListener('click', function() {
    // document.body.classList.remove('no-scroll');
    overlay.classList.remove('overlay');
    setTimeout(function() {
      modal.classList.remove(openClass);
    }, 100);
  });
}

// Example usage
initModal('accomodation-btn', 'accomodation-modal', 'close-accomodation-modal', 'overlay-wrapper', 'open', 'close');
