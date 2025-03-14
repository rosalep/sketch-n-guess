
document.addEventListener('DOMContentLoaded', () => { // ensures HTML is loaded before js used
    // begin canvas section
    const c = document.getElementById("active-canvas");
    const ctx = c.getContext("2d");
    
    ctx.lineCap = "round";
    
    let coordX = 0;
    let coordY = 0;
    let active = false;
    let eraser = false;
    // let fill = false;
    var savedTime = sessionStorage.getItem("timeLeft");
    if (savedTime) {
        timeLeft = parseInt(savedTime);
    }
    
    document.getElementById("increase-pencil-canvas").onclick = increaseWidth;
    document.getElementById("decrease-pencil-canvas").onclick = decreaseWidth;
    document.getElementById("color-canvas").onchange = colorPicker;
    document.getElementById("clear-canvas").onclick= clearCanvas;
    document.getElementById("eraser-canvas").onclick= changeEraser;
    document.getElementById("pencil-canvas").onclick= changeEraser;

    function clearCanvas() {
        ctx.clearRect(0, 0, c.width, c.height);
    }
    function changeEraser() {
        eraser = (eraser) ? eraser = false : eraser=true;
    }
    function increaseWidth() {
        ctx.lineWidth += 1;
    }
    function decreaseWidth() {
        ctx.lineWidth -= 1;
    }
    function colorPicker() {
        ctx.strokeStyle = document.getElementById("color-canvas").value;;
    }
    function getMousePosition(c, event) {
        const rect = c.getBoundingClientRect();
        const x = event.clientX - rect.left;
        const y = event.clientY - rect.top;
        return [x, y];
    }

    c.addEventListener("click", function (e) {
        const coords = getMousePosition(c, e);
        ctx.beginPath();
        if (eraser) {
            ctx.clearRect(coords[0] + 1, coords[1] + 1, ctx.lineWidth, ctx.lineWidth);
        }
        else {
            ctx.moveTo(coords[0], coords[1]);
            ctx.lineTo(coords[0] + 1, coords[1] + 1);
            ctx.fill();
            ctx.stroke();
        }
    });
    c.addEventListener("mousedown", function (e) {

        active = true;
        const coords = getMousePosition(c, e);
        coordX = coords[0];
        coordY = coords[1];

    });

    c.addEventListener("mouseup", function (e) {
        active = false;
    });

    c.addEventListener("mouseout", function (e) {
        active = false;
    });


    c.addEventListener("mousemove", function (e) {

        if (active) {
            const coords = getMousePosition(c, e);
            ctx.beginPath();
            if (eraser) {
                ctx.moveTo(coordX, coordY);
                ctx.clearRect(coords[0], coords[1], ctx.lineWidth, ctx.lineWidth);
                ctx.stroke();
                coordX = coords[0];
                coordY = coords[1];
            }
            else {
                ctx.moveTo(coordX, coordY);
                ctx.lineTo(coords[0], coords[1]);
                ctx.stroke();
                coordX = coords[0];
                coordY = coords[1];
            }
        }

    });
    // end canvas section

    // begin timer section
    var timeLeft = 180; // 180 = 3 minutes
    var activeTimer = setInterval(countdown, 1000); // gets called every second
    var savedTime = sessionStorage.getItem("timeLeft");
    if (savedTime) {
        timeLeft = parseInt(savedTime);
    }
    function countdown() {
        sessionStorage.getItem(timeLeft);
        if (timeLeft == -1) {
            // takes away control of canvas
            c.style.pointerEvents = "none";
            document.getElementById("tools-canvas-container").style.pointerEvents = "none";
            document.getElementById("game-timer").innerHTML = 'TIMES UP';
            clearTimeout(activeTimer);
            sessionStorage.removeItem('timeLeft');
        }
    
        else {
            document.getElementById("game-timer").innerHTML = 'Remaining Time: ' + Math.floor(timeLeft / 60) + ' minutes ' + (timeLeft % 60) + ' seconds';
            timeLeft--;
            sessionStorage.setItem("timeLeft", timeLeft);

        }
    }
    // end timer section


    // begin chat section
    // end chat section
});
// const chatSocket = new WebSocket("ws://" + window.location.host + "/");


//     chatSocket.onopen = function (e) {
//       console.log("The connection was setup successfully !");
//     };
//     chatSocket.onclose = function (e) {
//       console.log("Something unexpected happened !");
//     };
//     document.querySelector("#id_guess_send_input").focus();
//     document.querySelector("#id_guess_send_input").onkeyup = function (e) {
//       if (e.keyCode == 13) {
//         document.querySelector("#id_guess_send_button").click();
//       }
//     };
//     document.querySelector("#id_guess_send_button").onclick = function (e) {
//       var guessInput = document.querySelector(
//         "#id_guess_send_input"
//       ).value;
//       chatSocket.send(JSON.stringify({ guess: guessInput, username : "{{request.user.username}}"}));
//     };
//     chatSocket.onmessage = function (e) {
//       const data = JSON.parse(e.data);
//     //   var div = document.createElement("div");
//     //   div.innerHTML = data.username + " : " + data.guess;
//     document.querySelector('#guess_history').value += (data.guessInput + '\n');
//       document.querySelector("#id_guess_send_input").value = "";
//     //   document.querySelector("#id_chat_item_container").appendChild(div);
//     };