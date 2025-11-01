//фильтр
//$("Селектор").команда(параметры);
function All() {
    //$(".card").hide();
    $(".product-card").show();
}
function drink() {
    $(".product-card").hide();
    $(".drink").show();
}
function soup() {
    $(".product-card").hide();
    $(".soup").show();
}
function garnish() {
    $(".product-card").hide();
    $(".garnish").show();
}
function salad() {
    $(".product-card").hide();
    $(".salad").show();
}


$(".filter-all").click(All);
$(".filter-drink").click(drink);
$(".filter-soup").click(soup);
$(".filter-garnish").click(garnish);
$(".filter-salad").click(salad);


//модальное окно

let modalBtn = document.getElementById("modal");
let modalActive = document.getElementById("content-modal");
let notScroll = document.getElementById("body");
let modalBtnClose = document.getElementById("close-modal");


function openModal() {

    modalActive.classList.add("active");
    notScroll.classList.add("not-scroll");


}

function closeModal() {

    modalActive.classList.remove("active");
    notScroll.classList.remove("not-scroll");

}

modalBtn.addEventListener("click", openModal);
modalBtnClose.addEventListener("click", closeModal);

