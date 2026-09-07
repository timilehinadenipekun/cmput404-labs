import { Picker } from "emoji-mart"; // Import the emoji picker

const pickerOptions = { onEmojiSelect: (emoji) => {
  const textarea = document.getElementById('markdown-editor');
  textarea.value += emoji.native; // Add selected emoji to the editor
}};
const picker = new Picker(pickerOptions);
document.getElementById('emoji-picker').appendChild(picker); // Add emoji picker to the DOM
