document.addEventListener("DOMContentLoaded", main);

function main(){
    document.getElementById('fight_quest_image').addEventListener('mouseover' , showFightQuest);
}

function showFightQuest(){
    document.getElementById('fight_quest_text').style.display = "block";
    setTimeout(unshowFightQuest, 3000);
}

function unshowFightQuest(){
    document.getElementById('fight_quest_text').style.display = "none";
}