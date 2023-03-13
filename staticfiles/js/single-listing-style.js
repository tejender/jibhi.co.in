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


// modal position

function adjustModalPosition() {
  var urlBarHeight = window.outerHeight - window.innerHeight;
  var modal = document.getElementById("listing-gallery-modal-content");


  if (urlBarHeight > 0) {
    modal.style.marginTop = 50 + "px";
  } else {
    modal.style.marginTop = "0";
  }
}

window.addEventListener("resize", adjustModalPosition);