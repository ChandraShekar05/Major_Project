    document.addEventListener('DOMContentLoaded', async function() {
        // Fetch the column names from the server
        const response = await fetch('/columns');
        const columns = await response.json();

        // Store the column names for later use
        window.columns = columns;
    });

    document.getElementById('fetch-form').addEventListener('submit', async function(event) {
        event.preventDefault();
        
        const dataset = document.getElementById('dataset').value;
        const index = document.getElementById('index').value;
        const response = await fetch(`/transaction/${dataset}/${index}`);
        const transaction = await response.json();

        // Populate the "amount" input field with the transaction details
        const amountInput = document.getElementById('amount');
        if (amountInput && transaction['Amount'] !== undefined) {
            amountInput.value = transaction['Amount'];
        }

        // Store the fetched transaction details in a global variable
        window.transactionDetails = transaction;
    });

    document.getElementById('prediction-form').addEventListener('submit', async function(event) {
        event.preventDefault();
        
        const formData = new FormData(event.target);
        const data = {};
        formData.forEach((value, key) => {
            data[key] = parseFloat(value);
        });

        // Add the other fields with fetched values
        window.columns.forEach(column => {
            if (!data.hasOwnProperty(column)) {
                data[column] = parseFloat(window.transactionDetails[column] || 0);
            }
        });

        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        // Append the result to the #result div
        const resultDiv = document.getElementById('result');
        resultDiv.innerText = `Prediction: ${result.prediction}`;

        // Ensure the container grows dynamically
        const container = document.querySelector('.container');
        container.style.height = 'auto'; // Allow the container to grow
        container.style.overflowY = 'visible'; // Ensure scrolling if needed
    });