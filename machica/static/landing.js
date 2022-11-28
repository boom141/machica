// Get the navbar
var navbar = document.getElementById("navbar");
const nav_links = document.querySelectorAll('.mx-2')

// Get the offset position of the navbar
var sticky = navbar.offsetTop;

window.onscroll = function() {
  if (window.pageYOffset > 0) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
};

