var sitebody = document.body;

var popup = document.createElement('span');

//making the style
popup.style.position = "absolute"
popup.style.width = "200px";
popup.style.height = "150px";
popup.style.top = "10%";
popup.style.left = "10%";
popup.style.backgroundColor = "white";
popup.style.borderRadius = "15px";
popup.style.boxShadow = "5px 0px 10px black"

//making text content for popup
var text = document.createElement('span');
text.style.position = "absolute";
text.style.width = "80%";
text.style.height = "10%";
text.style.top = "20%";
text.style.left = "10%";
text.innerText = "Ask me a question.";

//making response text content for popup
var response = document.createElement('span');
response.style.position = "absolute";
response.style.width = "80%";
response.style.height = "60%";
response.style.top = "40%";
response.style.left = "10%";
response.innerText = "";

//making text box for popup
var textbox = document.createElement("input");
textbox.style.position = "absolute";  
textbox.style.width = "80%";
textbox.style.height = "15%";
textbox.style.top = "60%";
textbox.style.left = "10%";
textbox.style.zIndex = "1000";
textbox.type = "text"; 



//making button to confirm question
var confirm_button = document.createElement('span');
confirm_button.style.position = "absolute";
confirm_button.style.width = "20%";
confirm_button.style.height = "15%";
confirm_button.style.top = "80%";
confirm_button.style.left = "40%";
confirm_button.innerText = "Ask";
confirm_button.style.backgroundColor = "grey ";
confirm_button.style.borderRadius = "3px";
confirm_button.style.zIndex = "1000";
confirm_button.onclick = function() {respond()};
confirm_button.style.cursor = "pointer";

popup.appendChild(textbox);
popup.appendChild(confirm_button);
popup.appendChild(text);
popup.appendChild(response);
sitebody.appendChild(popup);







function respond() {
    question = textbox.value;
    response.innerText = "You asked: " + question;
}

