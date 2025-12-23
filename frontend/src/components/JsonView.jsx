function JsonView({ data }) {
  return (
    <div>
      <h3>Raw JSON</h3>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}

export default JsonView;
