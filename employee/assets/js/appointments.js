$(document).ready(function() {
    $(document).ready(function() {
        // When a join button is clicked
        $('.join-button').on('click', function() {
            // Hide the appointments container
            $('.appointments').hide();
            // Show the Meet UI
            $('.meet').show();
        });
    
        // When the complete appointment button is clicked
        $('.complete-appointment-button').on('click', function() {
            if (confirm('Are you sure you want to complete this appointment?')) {
                // Clear chat messages
                // Show the appointments container
                $('.appointments').show();
                // Hide the Meet UI
                $('.meet').hide();
                
                // Optional: Show completion message
                Toastify({
                    text: "Appointment completed successfully!",
                    duration: 3000,
                    gravity: "top",
                    position: "right",
                    backgroundColor: "#48c774",
                }).showToast();
            }
        });
    });


    $('.toggle-chat').click(function() {
        const videoSection = $('.video-section');
        const chatPanel = $('.chat-panel');
        
        if (chatPanel.is(':visible')) {
            chatPanel.hide();
            videoSection.removeClass('is-9');
        } else {
            chatPanel.show();
            videoSection.addClass('is-9');
        }
    });

    $('.close-chat').click(function() {
        $('.chat-panel').hide();
        $('.video-section').removeClass('is-9');
    });

    // Handle send message with Enter key
    $('.chat-input input').keypress(function(e) {
        if (e.which === 13) { // Enter key
            sendMessage();
        }
    });

    $('.send-message').click(sendMessage);

    function sendMessage() {
        const messageInput = $('.chat-input input');
        const message = messageInput.val().trim();
        
        if (message) {
            const messageElement = $(`
                <div class="message-bubble sent">
                    <p>${message}</p>
                    <small>${new Date().toLocaleTimeString()}</small>
                </div>
            `);
            $('.chat-messages').append(messageElement);
            messageInput.val('');
            $('.chat-messages').scrollTop($('.chat-messages')[0].scrollHeight);
        }
    }


    
});
