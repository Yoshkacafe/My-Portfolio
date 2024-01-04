document.addEventListener("DOMContentLoaded", main);

function main(){
    document.getElementById('intertale_image').addEventListener('click' , showIntertaleInteractiveProject);
    document.getElementById('close_infos').addEventListener('click' , unshowIntertaleInteractiveProject);
    // document.getElementById('kwix_image').addEventListener('click' , showKwixProject);
    // document.getElementById('close_infos_2').addEventListener('click' , unshowKwixProject);
    // document.getElementById('noka_image').addEventListener('click' , showNokaProject);
    // document.getElementById('close_infos_3').addEventListener('click' , unshowNokaProject);
    document.getElementById('chess_image').addEventListener('click' , showChessProject);
    document.getElementById('close_infos_4').addEventListener('click' , unshowChessProject);
    document.getElementById('fq_image').addEventListener('click' , showFightQuestProject);
    document.getElementById('close_infos_5').addEventListener('click' , unshowFightQuestProject);
    document.getElementById('intertale_site_image').addEventListener('click' , showIntertaleWeb);
    document.getElementById('close_infos_6').addEventListener('click' , unshowIntertaleWeb);
    document.getElementById('last_alone_image').addEventListener('click' , showLastAlone);
    document.getElementById('close_infos_8').addEventListener('click' , unshowLastAlone);
    document.getElementById('pizza_image').addEventListener('click' , showPizza);
    document.getElementById('close_infos_7').addEventListener('click' , unshowPizza);
}

function showIntertaleInteractiveProject(){
    document.getElementById('intertale_about').style.display = "block";
    console.log("show");
}

function unshowIntertaleInteractiveProject(){
    document.getElementById('intertale_about').style.display = "none";
}

// function showKwixProject(){
//     document.getElementById('kwix_about').style.display = "block";
// }

// function unshowKwixProject(){
//     document.getElementById('kwix_about').style.display = "none";
// }

// function showNokaProject(){
//     document.getElementById('noka_about').style.display = "block";
// }

// function unshowNokaProject(){
//     document.getElementById('noka_about').style.display = "none";
// }

function showChessProject(){
    document.getElementById("chess_about").style.display = "block";
    console.log("show");
}

function unshowChessProject(){
    document.getElementById('chess_about').style.display = "none";
}

function showFightQuestProject(){
    document.getElementById('fight_quest_about').style.display = "block";
}

function unshowFightQuestProject(){
    document.getElementById('fight_quest_about').style.display = "none";
}

function showIntertaleWeb(){
    document.getElementById('intertale_web_about').style.display = "block";
}

function unshowIntertaleWeb(){
    document.getElementById('intertale_web_about').style.display = "none";
}

function showLastAlone(){
    document.getElementById('last_alone_about').style.display = "block";
}

function unshowLastAlone(){
    document.getElementById('last_alone_about').style.display = "none";
}

function showPizza(){
    console.log("show");
    document.getElementById('pizza_about').style.display = "block";
}

function unshowPizza(){
    document.getElementById('pizza_about').style.display = "none";
}