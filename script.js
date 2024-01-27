function generateHash() {
  var text = document.getElementById('textInput').value;
  var hash = hashCode(text);
  document.getElementById('result').innerText = "Hash Value: " + hash;
}

// Hashing function
function hashCode(s) {
  var hash = 0, i, chr;
  if (s.length === 0) return hash;
  for (i = 0; i < s.length; i++) {
    chr   = s.charCodeAt(i);
    hash  = ((hash << 5) - hash) + chr;
    hash |= 0; // Convert to 32bit integer
  }
  return hash;
}
