//script that creates a new class

// Define the API endpoint
const apiUrl = '/api/professor/class';

// Create a new class
async function createClass(classData) {
  try {
    // Send a POST request to the API
    const response = await fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(classData) // Convert the classData object to JSON
    });

    // Check if the request was successful
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    // Parse the JSON response
    const result = await response.json();
    console.log('Class created successfully:', result);

    // Optionally, you can reset the form or show a success message
    document.getElementById('classForm').reset();
  } catch (error) {
    console.error('Error creating class:', error);
  }
}

// Handle button click
document.getElementById('add_class').addEventListener('click', function() {
  // Get form data
  const className = document.getElementById('name').value;
  const professorField = document.getElementById('field').value;
  const classMaxStd = document.getElementById('max_std').value;

  // Create class data object
  const newClass = {
    name: className,
    field: professorField,
    maximum_number_of_students: classMaxStd
  };

  // Call the function to create a new class
  createClass(newClass);
});


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
        console.error('Error:', error);
    }
}
// Add event listener to all Join buttons
document.addEventListener('DOMContentLoaded', function () {
    const joinButtons = document.querySelectorAll('.join-btn');

    joinButtons.forEach(button => {
        button.addEventListener('click', function (event) {
            // Get the class_id from the data attribute
            const classId = event.target.getAttribute('data-class-id');
            console.log(classId)

            // Call the function to join the class
            joinClass(classId);
        });
    });
});







