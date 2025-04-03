document.addEventListener("DOMContentLoaded", function () {
    const inputContainer = document.getElementById("inputFields");
    const form = document.getElementById("predictionForm");
    const resultDisplay = document.getElementById("result");

    // Create 10 input fields dynamically
    for (let i = 0; i < 10; i++) {
        const input = document.createElement("input");
        input.type = "number";
        input.placeholder = `Feature ${i + 1}`;
        input.required = true;
        inputContainer.appendChild(input);
    }

    form.addEventListener("submit", async function (e) {
        e.preventDefault();

        // Collect input values
        const inputs = inputContainer.querySelectorAll("input");
        const features = Array.from(inputs).map(input => Number(input.value));

        try {
            const response = await fetch("http://127.0.0.1:5000/predict", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ features })
            });

            const data = await response.json();
            if (data.prediction) {
                resultDisplay.innerHTML = `<strong>Prediction:</strong> ${data.prediction}`;
                resultDisplay.style.color = data.prediction === "Malignant" ? "red" : "green";
            } else {
                resultDisplay.innerHTML = `<strong>Error:</strong> ${data.error}`;
                resultDisplay.style.color = "red";
            }
        } catch (error) {
            resultDisplay.innerHTML = `<strong>Error:</strong> Unable to connect to the server.`;
            resultDisplay.style.color = "red";
        }
    });
});
