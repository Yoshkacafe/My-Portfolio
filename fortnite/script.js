document.addEventListener("DOMContentLoaded", main);

function main(){
    document.getElementById('buurger').addEventListener('click', onclikkk);
}

bool = 0;

function onclikkk(){
    if (bool == 0)
    {
        document.getElementById('hidden_menu').style.display = "block";
        document.getElementById('hidden_menu').style.transition = "0.5s";
        bool = 1;
    } else
    {
        document.getElementById('hidden_menu').style.display = "none";
        document.getElementById('hidden_menu').style.transition = "0.5s";
        bool = 0;
    }
}