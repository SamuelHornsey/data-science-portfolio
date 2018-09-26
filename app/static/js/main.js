const err = () => {
  let inputs = document.querySelectorAll(".js-input");

  inputs.forEach(input => {
    input.classList.add("error");
  });

  document.querySelector(".js-error").classList.remove("hidden");
};

const check_for_result = url => {
  fetch(url)
    .then(res => res.json())
    .then(json => {
      if (json.status === "PENDING") {
        setTimeout(() => {
          check_for_result(url);
        }, 1000);
      } else {
        document.querySelector(
          ".js-result"
        ).innerHTML = `Your appliance energy usage should be ${Math.round(
          json.result
        )}Wh`;
        document.querySelectorAll(".js-input").forEach(input => {
          input.disabled = false;
        });
        document.querySelector(".js-message").classList.add("hidden");
      }
    });
};

const run = () => {
  let inputs = document.querySelectorAll(".js-input");
  let data = {};

  for (let input of inputs) {
    if (input.value === "") {
      err();
      return;
    }

    if (isNaN(input.value)) {
      err();
      return;
    }

    data[input.name] = parseFloat(input.value);
  }

  let params = {
    method: "POST",
    headers: {
      "Content-Type": "application/json; charset=utf-8"
    },
    body: JSON.stringify(data)
  };

  document.querySelector(".js-message").classList.remove("hidden");
  inputs.forEach(input => {
    input.disabled = true;
  });

  fetch("/api/calculate", params)
    .then(res => res.headers.get("Location"))
    .then(location => check_for_result(location));
};

const app = () => {
  document.querySelector(".js-calculate").addEventListener("click", run);
};

window.addEventListener("load", app);
