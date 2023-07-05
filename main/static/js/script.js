// MODEL for contact
// If you want to trigger, add #btn-modal-contact 
// Get the modal
var modal = document.getElementById("modal-contact");

// Get the button that opens the modal
var btn = document.getElementById("btn-modal-contact");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {

  gtag('event', 'click_on_contact', {
    'app_name': 'paca',
    'screen_name': 'any'
  });
  
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}