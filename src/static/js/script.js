function increment() {
  fetch("/increment", { method: "POST" })
    .then((response) => response.json())
    .then((data) => {
      const { clicks = "0" } = data;
      document.getElementById("text").textContent = `${clicks} clicks`;
    });
}

function init() {
  fetch("/lastvalue", { method: "GET" })
    .then((response) => response.json())
    .then((data) => {
      const { clicks = "0" } = data;
      document.getElementById("text").textContent = `${clicks} clicks`;
    });
}

init();
