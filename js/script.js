
document.getElementById("attendance-form").addEventListener("submit", function (event) {
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
    var formDataObject = {};
    formData.forEach(function (value, key) {
        formDataObject[key] = value;
    });

    // Store the form data in local storage
    localStorage.setItem("formData", JSON.stringify(formDataObject));

    // Optionally provide user feedback
    alert("Form data stored locally. You can submit it later.");



    // Reset the form or redirect the user as needed
    event.target.reset();
});
