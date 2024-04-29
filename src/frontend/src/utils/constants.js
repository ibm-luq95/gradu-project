const CSRFINPUTNAME = "csrfmiddlewaretoken";
const baseUrl = window.location.origin;
const FETCHURLNAMEURL = new URL(process.env.FETCHURLNAMEURL, baseUrl);
export { CSRFINPUTNAME, FETCHURLNAMEURL };
