"use strict";
/**
 * This will serialize form inputs
 * @typedef param
 * @param {Object} param - this is object param
 * @param {HTMLFormElement} param.formElement The form element
 * @param {Array} param.excludedFields Array of excluded fields
 * @param {boolean} param.isOrdered Order the returned object
 * @param {boolean} param.returnAsFormData Return inputs as FormData object
 * @param {Array} param.filesArray File(s) inputs names
 * @returns {Object|FormData} json object of all inputs
 */
const formInputSerializer = ({
  formElement,
  excludedFields = [],
  onlyRadioInputs = true,
  customInputsCssClass = null,
}) => {
  const serializedObject = {};
  if (formElement.dataset["formStep"]) {
    serializedObject["step"] = formElement.dataset["formStep"];
  }
  //   console.log(formElement.dataset);
  //   console.log(Array.from(formElement.elements));
  if (onlyRadioInputs === true) {
    const inputsElements = formElement.querySelectorAll("input[type='radio']:checked");
    const dataArray = new Array();
    inputsElements.forEach((element) => {
      const eleDataset = element.dataset;
      const question = eleDataset["question"];
      const stepIdx = eleDataset["stepIdx"];
      const value = element.value;
      const fullData = {
        question: question,
        step: stepIdx,
        value: value,
      };
      dataArray.push(fullData);
      // console.log(fullData);
    });
    serializedObject["inputs"] = dataArray;
  } else {
    const formInputs = formElement.querySelectorAll(`.${customInputsCssClass}`);
    const dataInputs = new Array();
    if (formInputs.length > 0) {
      formInputs.forEach((input) => {
        if (input.type === "checkbox" || input.type === "radio") {
          if (input.checked) {
            dataInputs.push({
              name: input.name,
              value: input.value,
            });
          }
        } else {
          dataInputs.push({
            name: input.name,
            value: input.value,
          });
        }
      });
      serializedObject["inputs"] = dataInputs;
    }
  }
  return serializedObject;
};
const validateStepsForm = (form) => {
  const inputs = Array.from(
    form.querySelectorAll('input[type="text"], input[type="radio"]'),
  );
  let isValid = true;

  inputs.forEach((input) => {
    if (input.type === "text" && input.value.trim() === "") {
      isValid = false;
      // You can customize the error handling here, such as displaying an error message or adding a CSS class to indicate the error.
      // console.log("Text input is empty:", input.name);
      return false;
    }

    if (
      input.type === "radio" &&
      !form.querySelector(`input[name="${input.name}"]:checked`)
    ) {
      isValid = false;
      // You can customize the error handling here, such as displaying an error message or adding a CSS class to indicate the error.
      // console.log("Radio input is not selected:", input.name);
      return false;
    }
  });

  return isValid;
};
/**
 * Enable or disable form fieldset items with form's submit button
 * @typedef param
 * @param {Object} param - this is object param
 * @param {HTMLFormElement} param.formElement HTML form element
 * @param {string} param.state this will enable or disable
 */
const disableAndEnableFieldsetItems = ({ formElement, state }) => {
  const stateLower = state.toLowerCase();
  const fieldset = formElement.querySelector("fieldset");
  const allFormInputs = formElement.querySelectorAll("input, select, textarea, button");
  const submitBtn = document.querySelector(`button[form=${formElement.id}]`);

  switch (stateLower) {
    case "enable":
    case "e":
    case "en":
      fieldset.disabled = false;
      break;
    case "disable":
    case "dis":
    case "d":
      fieldset.disabled = true;
      //   submitBtn.disabled = true;

      break;
    default:
      console.warn(`${stateLower} not defined!`);
      break;
  }
};

export { formInputSerializer, disableAndEnableFieldsetItems, validateStepsForm };
