// Handles sending text + action to FastAPI and updating the UI

async function processText(action) {
    const text = document.getElementById('userInput').value.trim();
    const outputBox = document.getElementById('outputBox');

    if (!text) {
        outputBox.textContent = "Please enter some text.";
        return;
    }

    outputBox.textContent = "Processing... Please wait.";

    try {
        const response = await fetch("http://localhost:8000/api/process", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                action: action,
                text: text
            })
        });

        const data = await response.json();

        if (!response.ok) {
            outputBox.textContent = "Error: " + (data.detail || "Unexpected server error");
            return;
        }

        // Display result
        outputBox.textContent = data.result;

    } catch (error) {
        outputBox.textContent = "Network error: " + error.message;
    }
}
// 


