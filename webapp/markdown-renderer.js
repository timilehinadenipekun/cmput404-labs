import { marked } from "marked"; // Import the markdown converter

// Handle rendering
window.addEventListener('load', () => {
    const markdownText = document.getElementById('content').innerHTML;
    const htmlOutput = marked(markdownText);
    const contentDiv = document.getElementById('content');
    contentDiv.innerHTML = htmlOutput;
    contentDiv.style.display = 'block';
});
