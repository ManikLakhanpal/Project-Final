let btn = document.getElementsByClassName("menu")[0];
let items = document.getElementsByClassName("imp")[0];

console.log(btn);

btn.addEventListener("click", function() {
    if (items.style.display == "none") {
        items.style.display = "flex";
    } else {
        items.style.display = "none";
    }
});
