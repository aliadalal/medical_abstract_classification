// script.js

document.getElementById('predictionForm').addEventListener('submit', function (e) {
    e.preventDefault();
    
    const inputData = document.getElementById('inputData').value;
    const data = { input: inputData };
    
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = `Prediction: ${data.prediction}`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
