function TableView({ data }) {
  return (
    <div>
      <h3>Table View</h3>
      <table border="1" cellPadding="8" style={{ width: "100%" }}>
        <tbody>
          {Object.entries(data).map(([key, value]) => (
            <tr key={key}>
              <td style={{ fontWeight: "bold", width: "30%" }}>{key}</td>
              <td>
                {value === null && "N/A"}

                {Array.isArray(value) && (
                  <ul style={{ margin: 0, paddingLeft: "18px" }}>
                    {value.map((item, index) => (
                      <li key={index}>{item}</li>
                    ))}
                  </ul>
                )}

                {!Array.isArray(value) && value !== null && value}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default TableView;
