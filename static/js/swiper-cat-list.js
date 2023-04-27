var width = window.innerWidth;
var slideCount, gap;

if (width <= 600) {
  slideCount = 4;
  gap = 20;
} else {
  slideCount = 7;
  gap = 30;
}

// Set the initial value of initialSlide to 0
var initialSlide = 0;

var activeCat='';


activeCat = document.querySelector(".active-cat");

// Get the link inside the active category element


  const link = activeCat.querySelector('a') ;
  
  
  // Get the id attribute of the link element
  // const linkId = link.getAttribute('id');
  const linkId = link.getAttribute('id') ;



// Create the swiper instance

  
  if (linkId=='treehouse'){
    initialSlide=0
  }
  else if (linkId=='cottage'){
    initialSlide=1
  }
  else if (linkId=='homestay'){
    initialSlide=2
  }
  
  else if (linkId=='aframe'){
    initialSlide=3
  }
  else  if (linkId=='camping'){
    initialSlide=4
  }
  else if (linkId=='dome'){
    initialSlide=5
  }
  else if (linkId=='mudhouse'){
    initialSlide=6
  }



var swiper = new Swiper(".mySwiper-cat", {
  slidesPerView: slideCount,
  spaceBetween: gap,
  initialSlide: initialSlide,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".cat-next",
    prevEl: ".cat-prev",
  },
});
