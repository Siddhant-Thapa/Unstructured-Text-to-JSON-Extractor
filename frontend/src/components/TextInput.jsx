import "./TextInput.css";

function TextInput({ value, onChange }) {
  return (
    <div className="text-input-container">
      <label className="text-input-label">Input Text</label>
      <textarea
        className="text-input-textarea"
        rows="6"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder="Paste your unstructured text here (email, invoice, job description, etc.)..."
      />
    </div>
  );
}

export default TextInput;
