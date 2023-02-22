var width = window.innerWidth;
if (width<=500){
  var slideCount = 4
}
if(width>500){
  var slideCount = 9
}
var swiper = new Swiper(".mySwiper", {
  slidesPerView: slideCount,
  spaceBetween: 60,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  
});