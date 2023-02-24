var width = window.innerWidth;
if (width<=600){
  var slideCount = 4
  var gap=20
}
if(width>500){
  var slideCount = 7
  var gap=30
}

var swiper = new Swiper(".mySwiper-cat", {
  slidesPerView: slideCount,
  spaceBetween: gap,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".cat-next",
    prevEl: ".cat-prev",
  },
});