var sitebody = document.body;

var popup = document.createElement('span');
popup.id = "draggableElement"; // Assign the ID "draggableElement"

//making the style
popup.style.position = "absolute"
popup.style.width = "200px";
popup.style.height = "150px";
popup.style.top = "10%";
popup.style.left = "10%";
popup.style.backgroundColor = "white";
popup.style.borderRadius = "15px";
popup.style.boxShadow = "5px 0px 10px black"
popup.style.overflowY = "auto";

//making text content for popup
var text = document.createElement('span');
text.style.position = "absolute";
text.style.width = "80%";
text.style.height = "10%";
text.style.top = "10%";
text.style.left = "10%";
text.innerText = "Ask me a question.";

//making response text content for popup
var response = document.createElement('span');
response.style.border = "1px solid rgb(200,200,200)";
response.style.position = "absolute";
response.style.width = "80%";
response.style.height = "20%";
response.style.top = "30%";
response.style.left = "10%";
response.innerText = "";
response.style.overflowY = "auto";

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



var popup = document.getElementById("draggableElement");
var isDragging = false;
var offsetX, offsetY;

// Function to handle the mouse down event
function onMouseDown(event) {
  isDragging = true;
  offsetX = event.clientX - popup.getBoundingClientRect().left;
  offsetY = event.clientY - popup.getBoundingClientRect().top;
}

// Function to handle the mouse move event
function onMouseMove(event) {
  if (isDragging) {
    var newX = event.clientX - offsetX;
    var newY = event.clientY - offsetY;

    popup.style.left = newX + "px";
    popup.style.top = newY + "px";
  }
}

// Function to handle the mouse up event
function onMouseUp() {
  isDragging = false;
}

// Add event listeners for mouse events
popup.addEventListener("mousedown", onMouseDown);
document.addEventListener("mousemove", onMouseMove);
document.addEventListener("mouseup", onMouseUp);




function respond() {
    question = textbox.value;
    response.innerText = "You asked: " + question;
}

