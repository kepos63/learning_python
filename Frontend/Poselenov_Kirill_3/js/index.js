
//$("Селектор").команда(параметры);
function All() {
    //$(".card").hide();
    $(".card").show();
}
function drink() {
    $(".card").hide();
    $(".drink").show();
}
function soup() {
    $(".card").hide();
    $(".soup").show();
}
function garnish() {
    $(".card").hide();
    $(".garnish").show();
}
function salad() {
    $(".card").hide();
    $(".salad").show();
}





$(".filter0").click(All);
$(".filter1").click(drink);
$(".filter2").click(soup);
$(".filter3").click(garnish);
$(".filter4").click(salad);
