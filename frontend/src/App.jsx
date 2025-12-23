import { useState } from "react";
import { extractData } from "./services/api";
import SchemaSelect from "./components/SchemaSelect";
import TextInput from "./components/TextInput";
import JsonView from "./components/JsonView";
import TableView from "./components/TableView";

function App() {
  const [schemaType, setSchemaType] = useState("contact_info");
  const [inputText, setInputText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  async function handleExtract() {
    setLoading(true);
    setError(null);

    // console.log("Sending schema:", schemaType);

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
    <div style={{ padding: "24px", maxWidth: "900px", margin: "0 auto" }}>
      <h2>Unstructured Text to JSON Extractor</h2>

      <SchemaSelect value={schemaType} onChange={setSchemaType} />
      <TextInput value={inputText} onChange={setInputText} />

      <button onClick={handleExtract} disabled={loading}>
        {loading ? "Extracting..." : "Extract"}
      </button>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {result && (
        <>
          <JsonView data={result} />
          <TableView data={result} />
        </>
      )}
    </div>
  );
}

export default App;
