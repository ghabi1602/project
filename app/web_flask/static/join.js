// api that creates a join
async function joinClass(classId) {
    try {
        const response = await fetch('/api/classes/join', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                class_id: classId,
            }),
        });

        const data = await response.json();
       if (response.ok) {
        alert(data.message);
    } else {
        alert(data.error || data.message);
    }
} catch (error) {
    console.error(error.message);
}
}
// Add event listener to all Join buttons
console.log('Script loaded successfully')
document.addEventListener('DOMContentLoaded', function () {
    const joinButtons = document.querySelectorAll('.join-btn');
    console.log('Join buttons found:', joinButtons.length); // Should log the number of buttons
    joinButtons.forEach(button => {
        button.addEventListener('click', function (event) {
            // Get the class_id from the data attribute
            const classId = event.currentTarget.getAttribute('data-class-id');

            // Call the function to join the class
            joinClass(classId);
        });
    });
});