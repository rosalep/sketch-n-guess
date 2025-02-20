
document.addEventListener('DOMContentLoaded', () => { // ensures HTML is loaded before js used
    const c = document.getElementById("active-canvas");
    const ctx = c.getContext("2d");
    
    ctx.lineCap = "round";
    
    let coordX = 0;
    let coordY = 0;
    let active = false;
    let eraser = false;
    // let fill = false;
    
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

    var timeLeft = 180; // 180 = 3 minutes
    var activeTimer = setInterval(countdown, 1000); // gets called every second

    function countdown() {
        if (timeLeft == -1) {
            c.style.pointerEvents = "none";
            document.getElementById("tools-canvas-container").style.pointerEvents = "none";
            document.getElementById("game-timer").innerHTML = 'TIMES UP';
            clearTimeout(activeTimer);
        }

        else {
            document.getElementById("game-timer").innerHTML = 'Remaining Time: ' + Math.floor(timeLeft / 60) + ' minutes ' + (timeLeft % 60) + ' seconds';
            timeLeft--;
        }
    }
});