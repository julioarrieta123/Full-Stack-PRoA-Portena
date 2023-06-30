val1= document.getelementbyid("txt.input1").value
val2=document.getelementbyid("txt.input2").value

var carousel = document.querySelector('.carousel');
var images = carousel.getElementsByTagName('img');
var currentIndex = 0;
var prevButton = document.querySelector('.prev');
var nextButton = document.querySelector('.next');

function showImage(index) {
  for (var i = 0; i < images.length; i++) {
    images[i].style.display = 'none';
  }
  images[index].style.display = 'block';
}

function prevImage() {
  currentIndex = (currentIndex - 1 + images.length) % images.length;
  showImage(currentIndex);
}

function nextImage() {
  currentIndex = (currentIndex + 1) % images.length;
  showImage(currentIndex);
}

prevButton.addEventListener('click', prevImage);
nextButton.addEventListener('click', nextImage);

setInterval(nextImage, 2000); // Desplazamiento automático cada 2 segundos
