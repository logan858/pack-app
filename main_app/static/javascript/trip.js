const scores = document.querySelectorAll(".score");
const scoreUp = document.querySelectorAll(".score-up");
const scoreDown = document.querySelectorAll(".score-down");
const scoreValue = document.querySelectorAll(".score-value");

scores.forEach(item => {
    item.addEventListener("click", (e) => {
        let target = e.target
        if (target.classList.contains("path")) {
            target = target.parentElement;
        }
        const parent = target.parentElement;
        const up = parent.children[0];
        const down = parent.children[2];
        const score = parent.children[1];
        const classNames = {
            up : "score-up-post",
            down : "score-down-post"
        }
        const name = score.getAttribute("name");
        console.log(score)
        if (target.classList.contains("score-up")) {
            if (up.classList.contains(classNames.up)) {
                up.classList.remove(classNames.up)
                score.innerHTML = parseInt(score.innerHTML) - 1
                changeScore(name, -1)
            } else {
                up.classList.add(classNames.up);
                if (down.classList.contains(classNames.down)) {
                    down.classList.remove(classNames.down)
                    score.innerHTML = parseInt(score.innerHTML) + 2
                    changeScore(name, 2)
                } else {
                    score.innerHTML = parseInt(score.innerHTML) + 1
                    changeScore(name, 1)
                }
            }
        } else if (target.classList.contains("score-down")) {
            if (down.classList.contains(classNames.down)) {
                down.classList.remove(classNames.down)
                score.innerHTML = parseInt(score.innerHTML) + 1
                changeScore(name, 1)
            } else {
                down.classList.add(classNames.down);
                if (up.classList.contains(classNames.up)) {
                    up.classList.remove(classNames.up)
                    score.innerHTML = parseInt(score.innerHTML) - 2
                    changeScore(name, -2)
                } else {
                    score.innerHTML = parseInt(score.innerHTML) - 1
                    changeScore(name, -1)
                }
            }
        }
        return
    })
})

function changeScore(id, num) {
    const trip_id = document.querySelector("#trip_id").value;
    const url = "/api/vote"
    console.log(num)
    const json_upload = JSON.stringify({
        "trip_id" : trip_id,
        "item_id" : id,
        "change_value" : num.toString()
    });
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    const http = new XMLHttpRequest();
    http.open("POST", url, true);
    http.setRequestHeader('X-CSRFToken', csrftoken);
    http.send(json_upload);
}

const activityCards = document.querySelectorAll(".card-activity");
activityCards.forEach(item => {
    item.addEventListener("click", e => {
        let target = e.target
        let rightTarget = false;
        while (!rightTarget) {
            if (target.classList.contains("card-activity")) {
                rightTarget = true
            } else {
                target = target.parentElement
            }
        }
        target.classList.add("card-activity-active");
        target.children[0].checked = true;

        const parent = target.parentElement;
        const grandparent = parent.parentElement
        for (let i = 0; i < grandparent.children.length; i++) {
            const uncle = grandparent.children[i]
            if (uncle != parent && uncle.children[0].classList.contains("card-activity-active")) {
                uncle.children[0].classList.remove("card-activity-active")
                uncle.children[0].children[0].checked = false
            }
        }
    })
})