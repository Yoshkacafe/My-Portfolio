document.addEventListener("DOMContentLoaded", main);

function main(){
    document.getElementById('big_button_infos_mobile').addEventListener('click', showPrimaire);
    document.getElementById('clear').addEventListener('click', unshowPrimaire);
    document.getElementById('big_button_infos_mobile2').addEventListener('click', showCollege);
    document.getElementById('clear2').addEventListener('click', unshowCollege);
    document.getElementById('big_button_infos_mobile3').addEventListener('click', showLycee);
    document.getElementById('clear3').addEventListener('click', unshowLycee);
    document.getElementById('lil_button_infos_mobile').addEventListener('click', showRobotique);
    document.getElementById('lil_clear').addEventListener('click', unshowRobotique);
    document.getElementById('lil_button_infos_mobile2').addEventListener('click', showGame);
    document.getElementById('lil_clear2').addEventListener('click', unshowGame);
    document.getElementById('lil_button_infos_mobile3').addEventListener('click', showIntertaleInteractive);
    document.getElementById('lil_clear3').addEventListener('click', unshowIntertaleInteractive);
    document.getElementById('lil_button_infos_mobile4').addEventListener('click', showDelta);
    document.getElementById('lil_clear4').addEventListener('click', unshowDelta);
    document.getElementById('lil_button_infos_mobile5').addEventListener('click', showKwix);
    document.getElementById('lil_clear5').addEventListener('click', unshowKwix);
    document.getElementById('lil_button_infos_mobile6').addEventListener('click', showNoka);
    document.getElementById('lil_clear6').addEventListener('click', unshowNoka);
    document.getElementById('lil_button_infos_mobile7').addEventListener('click', showYourHouse);
    document.getElementById('lil_clear7').addEventListener('click', unshowYourHouse);
}

function showPrimaire(){
    document.getElementById('big_block').style.display = "block";
}

function unshowPrimaire(){
    document.getElementById('big_block').style.display = "none";
}

function showCollege(){
    document.getElementById('big_block2').style.display = "block";
}

function unshowCollege(){
    document.getElementById('big_block2').style.display = "none";
}

function showLycee(){
    document.getElementById('big_block3').style.display = "block";
}

function unshowLycee(){
    document.getElementById('big_block3').style.display = "none";
}

function showRobotique(){
    document.getElementById('lil_block').style.display = "block";
}

function unshowRobotique(){
    document.getElementById('lil_block').style.display = "none";
}

function showGame(){
    document.getElementById('lil_block2').style.display = "block";
}

function unshowGame(){
    document.getElementById('lil_block2').style.display = "none";
}

function showIntertaleInteractive(){
    document.getElementById('lil_block3').style.display = "block";
}

function unshowIntertaleInteractive(){
    document.getElementById('lil_block3').style.display = "none";
}

function showDelta(){
    document.getElementById('lil_block4').style.display = "block";
}

function unshowDelta(){
    document.getElementById('lil_block4').style.display = "none";
}

function showKwix(){
    document.getElementById('lil_block5').style.display = "block";
}

function unshowKwix(){
    document.getElementById('lil_block5').style.display = "none";
}

function showNoka(){
    document.getElementById('lil_block6').style.display = "block";
}

function unshowNoka(){
    document.getElementById('lil_block6').style.display = "none";
}

function showYourHouse(){
    document.getElementById('lil_block7').style.display = "block";
}

function unshowYourHouse(){
    document.getElementById('lil_block7').style.display = "none";
}