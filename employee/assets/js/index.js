$(document).ready(function() {
    const validCredentials = {
        username: 'admin',
        password: 'admin123'
    };

    $('#loginForm').on('submit', function(e) {
        e.preventDefault();
        
        const username = $('#username').val();
        const password = $('#password').val();

        if (username === validCredentials.username && password === validCredentials.password) {
            // Redirect to dashboard
            window.location.href = 'dashboard.html';
        } else {
            // Show the error message
            $('#errorMessage').fadeIn();
        }
    });

    // Close notification when clicking the delete button
    $('.delete').on('click', function() {
        $('#errorMessage').fadeOut();
    });
});