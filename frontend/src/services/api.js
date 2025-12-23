const API_URL = "http://127.0.0.1:8000/extract";

export async function extractData(schemaType, inputText) {
  const response = await fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      schema_type: schemaType,
      input_text: inputText,
    }),

  });
  

  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.detail || "Extraction failed");
  }

  return response.json();
}
