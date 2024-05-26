"use strict";
/* eslint no-unused-vars: 0 */ 
import Swal from "sweetalert2";
import "sweetalert2/dist/sweetalert2.css";
import { HSOverlay, HSStepper } from "preline/dist/preline";
import {
  disableAndEnableFieldsetItems,
  formInputSerializer,
} from "../utils/form_helpers";
import { CSRFINPUTNAME, PRELINECSSLOADERHTML } from "../utils/constants";
import { showToastNotification } from "../utils/toasts";
import { sendRequest } from "../utils/api";
import { sweetAlertMainConfig } from "../utils/tw_sweetalert";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const surveySpinner = document.querySelector("#surveySpinner");
  const stepperReadyBadge = document.querySelector("#stepperReadyBadge");
  if (document.querySelector("#stepper")) {
    setTimeout(() => {
      console.warn("Init stepper...");
      stepperReadyBadge.classList.remove("hidden");
      stepperReadyBadge.classList.add(
        ...["animate__animated", "animate__fadeIn", "animate__faster"],
      );
      surveySpinner.classList.add("hidden");
      const fullStepsData = {};
      const surveyUrl = document.querySelector("input#survey_url").value;
      const step1FormElement = document.querySelector("form#step1Form");
      const step2FormElement = document.querySelector("form#step2Form");
      const step3FormElement = document.querySelector("form#step3Form");
      const step4FormElement = document.querySelector("form#step4Form");
      const step5FormElement = document.querySelector("form#step5Form");
      const formsArray = [
        step1FormElement,
        step2FormElement,
        step3FormElement,
        step4FormElement,
        step5FormElement,
      ];
      const stepper = new HSStepper(document.querySelector("#stepper"));
      let errorState = 1;
      stepper.on("reset", (currentIndex) => {
        step1FormElement.reset();
        step2FormElement.reset();
        step3FormElement.reset();
        step4FormElement.reset();
        step5FormElement.reset();
      });
      // console.log(stepper);
      stepper.on("beforeNext", (index) => {
        console.warn("ON beforeNext");
        console.warn(`Current Step ${index}`);
        if (index === 1) {
          const step1Inputs = formInputSerializer({
            formElement: step1FormElement,
            onlyRadioInputs: false,
            customInputsCssClass: "step-1-input",
          });
          //   console.warn(step1Inputs);
          fullStepsData["step1"] = step1Inputs["inputs"];
        } else if (index === 2) {
          const step2Inputs = formInputSerializer({ formElement: step2FormElement });
          // console.warn(step2Inputs);
          fullStepsData["step2"] = step2Inputs["inputs"];
        } else if (index === 3) {
          const step3Inputs = formInputSerializer({ formElement: step3FormElement });
          // console.warn(step3Inputs);
          fullStepsData["step3"] = step3Inputs["inputs"];
        } else if (index === 4) {
          const step4Inputs = formInputSerializer({ formElement: step4FormElement });
          // console.warn(step4Inputs);
          fullStepsData["step4"] = step4Inputs["inputs"];
        } else if (index === 5) {
          const step5Inputs = formInputSerializer({ formElement: step5FormElement });
          // console.warn(step5Inputs);
          fullStepsData["step5"] = step5Inputs["inputs"];
        }
      });

      // stepper.on("next", (currentStep) => {
      //   console.warn("ON NEXT");
      //   console.warn(`Current Step ${currentStep}`);

      // });
      stepper.on("finish", (step) => {
        console.warn("ON finish");
        const step5Inputs = formInputSerializer({ formElement: step5FormElement });
        // console.warn(step5Inputs);
        fullStepsData["step5"] = step5Inputs["inputs"];
        formsArray.forEach((form) => {
          disableAndEnableFieldsetItems({ formElement: form, state: "dis" });
        });

        const requestOptions = {
          method: "POST",
          dataToSend: fullStepsData,
          url: surveyUrl,
          token: step1FormElement[CSRFINPUTNAME].value,
        };
        console.log(requestOptions);
        // Swal.fire(sweetAlertMainConfig({ title: "Done", icon: "success" }));
        let timerInterval;
        const progressElement = Swal.mixin({
          html: "Please wait to classifying your survey...",
          title: "Classifying...",
          // timer: 2000,
          timerProgressBar: true,
          didOpen: () => {
            Swal.showLoading();
            const timer = Swal.getPopup().querySelector("b");
            const request = sendRequest(requestOptions);
            request
              .then((data) => {
                console.warn(data);
                const predictionData = data["results"]["data"];
                progressElement.close();
                const { element } = HSOverlay.getInstance("#survey-result-modal", true);
                element.open();
                const surveyResultModal = document.querySelector("#survey-result-modal");
                const surveyTitle = document.querySelector("#survey-result-modal-title");
                const surveyResultModalImg = document.querySelector(
                  "#survey-result-modal-img",
                );
                const surveyResultModalDescription = document.querySelector(
                  "p#survey-result-modal-description",
                );
                const surveyShortAdvice = document.querySelector(
                  "em#survey-short-advice",
                );
                const surveyConclusionAdvice = document.querySelector(
                  "p#survey-conclusion-advice",
                );
                const surveyRecommendationsList = document.querySelector(
                  "ol#survey-recommendations-list",
                );
                showToastNotification("TXT", "success");
                surveyResultModalImg.src = predictionData["image"];
                surveyTitle.textContent = predictionData["label"];
                surveyShortAdvice.textContent = predictionData["short_advice"];
                surveyResultModalDescription.textContent = predictionData["description"];
                surveyConclusionAdvice.textContent = predictionData["conclusion_advice"];
                predictionData["recommendations"].forEach((recItem) => {
                  const li = document.createElement("li");
                  li.classList.add(...["text-sm", "text-grey-500"]);
                  li.textContent = recItem["content"];
                  surveyRecommendationsList.appendChild(li);
                });

                // setTimeout(() => {
                //   Swal.fire(
                //     sweetAlertMainConfig({
                //       title: "Done",
                //       icon: "success",
                //       text: data["result"],
                //     }),
                //   );
                // }, 2000);
              })
              .catch((error) => {
                console.error(error);
                showToastNotification(`Error in survey!!`, "error");
                console.error(error);
              })
              .finally(() => {
                formsArray.forEach((form) => {
                  disableAndEnableFieldsetItems({ formElement: form, state: "en" });
                });
              });
          },
          willClose: () => {
            clearInterval(timerInterval);
          },
        });
        progressElement.fire().then((result) => {
          /* Read more about handling dismissals below */
          console.warn("sldfjs");
          // if (result.dismiss === Swal.DismissReason.timer) {
          //   console.log("I was closed by the timer");
          // }
        });

        setTimeout(() => {
          console.warn(fullStepsData);
        }, 2000);
      });
      /* stepper.on("beforeNext", (index) => {
          console.warn("ON beforeNext");
          if (index === 2) {
            stepper.setProcessedNavItem(index);
    
            setTimeout(() => {
              stepper.unsetProcessedNavItem(index);
              stepper.enableButtons();
    
              if (errorState) {
                stepper.goToNext();
              } else {
                stepper.setErrorNavItem(index);
              }
    
              errorState = !errorState;
            }, 2000);
          }
        }); */
    }, 1000);
  }
});
