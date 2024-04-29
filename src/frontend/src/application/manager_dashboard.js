"use strict";
import Chart from "chart.js/auto";
import { FETCHURLNAMEURL } from "../utils/constants";
import { fetchUrlPathByName, sendRequest } from "../utils/api";
document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const managerDashboardElement = document.querySelector("#manager-dashboard");
  if (managerDashboardElement) {
    const chartCardLoaderCssClass = ".chart-card-loader";
    const chartCardWrapperCssClass = ".chart-card-wrapper";
    const quarterlyProgressSection = document.querySelector(
      "section#quarterly-progress-section",
    );
    const employeePerformanceSection = document.querySelector(
      "section#employee-performance-section",
    );
    const departmentChartSection = document.querySelector(
      "section#department-chart-section",
    );
    const employeePerformanceElement = employeePerformanceSection.querySelector(
      "canvas#employee-performance",
    );
    const departmentChartElement = departmentChartSection.querySelector(
      "canvas#department-chart",
    );
    const quarterlyProgressElement = quarterlyProgressSection.querySelector(
      "canvas#quarterly-progress",
    );
    const urlName = fetchUrlPathByName("dashboard:api");
    urlName
      .then((urlData) => {
        const url = urlData["urlPath"];
        const requestOptions = {
          method: "POST",
          url: url,
        };
        const request = sendRequest(requestOptions);
        request
          .then((data) => {
            if (departmentChartElement) {
              const chartData = data["departments_chart_data"];
              const chartLabels = chartData.map((item) => item["label"]);
              const chartValues = chartData.map((item) => item["count"]);
              new Chart(departmentChartElement, {
                type: "pie",
                data: {
                  labels: chartLabels,
                  datasets: [
                    {
                      // label: "Population (millions)",
                      backgroundColor: [
                        "#3e95cd",
                        "#8e5ea2",
                        "#3cba9f",
                        "#e8c3b9",
                        "#c45850",
                      ],
                      data: chartValues,
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
                    text: "All departments",
                  },
                },
              });
              departmentChartSection
                .querySelector(chartCardLoaderCssClass)
                .classList.add("hidden");
              departmentChartSection
                .querySelector(chartCardWrapperCssClass)
                .classList.remove("hidden");
            }
            if (quarterlyProgressElement) {
              console.log(data);
              const chartData = data["quarter_chart_data"];
              const chartMonthsLabels = chartData["months"];
              const datasetLabels = data["classification_chart_data"].map(
                (item) => item["label"],
              );
              const chartDatasets = new Array();

              console.warn(chartMonthsLabels);
              console.warn(datasetLabels);
              new Chart(quarterlyProgressElement, {
                type: "line",
                data: {
                  labels: chartMonthsLabels,
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
              quarterlyProgressSection
                .querySelector(chartCardLoaderCssClass)
                .classList.add("hidden");
              quarterlyProgressSection
                .querySelector(chartCardWrapperCssClass)
                .classList.remove("hidden");
            }
            if (employeePerformanceElement) {
              const chartData = data["classification_chart_data"];
              const chartLabels = chartData.map((element) => element.label);
              const chartValues = chartData.map((element) => element["surveys_count"]);
              new Chart(employeePerformanceElement, {
                type: "doughnut",
                data: {
                  labels: chartLabels,
                  datasets: [
                    {
                      label: "Employees",
                      backgroundColor: ["#4ade80", "#c084fc", "#facc15", "#f87171"],
                      data: chartValues,
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
              employeePerformanceSection
                .querySelector(chartCardLoaderCssClass)
                .classList.add("hidden");
              employeePerformanceSection
                .querySelector(chartCardWrapperCssClass)
                .classList.remove("hidden");
            }
          })
          .catch((error) => {
            console.error(error);
          });
      })
      .catch((error) => {
        console.error(error);
      });
  }
});
