function togglePaymentFields() {
    const cardInfo = document.getElementById("card-info");
    const paymentMethod = document.querySelector('input[name="payment-method"]:checked').value;
  
    if (paymentMethod === "cash") {
      cardInfo.classList.add("hidden");
    } else {
      cardInfo.classList.remove("hidden");
    }
  }

function togglePayeeFields() {
    const payeeInfo = document.getElementById("payee-info");
    const receiver = document.querySelector('input[name="receiver"]:checked').value;

    if (receiver === "self") {
        payeeInfo.classList.add("hidden");
    } else {
        payeeInfo.classList.remove("hidden");
    }
}
