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







