import {marked} from "marked"; //importing the markdown converter

//handling markdown conversion and rendering
document.getElementById('convert-btn').addEventListener('click', e=>{ e.preventDefault(); //prevents native functionality for this event
	const markdownText = document.getElementById('markdown-editor').value;
	const htmlOutput = marked(markdownText); //Convert markdown to HTML
	document.getElementById('markdown-output').innerHTML = htmlOutput; //add the generated html code to the output div element
});

 
