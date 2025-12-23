import { useState } from "react";
import { extractData } from "./services/api";
import SchemaSelect from "./components/SchemaSelect";
import TextInput from "./components/TextInput";
import JsonView from "./components/JsonView";
import TableView from "./components/TableView";
import "./App.css";

function App() {
  const [schemaType, setSchemaType] = useState("contact_info");
  const [inputText, setInputText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  async function handleExtract() {
    setLoading(true);
    setError(null);

    try {
      const response = await extractData(schemaType, inputText);
      setResult(response.data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="app-container">
      <div className="app-wrapper">
        <div className="app-card">
          <div className="app-header">
            <h1 className="app-title">Unstructured Text to JSON Extractor</h1>
            <p className="app-subtitle">
              Transform messy text into structured data instantly
            </p>
          </div>

          <SchemaSelect value={schemaType} onChange={setSchemaType} />
          <TextInput value={inputText} onChange={setInputText} />

          <button
            className="extract-button"
            onClick={handleExtract}
            disabled={loading || !inputText.trim()}
          >
            {loading && <span className="spinner"></span>}
            {loading ? "Extracting..." : "Extract Data"}
          </button>

          {error && <div className="error-message">{error}</div>}

          {result && (
            <div className="results-section fade-in">
              <JsonView data={result} />
              <TableView data={result} />
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
