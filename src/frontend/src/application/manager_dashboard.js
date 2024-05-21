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
              const chartDatasets = new Array();
              const cdata = {
                labels: monthsA,
                datasets: [
                  {
                    label: "My First Dataset",
                    data: [65, 59, 80, 81, 56, 55, 40],
                    fill: false,
                    borderColor: "rgb(75, 192, 192)",
                    tension: 0.1,
                  },
                  {
                    label: "My sec Dataset",
                    data: [100, 62, 22, 77, 56, 55, 40],
                    fill: false,
                    borderColor: "rgb(23, 111, 192)",
                    tension: 0.1,
                  },
                ],
              };
              console.warn(chartMonthsLabels);
              console.warn(datasetLabels);
              new Chart(quarterlyProgressElement, {
                type: "line",
                data: cdata,
                options: {
                  plugins: {
                    legend: {
                      display: true,
                      labels: {
                        color: "rgb(255, 99, 132)",
                      },
                    },
                  },
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
