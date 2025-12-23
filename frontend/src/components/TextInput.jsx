function TextInput({ value, onChange }) {
  return (
    <div>
      <label>Input Text</label>
      <textarea
        rows="6"
        style={{ width: "100%" }}
        value={value}
        onChange={(e) => onChange(e.target.value)}
      />
    </div>
  );
}

export default TextInput;
