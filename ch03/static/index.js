let count = 0;

const countElement = document.getElementById("count");
const increaseButton = document.getElementById("increaseButton");
const sendButton = document.getElementById("sendButton");

increaseButton.addEventListener("click", function () {
    count++;
    countElement.textContent = count;
});

sendButton.addEventListener("click", function () {
    window.location.href = `/${count}`;
});
