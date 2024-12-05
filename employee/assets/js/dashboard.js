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
        const appointmentsData = {
            5: [
                { time: '10:00 AM - 11:00 AM', title: 'Mental Health Consultation', status: 'Confirmed', duration: '1 hour' },
                { time: '2:00 PM - 2:30 PM', title: 'Regular Checkup', status: 'Pending', duration: '30 minutes' }
            ],
            7: [
                { time: '1:00 PM - 1:45 PM', title: 'Regular Checkup', status: 'Confirmed', duration: '45 minutes' }
            ],
            11: [
                { time: '9:00 AM - 10:00 AM', title: 'Physical Health Consultation', status: 'Confirmed', duration: '1 hour' },
                { time: '11:00 AM - 12:00 PM', title: 'Mental Health Consultation', status: 'Confirmed', duration: '1 hour' },
                { time: '2:30 PM - 3:15 PM', title: 'Physical Health Consultation', status: 'Pending', duration: '45 minutes' },
                { time: '3:30 PM - 4:10 PM', title: 'Regular Checkup', status: 'Pending', duration: '45 minutes' }
            ],
            19: [
                { time: '4:00 PM - 4:45 PM', title: 'Regular Checkup', status: 'Confirmed', duration: '45 minutes' }
            ],
            27: [
                { time: '12:00 PM - 12:30 PM', title: 'Regular Checkup', status: 'Pending', duration: '30 minutes' },
                { time: '5:00 PM - 6:00 PM', title: 'Regular Checkup', status: 'Confirmed', duration: '1 hour' }
            ]
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
            if (appointmentsData[day]) {
                classes = 'has-background-primary-light';
                const appointments = appointmentsData[day];
                title = `title="${appointments.length} appointment${appointments.length > 1 ? 's' : ''}"`;
            }
            
            $('.calendar-body').append(`
                <div class="${classes}" ${title} data-day="${day}">
                    ${day}
                </div>
            `);
        }
    
        // Add next month's days
        const remainingCells = 42 - (startingDay + totalDays);
        for (let i = 1; i <= remainingCells; i++) {
            $('.calendar-body').append(`<div class="has-text-grey-light">${i}</div>`);
        }
    
        // Create a dropdown container using Bulma's card component
        const dropdown = $('<div style="position: absolute; display: none; z-index: 1000; width: 400px;"></div>');
        const dropdownContent = $('<div class="card-content" style="background-color: white; border: 1px solid #ededed;"></div>');
        dropdown.append(dropdownContent);
        $('body').append(dropdown);
    
        let hideTimeout;
    
        // Add hover event to show/hide appointment previews
        $('.calendar-body div.has-background-primary-light').hover(
            function(event) {
                clearTimeout(hideTimeout); // Clear any existing hide timeout
                const day = $(this).data('day');
                const appointments = appointmentsData[day];
    
                // Populate the dropdown with appointment previews
                dropdownContent.empty();
                appointments.forEach(appointment => {
                    // Determine the appropriate Bulma class based on the status
                    let statusClass = '';
                    if (appointment.status === 'Confirmed') {
                        statusClass = 'is-success';
                    } else if (appointment.status === 'Pending') {
                        statusClass = 'is-warning';
                    } else {
                        statusClass = 'is-info'; // Default or other statuses
                    }
                
                    dropdownContent.append(`
                        <div class="box appointment-item" style="border: 1px solid #d2d2d2; display: flex; justify-content: space-between; align-items: center; gap: 10px;">
                            <div>
                                <p><strong>${appointment.time}</strong></p>
                                <p>${appointment.title}</p>
                            </div>
                            <div style="text-align: right; weight: 500px;">
                                <span class="tag ${statusClass}">${appointment.status}</span>
                                <p style="margin-top: 5px;">${appointment.duration}</p>
                            </div>
                        </div>
                    `);
                });
    
                // Position the dropdown
                const offset = $(this).offset();
                dropdown.css({
                    top: offset.top + $(this).outerHeight(),
                    left: offset.left,
                    display: 'block'
                });
            },
            function() {
                // Set a timeout to hide the dropdown
                hideTimeout = setTimeout(() => {
                    dropdown.hide();
                }, 200); // Adjust the delay as needed
            }
        );
    
        // Ensure dropdown hides when mouse leaves it
        dropdown.hover(
            function() {
                clearTimeout(hideTimeout); // Clear the hide timeout if hovering over the dropdown
            },
            function() {
                // Set a timeout to hide the dropdown
                hideTimeout = setTimeout(() => {
                    dropdown.hide();
                }, 300); // Adjust the delay as needed
            }
        );
    }

    // Add CSS for hover effect on appointment items
    $('<style>')
        .prop('type', 'text/css')
        .html(`
            .appointment-item:hover {
                background-color: #f5f5f5;
                cursor: pointer;
            }
        `)
        .appendTo('head');

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

        // Check if the click target is the start button
        if ($(event.target).closest('.start-button, .join-button').length) {
            return; // Exit the function if the start button was clicked
        }
        // Store a reference to the clicked card
        const clickedCard = $(this);

        // Get appointment details from the card
        let time = clickedCard.find('.level-item strong').text();
        const status = clickedCard.find('.tag').text();
        const patient = clickedCard.find('p:contains("Patient:")').text().replace('Patient:', '').trim();
        const service = clickedCard.find('p:contains("Service:")').text().replace('Service:', '').trim();
        const durationField = $('#modalDuration');
        let originalDuration = clickedCard.find('p:contains("Duration:")').text().replace('Duration:', '').trim();
       
        // Update modal with appointment details
        const dateText = status === 'Pending' ? 'Dec 11, 2024' : 'Dec 03, 2024';
        $('#modalDateTime').text(`${dateText} | ${time}`);
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
        $('#editAppointment').off('click').on('click', function() {

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

                        updateAppointmentTime();

                        const dateText = status === 'Pending' ? 'Dec 11, 2024' : 'Dec 03, 2024';
                        time = clickedCard.find('.level-item strong').text();
                        $('#modalDateTime').text(`${dateText} | ${time}`);
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

    // Cancel appointment handler
    $('#cancelAppointment').click(function() {
        if (confirm('Are you sure you want to cancel this appointment?')) {
            alert('Appointment cancelled successfully');
            $('#appointmentModal').removeClass('is-active');
        }
    });

    updateAppointmentTime();

    // Event delegation for dynamically added start buttons
    $(document).on('click', '.start-button', function(event) {
        // Redirect to the appointments page
        window.location.href = 'appointments.html';
    });


});

