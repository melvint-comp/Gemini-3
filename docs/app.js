// Get DOM elements
const runDemoBtn = document.getElementById("run-demo");
const fraudScoreEl = document.getElementById("fraud-score");
const geminiExplanationEl = document.getElementById("gemini-explanation");

// Simulated backend URL
const API_URL = "http://localhost:8000/demo-event"; // Replace with real API endpoint

// Demo function
async function runDemo() {
  try {
    fraudScoreEl.innerText = "Fraud Score: Running...";
    geminiExplanationEl.innerText = "Explanation: Waiting...";

    // Fetch detection result
    const response = await fetch(API_URL);
    const data = await response.json();

    // Update UI
    fraudScoreEl.innerText = `Fraud Score: ${data.score.toFixed(3)}`;
    geminiExplanationEl.innerText = `Explanation: ${data.explanation}`;
  } catch (error) {
    fraudScoreEl.innerText = "Fraud Score: Error";
    geminiExplanationEl.innerText = "Explanation: Error connecting to backend";
    console.error(error);
  }
}

// Attach event
runDemoBtn.addEventListener("click", runDemo);