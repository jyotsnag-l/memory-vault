import { useState } from "react";
import "./App.css";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function askQuestion() {
    if (!question.trim()) {
      return;
    }

    setLoading(true);
    setAnswer("");
    setError("");

    try {
      const response = await fetch("http://localhost:8000/ask", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question: question,
        }),
      });

      if (!response.ok) {
        throw new Error("Failed to get an answer");
      }

      const data = await response.json();

      setAnswer(data.answer);
    } catch (error) {
      console.error(error);
      setError("Unable to connect to the backend.");
    } finally {
      setLoading(false);
    }
  }

  function handleKeyDown(event) {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault();
      askQuestion();
    }
  }

  return (
    <main className="app">
      <header className="header">
        <div className="brand">
          <span className="brand-mark">M</span>
          <span>Memory Vault</span>
        </div>

        <div className="status">
          <span className="status-dot"></span>
          Knowledge Base
        </div>
      </header>

      <section className="main-content">
        <div className="question-section">
          <h1>Ask your knowledge base.</h1>

          <div className="question-area">
            <label htmlFor="question">Your question</label>

            <div className="input-wrapper">
              <textarea
                id="question"
                rows="3"
                placeholder="What would you like to know?"
                value={question}
                onChange={(event) => setQuestion(event.target.value)}
                onKeyDown={handleKeyDown}
              />

              <button
                type="button"
                onClick={askQuestion}
                disabled={loading || !question.trim()}
              >
                {loading ? "..." : "Ask"}
              </button>
            </div>
          </div>
        </div>

        <div className="answer-section">
          <div className="section-heading">RESULT</div>

          <div className="answer-box">
            {loading ? (
              <p className="placeholder">Searching...</p>
            ) : error ? (
              <p className="error">{error}</p>
            ) : answer ? (
              <p className="answer">{answer}</p>
            ) : (
              <p className="placeholder">Your answer will appear here.</p>
            )}
          </div>
        </div>
      </section>
    </main>
  );
}

export default App;