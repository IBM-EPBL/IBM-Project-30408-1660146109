document
  .getElementById("calorie-form")
  .addEventListener("submit", function (e) {
    document.getElementById("results").style.display = "none";

    document.getElementById("loading").style.display = "block";

    setTimeout(calculateCalories, 2000);

    e.preventDefault();
  });

if (
  age.value === "" ||
  weight.value === "" ||
  height.value === "" ||
  80 < age.value ||
  age.value < 21
) {
  errorMessage("Please make sure the values you entered are correct");
}

function errorMessage(error) {
  document.getElementById("results").style.display = "none";

  document.getElementById("loading").style.display = "none";
  const errorDiv = document.createElement("div");
  const card = document.querySelector(".card");
  const heading = document.querySelector(".heading");
  errorDiv.className = "alert alert-danger";
  errorDiv.appendChild(document.createTextNode(error));

  card.insertBefore(errorDiv, heading);

  setTimeout(clearError, 4000);
}

function clearError() {
  document.querySelector(".alert").remove();
}
