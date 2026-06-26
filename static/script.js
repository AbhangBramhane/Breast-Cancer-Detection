// ===============================
// Load Sample Data
// ===============================

let sampleData = {};

// Load samples.json when page loads
fetch("/static/samples.json")
.then(response => response.json())
.then(data => {
    sampleData = data;
})
.catch(error => {
    console.error("Unable to load samples.json", error);
});

// Fill all input fields
function fillForm(values){

    const inputs = document.querySelectorAll("input[type='number']");

    inputs.forEach((input,index)=>{

        if(index < values.length){

            input.value = values[index];

        }

    });

    // Scroll to Predict button
    document.querySelector(".btn-primary").scrollIntoView({
        behavior:"smooth",
        block:"center"
    });

}

// Load Benign Sample
function loadBenign(){

    if(sampleData.benign){

        fillForm(sampleData.benign);

    }else{

        alert("Sample data not loaded yet.");

    }

}

// Load Malignant Sample
function loadMalignant(){

    if(sampleData.malignant){

        fillForm(sampleData.malignant);

    }else{

        alert("Sample data not loaded yet.");

    }

}

// ===============================
// Reset Form
// ===============================

function resetForm() {

    const inputs = document.querySelectorAll("input[type='number']");

    inputs.forEach(input => {
        input.value = "";
    });

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });

}