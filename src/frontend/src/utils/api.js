"use strict";

import { getCookie } from "./cookie";

/**
 * This function will send a request to backend server
 * @param {Object} options json object of all options of the request
 * @returns Promise
 */
const sendRequest = (options) => {
  return new Promise((resolve, reject) => {
    try {
      const url = options["url"];
      const controller = new AbortController(); // the AbortController
      const { signal } = controller;
      const headers = new Headers({
        "Content-Type": options["contentType"] ?? "application/json;charset=utf-8",
        Accept: "application/json",
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": options["token"] ? options["token"] : getCookie("csrftoken"),
      });
      const fetchOptions = {
        method: options["method"],
        mode: "same-origin",
        credentials: "include",
        cache: "no-cache",
        body: JSON.stringify(options["dataToSend"]),
        // body: formData,
      };
      const request = new Request(url, {
        headers: headers,
        signal: signal,
      });
      const fetchObj = fetch(request, fetchOptions);
      fetchObj
        .then((response) => {
          if (!response.ok) {
            return response.text().then((text) => {
              reject(JSON.parse(text));
            });
          }
          resolve(response.json());
        })
        .catch((error) => {
          reject(error);
        });
    } catch (error) {
      reject(error);
    }
  });
};

export { sendRequest };
