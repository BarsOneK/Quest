const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

const ground = new Image();
ground.src = "../../static/img/game_field.png";         //bug      підключення картинок

const foodImg = new Image();
foodImg.src = "../../static/img/food.png";          //bug      підключення картинок

let box = 40;
let score = 0;

let food = {
  x: Math.floor((Math.random() * 10)) * box,
  y: Math.floor((Math.random() * 10)) * box,
};

let snake = [];
snake[0] = {
  x: 4 * box,
  y: 4 * box,
};

document.addEventListener("keydown", direction);

let dir;

function direction(event) {
  if (event.keyCode == 37 && dir != "right")
    dir = "left";
  else if(event.keyCode == 38 && dir != "down")
    dir = "up";
  else if(event.keyCode == 39 && dir != "left")
    dir = "right";
  else if (event.keyCode == 40 && dir != "up")
    dir = "down";
}

function eatTail(head, arr) {
  for (let i = 0; i < arr.length; i++) {
    if (head.x == arr[i].x && head.y == arr[i].y)
      clearInterval(game);
  }
}

function drawGame() {
  ctx.drawImage(ground, 0, 0);
  ctx.drawImage(foodImg, food.x, food.y+100);

  for (let i = 0; i < snake.length; i++) {
    ctx.fillStyle = i == 0 ? "rgb(66, 141, 238)" : "rgb(111, 166, 237)";
    ctx.fillRect(snake[i].x, snake[i].y+100, box, box);
  }

  ctx.fillStyle = "black";
  ctx.font = "20pt 'Press Start 2P'";
  ctx.fillText(score, box * 2, box * 1.68);

  let snakeX = snake[0].x;
  let snakeY = snake[0].y;

  if (snakeX == food.x && snakeY == food.y) {
    score++;
    food = {
      x: Math.floor((Math.random() * 10)) * box,
      y: Math.floor((Math.random() * 10)) * box,
    };
    if (score == 5) {
      location.href = "../info_1";
    }
  } else {
    snake.pop();
  }


  if (snakeX < 0 || snakeX > box * 9 || snakeY < 0 || snakeY > box * 9)
    clearInterval(game);

  if (dir == "left") snakeX -=box;
  if (dir == "right") snakeX +=box;
  if (dir == "up") snakeY -=box;
  if (dir == "down") snakeY +=box;

  let newHead = {
    x: snakeX,
    y: snakeY
  };

  eatTail(newHead, snake)

  snake.unshift(newHead);
}

let game = setInterval(drawGame, 100);
