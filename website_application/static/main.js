function addBackgroundImage() {
    document.getElementsByTagName("body")[0].style.backgroundImage = "linear-gradient(var(--rine-dark-blue), var(--rine-dark-magenta))";
    document.getElementsByTagName("body")[0].style.backgroundAttachment = "fixed";
}

function removeBackgroundImage() {
    document.getElementsByTagName("body")[0].style.backgroundImage = "none";
}

function showLeftSidebar() {
    document.getElementById("leftSidebar").style.display = "block";
    document.getElementById("postsContainer").style.display = "none";
}

function showRightSidebar() {
    document.getElementById("rightSidebar").style.display = "block";
    document.getElementById("postsContainer").style.display = "none";
}

function hideLeftSidebar() {
    document.getElementById("leftSidebar").style.display = "none";
    document.getElementById("postsContainer").style.display = "block";
}

function hideRightSidebar() {
    document.getElementById("rightSidebar").style.display = "none";
    document.getElementById("postsContainer").style.display = "block";
}

function showSidebarOpenButtons() {
    document.getElementById("leftSidebarButtonOpen").style.display = "block";
    document.getElementById("rightSidebarButtonOpen").style.display = "block";
}

function hideSidebarOpenButtons() {
    document.getElementById("leftSidebarButtonOpen").style.display = "none";
    document.getElementById("rightSidebarButtonOpen").style.display = "none";
}

function openLeft() {
    addBackgroundImage()
    showLeftSidebar()
    hideSidebarOpenButtons()
    document.getElementById("leftSidebarButtonClose").style.display = "block";
}

function closeLeft() {
    removeBackgroundImage()
    hideLeftSidebar()
    showSidebarOpenButtons()
    document.getElementById("leftSidebarButtonClose").style.display = "none";
}

function openRight() {
    addBackgroundImage()
    showRightSidebar()
    hideSidebarOpenButtons()
    document.getElementById("rightSidebarButtonClose").style.display = "block";
}

function closeRight() {
    removeBackgroundImage()
    hideRightSidebar()
    showSidebarOpenButtons()
    document.getElementById("rightSidebarButtonClose").style.display = "none";
}