function updateAppointmentTime(){
    document.querySelectorAll('.card-content').forEach(card => {
        const timeElement = card.querySelector('.ml-2');
        const durationElement = Array.from(card.querySelectorAll('p')).find(p => p.textContent.includes('Duration:'));
    
        if (timeElement && durationElement) {
            // Extract the start time and duration
            let startTime = timeElement.textContent.trim();
            const durationText = durationElement.textContent.replace('Duration:', '').trim();
    
            // Check if the time already includes a range
            if (startTime.includes('-')) {
                startTime = startTime.split('-')[0].trim(); // Extract the first part as the start time
            }
    
            // Parse the start time
            const timeParts = startTime.match(/(\d+):(\d+)\s*(AM|PM)/i);
            if (!timeParts) {
                console.error('Invalid start time format:', startTime);
                return;
            }
    
            const startHour = parseInt(timeParts[1], 10);
            const startMinute = parseInt(timeParts[2], 10);
            const isPM = timeParts[3].toUpperCase() === 'PM';
            let startHour24 = isPM ? (startHour % 12) + 12 : startHour;
    
            // Parse the duration
            let durationMinutes = 0;
            let durationHours = 0;
            if (durationText.includes('hour')) {
                durationHours = parseInt(durationText.split(' ')[0], 10);
            } else if (durationText.includes('minute')) {
                durationMinutes = parseInt(durationText.split(' ')[0], 10);
            }
    
            if (isNaN(durationMinutes) && isNaN(durationHours)) {
                console.error('Invalid duration format:', durationText);
                return;
            }
    
            // Calculate end time
            const endDate = new Date();
            endDate.setHours(startHour24 + durationHours, startMinute + durationMinutes);
    
            const endHour = endDate.getHours();
            const endMinute = endDate.getMinutes();
            const endPeriod = endHour >= 12 ? 'PM' : 'AM';
            const endHour12 = endHour % 12 || 12; // Convert to 12-hour format
    
            // Format end time
            const formattedEndTime = `${endHour12}:${endMinute.toString().padStart(2, '0')} ${endPeriod}`;
    
            // Replace the time display with the new time range
            timeElement.textContent = `${startTime} - ${formattedEndTime}`;
        }
    });
}