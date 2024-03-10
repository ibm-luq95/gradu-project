// This is the scss entry file
import "../styles/index.scss";
// import "../styles/app.scss";
import "animate.css";
import "@fortawesome/fontawesome-free/js/all.js";
import "@fortawesome/fontawesome-free/css/all.min.css";
import "../../node_modules/preline/dist/preline.js";
// We can import Bootstrap JS instead of the CDN link, if you do not use
// Bootstrap, please feel free to remove it.
// import "bootstrap/dist/js/bootstrap.bundle";
// eslint-disable-next-line no-unused-vars
import Chart from "chart.js/auto";

// We can import other JS file as we like

window.document.addEventListener("DOMContentLoaded", function () {
  window.console.log("dom ready 1");
  const employeePerformanceElement = document.querySelector(
    "canvas#employee-performance",
  );
  const departmentChartElement = document.querySelector("canvas#department-chart");
  const quarterlyProgressElement = document.querySelector("canvas#quarterly-progress");
  if (departmentChartElement) {
    new Chart(departmentChartElement, {
      type: "pie",
      data: {
        labels: [
          "Software Development",
          "Hardware Development",
          "IT Services",
          "Cyber Security",
          "Other",
        ],
        datasets: [
          {
            label: "Population (millions)",
            backgroundColor: ["#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850"],
            data: [2478, 5267, 734, 784, 433],
          },
        ],
      },
      options: {
        plugins: {
          legend: {
            position: "bottom",
          },
        },
        title: {
          display: true,
          text: "Predicted world population (millions) in 2050",
        },
      },
    });
  }
  if (quarterlyProgressElement) {
    new Chart(quarterlyProgressElement, {
      type: "line",
      data: {
        labels: [1500, 1600, 1700, 1750, 1800, 1850, 1900, 1950, 1999, 2050],
        datasets: [
          {
            data: [86, 114, 106, 106, 107, 111, 133, 221, 783, 2478],
            label: "Africa",
            borderColor: "#3e95cd",
            fill: false,
          },
          {
            data: [282, 350, 411, 502, 635, 809, 947, 1402, 3700, 5267],
            label: "Asia",
            borderColor: "#8e5ea2",
            fill: false,
          },
          {
            data: [168, 170, 178, 190, 203, 276, 408, 547, 675, 734],
            label: "Europe",
            borderColor: "#3cba9f",
            fill: false,
          },
          {
            data: [40, 20, 10, 16, 24, 38, 74, 167, 508, 784],
            label: "Latin America",
            borderColor: "#e8c3b9",
            fill: false,
          },
          {
            data: [6, 3, 2, 2, 7, 26, 82, 172, 312, 433],
            label: "North America",
            borderColor: "#c45850",
            fill: false,
          },
        ],
      },
      options: {
        title: {
          display: true,
          text: "World population per region (in millions)",
        },
      },
    });
  }
  if (employeePerformanceElement) {
    new Chart(employeePerformanceElement, {
      type: "doughnut",
      data: {
        labels: ["Healthy", "Burn Out", "Highly Stressed", "Mildly Stressed"],
        datasets: [
          {
            label: "Employees",
            backgroundColor: ["#4ade80", "#f87171", "#facc15", "#c084fc"],
            data: [2478, 5267, 734, 784, 433],
          },
        ],
      },
      options: {
        plugins: {
          legend: {
            position: "bottom",
          },
        },

        title: {
          display: true,
          text: "Predicted world population (millions) in 2050",
        },
      },
    });
  }
});
