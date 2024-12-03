$(document).ready(function() {
    let currentDate = new Date();
    
    function updateCalendar() {
        // Get current year and month
        const year = currentDate.getFullYear();
        const month = currentDate.getMonth();
        
        // Update month title
        const monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 
                          'July', 'August', 'September', 'October', 'November', 'December'];
        $('.title.is-4.mb-0').text(`${monthNames[month]} ${year}`);

        // Get first day of month and total days
        const firstDay = new Date(year, month, 1);
        const lastDay = new Date(year, month + 1, 0);
        const totalDays = lastDay.getDate();
        const startingDay = firstDay.getDay();

        // Clear existing calendar days
        $('.calendar-body').empty();

        // Sample appointments data (you can modify this)
        const appointmentsCount = {
            5: 2,  // 2 appointments on the 5th
            7: 1,  // 1 appointment on the 7th
            11: 3, // 3 appointments on the 11th
            19: 1, // 1 appointment on the 19th
            27: 2  // 2 appointments on the 27th
        };

        // Add previous month's days
        const prevMonthLastDay = new Date(year, month, 0).getDate();
        for (let i = startingDay - 1; i >= 0; i--) {
            $('.calendar-body').append(`<div class="has-text-grey-light">${prevMonthLastDay - i}</div>`);
        }

        // Add current month's days
        for (let day = 1; day <= totalDays; day++) {
            let classes = '';
            let title = '';
            
            // Check if day has appointments
            if (appointmentsCount[day]) {
                classes = 'has-background-primary-light';
                const count = appointmentsCount[day];
                title = `title="${count} appointment${count > 1 ? 's' : ''}"`;
            }
            
            $('.calendar-body').append(`<div class="${classes}" ${title}>${day}</div>`);
        }

        // Add next month's days
        const remainingCells = 42 - (startingDay + totalDays);
        for (let i = 1; i <= remainingCells; i++) {
            $('.calendar-body').append(`<div class="has-text-grey-light">${i}</div>`);
        }
    }

    // Add click handlers for navigation buttons
    $('#prevMonth').click(function() {
        currentDate.setMonth(currentDate.getMonth() - 1);
        updateCalendar();
    });

    $('#nextMonth').click(function() {
        currentDate.setMonth(currentDate.getMonth() + 1);
        updateCalendar();
    });

    // Initialize calendar
    updateCalendar();

    // Today's tasks Tab switching
    $('.tabs li').click(function() {
        const tabId = $(this).index();
        
        // Update active tab
        $('.tabs li').removeClass('is-active');
        $(this).addClass('is-active');
        
        // Show corresponding content
        $('.tab-content').addClass('is-hidden');
        $('.tab-content').eq(tabId).removeClass('is-hidden');
    });

    
    // Add click handler to appointment cards
    $('.card').click(function() {
        // Store a reference to the clicked card
        const clickedCard = $(this);

        // Get appointment details from the card
        const time = clickedCard.find('.level-item strong').text();
        const status = clickedCard.find('.tag').text();
        const patient = clickedCard.find('p:contains("Patient:")').text().replace('Patient:', '').trim();
        const service = clickedCard.find('p:contains("Service:")').text().replace('Service:', '').trim();
        const durationField = $('#modalDuration');
        let originalDuration = clickedCard.find('p:contains("Duration:")').text().replace('Duration:', '').trim();

        // Update modal with appointment details
        $('#modalDateTime').text(`Today, ${time}`);
        $('#modalStatus').html(`<span class="tag ${
            status === 'Confirmed' ? 'is-success' :
            status === 'Completed' ? 'is-info' :
            'is-warning'
        }">${status}</span>`);
        $('#modalPatient').text(patient);
        $('#modalService').text(service);
        durationField.text(originalDuration);

        // Show or hide buttons based on status
        if (status === 'Completed') {
            $('#editAppointment, #cancelAppointment').hide();
            $('#confirmAppointment').hide(); // Ensure confirm button is hidden
        } else if (status === 'Pending') {
            $('#editAppointment, #confirmAppointment, #cancelAppointment').show();
        } else {
            $('#editAppointment, #cancelAppointment').show();
            $('#confirmAppointment').hide(); // Ensure confirm button is hidden
        }

        // Show modal
        $('#appointmentModal').addClass('is-active');

        // Edit appointment handler
        $('#editAppointment').click(function() {
            // Make duration field editable
            durationField.attr('contenteditable', 'true').css({
                'border': '1px dashed #007BFF',
                'background-color': '#e7f1ff'
            });
    
            // Hide edit, cancel appointment, and close buttons
            $('#editAppointment, #cancelAppointment, #closeModal').hide();
    
            // Check if status is pending to hide the confirm button
            if ($('#modalStatus').text().trim() === 'Pending') {
                $('#confirmAppointment').hide();
            }
    
            // Add a save button to confirm changes
            if (!$('#saveChanges').length) {
                $('<button class="button is-success" id="saveChanges">Reschedule & Save</button>')
                    .insertAfter('#editAppointment')
                    .click(function() {
                        // Save changes and disable editing
                        durationField.attr('contenteditable', 'false').css({
                            'border': '',
                            'background-color': ''
                        });
    
                        // Update the duration text in the clicked card
                        clickedCard.find('p:contains("Duration:")').html(`<strong>Duration:</strong> ${durationField.text()}`);
                        originalDuration = durationField.text();
    
                        alert('Changes saved successfully');
                        $('#cancelChanges').remove(); // Remove the cancel button
                        $(this).remove(); // Remove the save button after saving
    
                        // Show the hidden buttons
                        $('#editAppointment, #cancelAppointment, #closeModal').show();
                        if ($('#modalStatus').text().trim() === 'Pending') {
                            $('#confirmAppointment').show();
                        }
                    });
            }
    
            // Add a cancel button to discard changes
            if (!$('#cancelChanges').length) {
                $('<button class="button is-danger is-light" id="cancelChanges">Cancel Changes</button>')
                    .insertAfter('#saveChanges')
                    .click(function() {
                        // Revert changes and disable editing
                        durationField.text(originalDuration).attr('contenteditable', 'false').css({
                            'border': '',
                            'background-color': ''
                        });
                        $('#saveChanges').remove(); // Remove the save button
                        $(this).remove(); // Remove the cancel button
    
                        // Show the hidden buttons
                        $('#editAppointment, #cancelAppointment, #closeModal').show();
                        if ($('#modalStatus').text().trim() === 'Pending') {
                            $('#confirmAppointment').show();
                        }
                    });
            }
        });
    });



    // Close modal handlers
    $('#closeModal').click(function() {
        $('#appointmentModal').removeClass('is-active');
    });

    // Confirm appointment handler
    $('#confirmAppointment').click(function() {
        alert('Appointment confirmed successfully');
        $('#appointmentModal').removeClass('is-active');
    });

    // Edit appointment handler
    // $('#editAppointment').click(function() {
    //     // Make time and duration fields editable
    //     const durationField = $('#modalDuration');
    //     let originalDuration = durationField.text(); // Store original value

    //     // Add visual indicators for editable fields
    //     durationField.attr('contenteditable', 'true').css({
    //         'border': '1px dashed #007BFF',
    //         'background-color': '#e7f1ff'
    //     });

    //     // Hide edit, cancel appointment, and close buttons
    //     $('#editAppointment, #cancelAppointment, #closeModal').hide();

    //     // Add a save button to confirm changes
    //     if (!$('#saveChanges').length) {
    //         $('<button class="button is-success" id="saveChanges">Reschedule & Save</button>')
    //             .insertAfter('#editAppointment')
    //             .click(function() {
    //                 // Save changes and disable editing
    //                 durationField.attr('contenteditable', 'false').css({
    //                     'border': '',
    //                     'background-color': ''
    //                 });

    //                 // Update the originalDuration with the new value
    //                 originalDuration = durationField.text();

    //                 alert('Changes saved successfully');
    //                 $('#cancelChanges').remove(); // Remove the cancel button
    //                 $(this).remove(); // Remove the save button after saving

    //                 // Show the hidden buttons
    //                 $('#editAppointment, #cancelAppointment, #closeModal').show();
    //             });
    //     }

    //     // Add a cancel button to discard changes
    //     if (!$('#cancelChanges').length) {
    //         $('<button class="button is-light" id="cancelChanges">Cancel Changes</button>')
    //             .insertAfter('#saveChanges')
    //             .click(function() {
    //                 // Revert changes and disable editing
    //                 durationField.text(originalDuration).attr('contenteditable', 'false').css({
    //                     'border': '',
    //                     'background-color': ''
    //                 });
    //                 $('#saveChanges').remove(); // Remove the save button
    //                 $(this).remove(); // Remove the cancel button

    //                                     // Show the hidden buttons
    //                 $('#editAppointment, #cancelAppointment, #closeModal').show();
    //             });
    //     }
    // });

    // Cancel appointment handler
    $('#cancelAppointment').click(function() {
        if (confirm('Are you sure you want to cancel this appointment?')) {
            alert('Appointment cancelled successfully');
            $('#appointmentModal').removeClass('is-active');
        }
    });

});