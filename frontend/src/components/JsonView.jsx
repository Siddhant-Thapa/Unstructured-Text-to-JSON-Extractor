import "./JsonView.css";

function JsonView({ data }) {
  return (
    <div className="json-view-container">
      <div className="json-view-header">
        <h3 className="json-view-title">
          <svg
            className="json-view-icon"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"
            />
          </svg>
          Raw JSON Output
        </h3>
      </div>
      <pre className="json-view-pre">{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}

export default JsonView;
