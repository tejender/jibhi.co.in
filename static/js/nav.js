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

var modal = document.querySelector(".modal");
var triggerDesktop = document.querySelector(".trigger-desktop");
var triggerMobile = document.querySelector(".trigger-mobile");
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