function openLeft() {
    document.getElementsByTagName("body")[0].style.backgroundImage = "linear-gradient(var(--rine-dark-blue), var(--rine-dark-magenta))";
    document.getElementById("leftSidebar").style.display = "block";
    document.getElementById("postsContainer").style.display = "none";
    document.getElementById("leftSidebarButtonClose").style.display = "block";
    document.getElementById("leftSidebarButtonOpen").style.display = "none";
    document.getElementById("rightSidebarButtonOpen").style.display = "none";
}

function closeLeft() {
    document.getElementsByTagName("body")[0].style.backgroundImage = "none";
    document.getElementById("leftSidebar").style.display = "none";
    document.getElementById("postsContainer").style.display = "block";
    document.getElementById("leftSidebarButtonOpen").style.display = "block";
    document.getElementById("leftSidebarButtonClose").style.display = "none";
    document.getElementById("rightSidebarButtonOpen").style.display = "block";
}

function openRight() {
    document.getElementsByTagName("body")[0].style.backgroundImage = "linear-gradient(var(--rine-dark-blue), var(--rine-dark-magenta))";
    document.getElementById("rightSidebar").style.display = "block";
    document.getElementById("postsContainer").style.display = "none";
    document.getElementById("rightSidebarButtonClose").style.display = "block";
    document.getElementById("rightSidebarButtonOpen").style.display = "none";
    document.getElementById("leftSidebarButtonOpen").style.display = "none";
}

function closeRight() {
    document.getElementsByTagName("body")[0].style.backgroundImage = "none";
    document.getElementById("rightSidebar").style.display = "none";
    document.getElementById("postsContainer").style.display = "block";
    document.getElementById("rightSidebarButtonOpen").style.display = "block";
    document.getElementById("rightSidebarButtonClose").style.display = "none";
    document.getElementById("leftSidebarButtonOpen").style.display = "block";
}
