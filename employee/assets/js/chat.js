$(document).ready(function() {
    // Start chat button click handler
    $('#startChat').click(function() {
        // Hide initial state
        $('#initialState').addClass('is-hidden');
        // Show loading state
        $('#loadingState').removeClass('is-hidden');

        // After x seconds, show chat interface
        setTimeout(function() {
            $('#loadingState').addClass('is-hidden');
            $('#chatInterface').removeClass('is-hidden');
            addMessage('SYSTEM: Client joins the chat.', 'system', '');


            // Add welcome message from bot
            addMessage('Hello! How can I help you today?', 'received', 'GetHealthBot');
        
            // Show typing indicator for client
            setTimeout(function() {
                addTypingIndicator('Client');
                
                // Remove typing indicator and show message after 3 seconds
                setTimeout(function() {
                    removeTypingIndicator();
                    addMessage('Hello, I would like to consult on what exercises can help me relax.', 'received', 'Client');
                }, 2000);
            }, 600);
        }, 800);



    });

    // Send message handler
    $('#sendMessage').click(sendMessage);
    $('#messageInput').keypress(function(e) {
        if (e.which == 13) { // Enter key
            sendMessage();
        }
    });

    function sendMessage() {
        const message = $('#messageInput').val().trim();
        if (message) {
            // Add sent message with Dr. Alex name
            addMessage(message, 'sent', 'Dr. Alex');
            $('#messageInput').val('');

            setTimeout(function() {
                addMessage('SYSTEM: Client left the chat, please complete the chat session.', 'system', '');
            }, 500);

        }
    }

    function addMessage(text, type, sender) {
        const messageDiv = $('<div>').addClass('message').addClass(type);
        
        // Add sender name
        const senderSpan = $('<span>')
            .addClass('sender-name')
            .text(sender);
        
        // Add message text
        const textDiv = $('<div>')
            .addClass('message-text')
            .text(text);
        
        messageDiv.append(senderSpan, textDiv);
        
        $('#chatMessages').append(messageDiv);
        // Scroll to bottom
        $('#chatMessages').scrollTop($('#chatMessages')[0].scrollHeight);
    }

    function addTypingIndicator(sender) {
        const typingDiv = $('<div>').addClass('message received typing-indicator');
        const senderSpan = $('<span>')
            .addClass('sender-name')
            .text(sender + ' is typing...');
        
        const dotsDiv = $('<div>')
            .addClass('typing-dots')
            .html('<span></span><span></span><span></span>');
        
        typingDiv.append(senderSpan, dotsDiv);
        $('#chatMessages').append(typingDiv);
        $('#chatMessages').scrollTop($('#chatMessages')[0].scrollHeight);
    }

    function removeTypingIndicator() {
        $('.typing-indicator').remove();
    }

    // complete chat button click handler
    $('#completeChat').click(function() {
        // Show confirmation dialog
        if (confirm('Are you sure you want to complete this chat session?')) {
            // Clear chat messages
            $('#chatMessages').empty();
            
            // Reset input
            $('#messageInput').val('');
            
            // Hide chat interface
            $('#chatInterface').addClass('is-hidden');
            
            // Show initial state
            $('#initialState').removeClass('is-hidden');
            
            // Optional: Show completion message
            Toastify({
                text: "Chat session completed successfully!",
                duration: 3000,
                gravity: "top",
                position: "right",
                backgroundColor: "#48c774",
            }).showToast();
        }
    });
});