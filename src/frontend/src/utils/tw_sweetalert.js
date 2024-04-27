"use strict";

import Swal from "sweetalert2";

const sweetAlertMainConfig = ({
  icon = "info",
  title = "",
  text = "",
  footer = null,
}) => {
  // icons: success, error, warning, info, question
  return {
    icon: icon,
    title: title,
    text: text,
    allowOutsideClick: false,
    allowEscapeKey: false,
    footer: footer ? footer : null,
    customClass: {
      confirmButton: "",
    },
  };
};

const sweetAlertConfirmCallback = () => {
  const swalWithBootstrapButtons = Swal.mixin({
    customClass: {
      confirmButton: "btn btn-success",
      cancelButton: "btn btn-danger",
    },
    buttonsStyling: false,
  });
  swalWithBootstrapButtons
    .fire({
      title: "Are you sure?",
      text: "You won't be able to revert this!",
      icon: "warning",
      showCancelButton: true,
      confirmButtonText: "Yes, delete it!",
      cancelButtonText: "No, cancel!",
      reverseButtons: true,
    })
    .then((result) => {
      if (result.isConfirmed) {
        swalWithBootstrapButtons.fire({
          title: "Deleted!",
          text: "Your file has been deleted.",
          icon: "success",
        });
      } else if (
        /* Read more about handling dismissals below */
        result.dismiss === Swal.DismissReason.cancel
      ) {
        swalWithBootstrapButtons.fire({
          title: "Cancelled",
          text: "Your imaginary file is safe :)",
          icon: "error",
        });
      }
    });
};

export { sweetAlertMainConfig, sweetAlertConfirmCallback };
