function generateHash() {
  var text = document.getElementById('textInput').value;
  var hash = hashCode(text);
  document.getElementById('result').innerText = "Hash Value: " + hash;
  // Make the hash value available globally
  window.hashValue = hash;
}

function copyToClipboard() {
  // Create a temporary input element
  var tempInput = document.createElement("input");
  // Assign the hash value to the input value
  tempInput.value = window.hashValue;
  // Append the input to the body
  document.body.appendChild(tempInput);
  // Select the input
  tempInput.select();
  // Copy the selected text
  document.execCommand("copy");
  // Remove the temporary input
  document.body.removeChild(tempInput);
  alert("Hash copied to clipboard: " + window.hashValue);
}

// Hashing function
function hashCode(s) {
  var hash = 0, i, chr;
  if (s.length === 0) return hash;
  for (i = 0; i < s.length; i++) {
    chr   = s.charCodeAt(i);
    hash  = ((hash << 5) - hash) + chr;
    hash |= 0; // loun Convert to 32bit integer
  }
  return hash;
}
