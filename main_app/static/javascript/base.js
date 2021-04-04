// Search Autocomplete
function initialize() {
    const input = document.getElementById('searchTextField');
    const options = {
        types: ['(cities)'],
    }
    new google.maps.places.Autocomplete(input, options);
}
google.maps.event.addDomListener(window, 'load', initialize);

// Sidebar Nav
const sideNav = document.getElementById("side-nav-container");
const sidebarButton = document.getElementById("sidebar-button");
const content = document.querySelector("#content");
const menuItems = document.querySelector("#side-nav>ul");

function openSideNav() {
    sideNav.style.display = "flex";
    sideNav.style.minWidth = "250px";
    sideNav.style.maxWidth = "250px";
    menuItems.style.display = "block";
    content.style.marginLeft ="250px"
}

function closeSideNav() {
    sideNav.style.minWidth = "0px";
    sideNav.style.maxWidth = "0px";
    menuItems.style.display = "none";
    content.style.marginLeft ="0px";
}

sidebarButton.addEventListener("click", function (e) {
  if (sideNav.style.minWidth == "0px") {
    openSideNav();
  } else {
    closeSideNav();
  }
});

document.addEventListener("click", function(e) {
    const target = e.target
    if (target != sidebarButton) {
        closeSideNav();
    }
});
  