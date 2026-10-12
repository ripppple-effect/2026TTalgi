const led = document.querySelector("#led");
const onButton = document.querySelector("#on");
const offButton = document.querySelector("#off");

onButton.addEventListener("click", function () {
  fetch("/on", { method: "GET" })
    .then(response => {
      if (!response.ok) {
        throw new Error("HTTP error " + response.status);
      }

      return response.text();
    })
    .then(result => {
      led.src = "/static/on.png";
    })
    .catch(error => {
      alert(error);
    });
});

offButton.addEventListener("click", function () {
  fetch("/off", { method: "GET" })
    .then(response => {
      if (!response.ok) {
        throw new Error("HTTP error " + response.status);
      }

      return response.text();
    })
    .then(result => {
      led.src = "/static/off.png";
    })
    .catch(error => {
      alert(error);
    });
});
