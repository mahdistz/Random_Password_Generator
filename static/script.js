function validateForm() {
       var checkboxes = document.querySelectorAll('input[type="checkbox"]');
       var atLeastOneChecked = Array.prototype.slice.call(checkboxes).some(function (checkbox) {
           return checkbox.checked;
       });

       if (!atLeastOneChecked) {
           document.getElementById('error-message').style.display = 'block';
           return false;
       } else {
           document.getElementById('error-message').style.display = 'none';
           return true;
       }
   }

   function copyPassword(button) {
       var passwordElement = document.getElementById('password-box');
       var password = passwordElement.innerText;

       navigator.clipboard.writeText(password).then(function () {
           button.innerText = 'Copied';
           button.style.backgroundColor = '#5cb85c';
           setTimeout(function () {
               button.innerText = 'Copy';
               button.style.backgroundColor = '#337ab7';
           }, 2000);
       });
   }