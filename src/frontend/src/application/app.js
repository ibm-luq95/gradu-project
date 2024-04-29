// This is the scss entry file
import "../styles/index.scss";
import "../styles/app.scss";
import "animate.css";
import "@fortawesome/fontawesome-free/js/all.js";
import "@fortawesome/fontawesome-free/css/all.min.css";
import "../../node_modules/preline/dist/preline.js";
// We can import Bootstrap JS instead of the CDN link, if you do not use
// Bootstrap, please feel free to remove it.
// import "bootstrap/dist/js/bootstrap.bundle";
// eslint-disable-next-line no-unused-vars
import "./manager_dashboard.js";
import "./survey.js";
import "./contact.js";

// We can import other JS file as we like

window.document.addEventListener("DOMContentLoaded", function () {
  window.console.log("dom ready 1");
  const allInputs = document.querySelectorAll(".tw-inputs");
  if (allInputs.length > 0) {
    allInputs.forEach((item) => {
      item.disabled = false;
      item.classList.remove("cursor-progress");
    });
  }
});
