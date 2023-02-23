var width = window.innerWidth;
if (width<=600){
  var slideCount = 4
  var gap=30
}
if(width>500){
  var slideCount = 9
  var gap=60
}

var swiper = new Swiper(".mySwiper", {
  slidesPerView: 3,
  spaceBetween: 30,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
});