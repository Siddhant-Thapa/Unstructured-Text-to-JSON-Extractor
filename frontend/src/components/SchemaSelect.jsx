function SchemaSelect({ value, onChange }) {
  return (
    <div>
      <label>Extraction Type</label>
      <select value={value} onChange={(e) => onChange(e.target.value)}>
        <option value="contact_info">Contact Info</option>
        <option value="job_requirements">Job Requirements</option>
        <option value="invoice_info">Invoice Info</option>
      </select>
    </div>
  );
}

export default SchemaSelect;
