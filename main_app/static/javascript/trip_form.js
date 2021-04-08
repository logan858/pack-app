// Search Autocomplete
function initialize() {
    const input = document.getElementById('searchTextField');
    const options = {
        types: ['(cities)'],
    }
    new google.maps.places.Autocomplete(input, options);
}
google.maps.event.addDomListener(window, 'load', initialize);

const addTravellerButton = document.querySelector("#add-traveller-button")
const travellersList = document.querySelector("#travellers-list")
let travellerTemplate = document.querySelector("#traveller-template");
let removeTravellerButtons = document.querySelectorAll(".remove-traveller-button")

addTravellerButton.addEventListener("click", e => {
    const clone = travellerTemplate.cloneNode(true);
    clone.removeAttribute("id");
    clone.querySelectorAll("input").forEach(input => {
        input.value="";
    })
    travellersList.appendChild(clone)
    removeButtons();
})

document.querySelector(".remove-traveller-button").addEventListener("click", e => {
    e.preventDefault();
    removeTravellerButtons = document.querySelectorAll(".remove-traveller-button");
    removeButtons()
})

function removeButtons() {
    removeTravellerButtons.forEach(removeTravellerButton => {
        removeTravellerButton.addEventListener("click", e => {
            e.preventDefault();
            const target = e.target
            if (target == removeTravellerButton) {
                let removed = false
                let parent = target.parentElement
                while (removed == false) {
                    if (parent.nodeName == "LI" ) {
                        parent.remove();
                        removed = true
                    } else {
                        parent = parent.parentElement
                    }
                }
            }
        })
    })
}

const packingCards = document.querySelectorAll(".card-packing");
packingCards.forEach(item => {
    item.addEventListener("click", e => {
        let target = e.target
        let rightTarget = false;
        while (!rightTarget) {
            if (target.classList.contains("card-packing")) {
                rightTarget = true
            } else {
                target = target.parentElement
            }
        }
        target.classList.add("card-packing-active");
        target.children[0].checked = true;

        const parent = target.parentElement;
        const grandparent = parent.parentElement
        for (let i = 0; i < grandparent.children.length; i++) {
            const uncle = grandparent.children[i]
            if (uncle != parent && uncle.children[0].classList.contains("card-packing-active")) {
                uncle.children[0].classList.remove("card-packing-active")
                uncle.children[0].children[0].checked = false
            }
        }
    })
})

const activityCards = document.querySelectorAll(".card-activity");
activityCards.forEach(item => {
    item.addEventListener("click", e => {
        e.preventDefault();
        let target = e.target
        let rightTarget = false;
        while (!rightTarget) {
            if (target.classList.contains("card-activity")) {
                rightTarget = true
            } else {
                target = target.parentElement
            }
        }

        if (target.classList.contains("card-activity-active") == false) {
            target.classList.add("card-activity-active");
            target.children[0].checked = true;
        } else {
            target.classList.remove("card-activity-active")
            target.children[0].checked = false;
        }
    })
})
