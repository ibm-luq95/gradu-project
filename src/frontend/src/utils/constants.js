const CSRFINPUTNAME = "csrfmiddlewaretoken";
const baseUrl = window.location.origin;
const FETCHURLNAMEURL = new URL(process.env.FETCHURLNAMEURL, baseUrl);
const PRELINECSSLOADERHTML = `<div class="animate-spin inline-block size-6 border-[3px] border-current border-t-transparent text-blue-600 rounded-full dark:text-blue-500" role="status" aria-label="loading">
<span class="sr-only">Loading...</span>
</div>`;
export { CSRFINPUTNAME, FETCHURLNAMEURL, PRELINECSSLOADERHTML };
