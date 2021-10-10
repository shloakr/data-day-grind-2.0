const clearInput = () => {
  const input = document.getElementsByTagName("input")[0];
  input.value = "";
};

const clearBtn = document.getElementById("clear-btn");
clearBtn.addEventListener("click", clearInput);

document.getElementById("planet").style.display = "none";

function displayLoading() {
  console.log("Loading...");
  var x = document.getElementById("planet");
  x.style.display = "block";
}

