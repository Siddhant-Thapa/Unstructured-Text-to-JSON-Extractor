import "./SchemaSelect.css";

function SchemaSelect({ value, onChange }) {
  return (
    <div className="schema-select-container">
      <label className="schema-label">Extraction Type</label>
      <select
        className="schema-select"
        value={value}
        onChange={(e) => onChange(e.target.value)}
      >
        <option value="contact_info"> Contact Information</option>
        <option value="job_requirements"> Job Requirements</option>
        <option value="invoice_info"> Invoice Details</option>
      </select>
    </div>
  );
}

export default SchemaSelect;
