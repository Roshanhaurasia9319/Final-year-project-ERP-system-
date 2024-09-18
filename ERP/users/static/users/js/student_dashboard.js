

// Add event listeners to sidebar items
const sidebarItems = document.querySelectorAll('.sidebar-item');

sidebarItems.forEach(item => {
    item.addEventListener('click', () => {
        // Remove active class from all sidebar items
        sidebarItems.forEach(i => i.classList.remove('active'));

        // Add active class to the clicked item
        item.classList.add('active');
    });
});

// Add event listeners to course view buttons
const courseViewButtons = document.querySelectorAll('.course-item button');

courseViewButtons.forEach(button => {
    button.addEventListener('click', () => {
        // Get the course title from the parent card
        const courseTitle = button.parentElement.querySelector('.card-title').textContent;

        // Do something with the course title, e.g., navigate to a new page
        console.log(`Viewing course: ${courseTitle}`);
    });
});

