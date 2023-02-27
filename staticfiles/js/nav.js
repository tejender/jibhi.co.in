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