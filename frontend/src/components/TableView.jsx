import "./TableView.css";

function TableView({ data }) {
  return (
    <div className="table-view-container">
      <div className="table-view-header">
        <h3 className="table-view-title">
          <svg
            className="table-view-icon"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M3 10h18M3 14h18m-9-4v8m-7 0h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z"
            />
          </svg>
          Extracted Data
        </h3>
      </div>
      <table className="table-view-table">
        <tbody>
          {Object.entries(data).map(([key, value]) => (
            <tr key={key} className="table-view-row">
              <td className="table-view-key">{key.replace(/_/g, " ")}</td>
              <td className="table-view-value">
                {value === null && <span className="table-view-na">N/A</span>}

                {Array.isArray(value) && (
                  <ul className="table-view-list">
                    {value.map((item, index) => (
                      <li key={index} className="table-view-list-item">
                        {item}
                      </li>
                    ))}
                  </ul>
                )}

                {!Array.isArray(value) && value !== null && String(value)}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default TableView;
