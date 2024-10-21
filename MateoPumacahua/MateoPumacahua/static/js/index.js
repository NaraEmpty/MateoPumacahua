document.addEventListener('DOMContentLoaded', function() {
    var homeLink = document.getElementById('index-link');
    homeLink.addEventListener('click', function(e) {
        e.preventDefault();
        window.location.href = '/index/';
        homeLink.classList.add('clicked');
    });
});

