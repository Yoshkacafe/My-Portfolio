document.addEventListener("DOMContentLoaded", main);

function main(){
    document.getElementById('burger').addEventListener('click', onclikkk);
    document.getElementById('burger_others').addEventListener('click', onclikkkForOtherPages);
    document.getElementById('primaire').addEventListener('click', showPrimaire);
}

bool = 0;

function onclikkk(){
    if (bool == 0)
    {
        document.getElementById('hidden_menu').style.display = "block";
        document.getElementById('burger').src = "img/cross-small.png";
        bool = 1;
    } else
    {
        document.getElementById('hidden_menu').style.display = "none";
        document.getElementById('burger').src = "img/menu-burger.png";
        bool = 0;
    }
}

function onclikkkForOtherPages(){
    if (bool == 0)
    {
        document.getElementById('hidden_menu').style.display = "block";
        document.getElementById('burger_others').src = "../img/cross-small.png";
        bool = 1;
    } else
    {
        document.getElementById('hidden_menu').style.display = "none";
        document.getElementById('burger_others').src = "../img/menu-burger.png";
        bool = 0;
    }
}

function showPrimaire(){

}