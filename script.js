document.getElementById("translateBtn").addEventListener("click", function() {
  const text = document.getElementById("textInput").value;
  const targetLang = document.getElementById("languageSelect").value;

  if (text.trim() === "") {
      alert("Please enter text to translate.");
      return;
  }

  fetch("https://your-app-name.onrender.com/translate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: text, target_language: targetLang })
  })
  .then(response => response.json())
  .then(data => {
      document.getElementById("outputText").textContent = data.translated_text;
  })
  .catch(error => {
      console.error("Error:", error);
      alert("Translation failed. Try again.");
  });
});
