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


});