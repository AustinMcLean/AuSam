

document.getElementById("attendance-form").addEventListener("submit", function (event) {
    
    // Needed this line to stop bug causing form to submit twice when I moved it to Django
    event.stopImmediatePropagation();
    // Prevent the default form submission
    event.preventDefault();

    // Get form data 
    var formData = new FormData(event.target);


    /*
    // Log the form data to the console for testing purposes
    for (var pair of formData.entries()) {
        console.log(pair[0] + ', ' + pair[1]);
    }
    alert("Form data logged to console. No data sent to the server.");
    */


    // Convert form data to a JSON object
    // TODO: do this individually for each field and have type specific checks for each
    var formDataObject = {};
    formData.forEach(function (value, key) {
        formDataObject[key] = value;
    });

    // Store the form data in local storage
    localStorage.setItem("formData", JSON.stringify(formDataObject));

    // Use a relative path to send the data to the Django view
    fetch('../../submit-rsvp/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formDataObject),
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from the server if needed
        console.log(data);
    })
    .catch(error => {
        // Handle errors
        console.error('Error:', error);
    });

    console.log(JSON.stringify(formDataObject));

    // Optionally provide user feedback
    alert("Form data stored locally. You can submit it later.");



    // Reset the form or redirect the user as needed
    event.target.reset();
});