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
              const chartData = data["quarter_chart_data"];
              const quarterChart = data["quarter_chart"];
              const chartMonthsLabels = chartData["months"];
              const datasetLabels = data["classification_chart_data"].map(
                (item) => item["label"],
              );

              const monthsA = [
                "Jan",
                "Feb",
                "Mar",
                "Apr",
                "May",
                "Jun",
                "Jul",
                "Aug",
                "Sep",
                "Oct",
                "Nov",
                "Dec",
              ];
              const quarterChartDatasets = new Array();
              for (const key in quarterChart) {
                if (Object.hasOwnProperty.call(quarterChart, key)) {
                  const element = quarterChart[key];
                  const monthsTArray = element.map((element) => element["count"]);
                  let bgColor;
                  switch (key) {
                    case "Burned Out":
                      bgColor = "#f87171";
                      break;
                    case "Highly Stressed":
                      bgColor = "#facc15";
                      break;
                    case "Mildly Stressed":
                      bgColor = "#c084fc";
                      break;
                    case "Healthy":
                      bgColor = "#4ade80";
                      break;
                    default:
                      // Handle the default case if needed
                      break;
                  }
                  quarterChartDatasets.push({
                    label: key,
                    data: monthsTArray,
                    tension: 0.1,
                    fill: false,
                    borderColor: bgColor,
                  });
                }
              }
              const cdata = {
                labels: monthsA,
                datasets: quarterChartDatasets,
              };
              new Chart(quarterlyProgressElement, {
                type: "line",
                data: cdata,
                options: {
                  scales: {
                    y: {
                      beginAtZero: true,
                    },
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
