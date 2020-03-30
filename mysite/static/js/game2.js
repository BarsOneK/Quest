const canvas = document.getElementById("game2");
const ctx = canvas.getContext("2d");

const ground = new Image();
ground.src = "../../static/img/smile.png";

let score = 0;


function direction() {
    let elem = document.getElementById('mainline');
    score++;
    elem.style.width = score + '%';
}


function drawGame() {
  ctx.drawImage(ground, 0, 0);

  ctx.fillStyle = "black";
  ctx.font = "30px 'Press Start 2P'";

  if (score <= 9) {
    ctx.fillText(score, 185, 90);
  }
  if (score >= 10) {
    ctx.fillText(score, 170, 90);
  }
  if (score == 100) {
    location.href = '../info_2';
  }
}

let game = setInterval(drawGame, 100);
