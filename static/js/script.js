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
        button.style.backgroundImage = '/static/images/tick.png';
        setTimeout(function () {
            button.style.backgroundImage = '/static/images/copy.png';
        }, 2000);
    });
}