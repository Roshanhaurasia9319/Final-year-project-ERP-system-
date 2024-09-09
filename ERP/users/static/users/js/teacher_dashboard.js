
document.getElementById('toggle-btn').addEventListener('click', function () {
    document.getElementById('sidebar').classList.toggle('active');
    document.getElementById('content').classList.toggle('active');
});

document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        events: '/calendar-data/',  // This should point to your view returning JSON data
        eventClick: function(info) {
            alert(info.event.title + ": " + info.event.extendedProps.description);
        }
    });

    calendar.render();
});
