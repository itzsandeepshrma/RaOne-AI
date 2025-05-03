// Basic RaOne AI UI JS
document.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("start-btn");
  const status = document.getElementById("status");

  btn.addEventListener("click", () => {
    status.innerText = "RaOne is listening...";
    btn.disabled = true;

    // Simulate processing delay
    setTimeout(() => {
      status.innerText = "Speak now.";
      btn.disabled = false;
    }, 2000);
  });
});
