"use strict";

import JustValidate from "just-validate";
import { sendRequest } from "../utils/api";
import { CSRFINPUTNAME } from "../utils/constants";
import {
  disableAndEnableFieldsetItems,
  formInputSerializer,
} from "../utils/form_helpers";
import { showToastNotification } from "../utils/toasts";
// eslint-disable-next-line no-unused-vars
document.addEventListener("DOMContentLoaded", (_readyEvent) => {
  const contactFormSection = document.querySelector("section#contactFormSection");
  const contactAlertMessage = document.querySelector("div#contactAlertMessage");
  const contactMessageContent = document.querySelector("div#contactMessageContent");
  const contactSuccessSection = document.querySelector("section#contactSuccessSection");
  const contactForm = document.querySelector("form#contactForm");
  // const prelineErrorCssClasses =
  //   "py-3 px-4 block w-full border-red-500 rounded-lg text-sm focus:border-red-500 focus:ring-red-500 dark:bg-neutral-800 dark:border-neutral-700 dark:text-neutral-400";
  // const errorsArrayCssClasses = prelineErrorCssClasses.split(" ");
  if (contactForm) {
    const validate = new JustValidate("#contactForm");
    validate
      .addField("#first_name", [{ rule: "required" }])
      .addField("#last_name", [{ rule: "required" }])
      .addField("#email", [{ rule: "required" }, { rule: "email" }])
      .addField("#phone", [
        { rule: "required" },
        {
          rule: "customRegexp",
          value: /^(?:966|0)(?:\d{9})$/,
        },
      ])
      .addField("#message", [{ rule: "required" }]);
    // eslint-disable-next-line no-unused-vars
    validate.onSuccess((_event) => {
      // event.currentTarget.submit();
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
          disableAndEnableFieldsetItems({ formElement: contactForm, state: "e" });
        });
    });
  }
});
