"use strict";

import { sendRequest } from "../utils/api";
import { CSRFINPUTNAME } from "../utils/constants";
import {
  disableAndEnableFieldsetItems,
  formInputSerializer,
} from "../utils/form_helpers";
import { showToastNotification } from "../utils/toasts";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const contactFormSection = document.querySelector("section#contactFormSection");
  const contactAlertMessage = document.querySelector("div#contactAlertMessage");
  const contactMessageContent = document.querySelector("div#contactMessageContent");
  const contactSuccessSection = document.querySelector("section#contactSuccessSection");
  const contactForm = document.querySelector("form#contactForm");
  if (contactForm) {
    contactForm.addEventListener("submit", (event) => {
      event.preventDefault();
      const inputs = formInputSerializer({
        formElement: contactForm,
        onlyRadioInputs: false,
        customInputsCssClass: "contact-inputs",
      });
      const cleanData = {};
      for (const input of inputs["inputs"]) {
        cleanData[input["name"]] = input["value"];
      }
      const requestOptions = {
        method: "POST",
        dataToSend: cleanData,
        url: contactForm.action,
        token: contactForm[CSRFINPUTNAME].value,
      };
      disableAndEnableFieldsetItems({ formElement: contactForm, state: "dis" });
      const request = sendRequest(requestOptions);
      request
        .then((data) => {
          contactMessageContent.textContent = data["msg"];
          setTimeout(() => {
            contactAlertMessage.classList.remove("hidden");
            contactAlertMessage.classList.add(
              ...["animate__animated", "animate__fadeIn", "animate__faster"],
            );
            contactFormSection.classList.add(
              ...["animate__animated", "animate__fadeOut", "animate__faster"],
            );
            contactSuccessSection.classList.remove("hidden");
            contactSuccessSection.classList.add(
              ...["animate__animated", "animate__fadeIn", "animate__faster"],
            );
          }, 1000);
        })
        .catch((error) => {
          console.error(error);
          showToastNotification(`Error while contact us!!`, "error");
          console.error(error);
        })
        .finally(() => {
          disableAndEnableFieldsetItems({ formElement: contactForm, state: "en" });
        });
    });
  }
});
