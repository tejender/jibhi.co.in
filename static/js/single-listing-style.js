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
