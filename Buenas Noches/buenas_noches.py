<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Buenas Noches</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #001f3f;
            color: white;
            font-family: 'Arial', sans-serif;
            overflow: hidden;
            background: linear-gradient(to bottom, #001f3f, #000);
        }
        .message {
            text-align: center;
            position: relative;
            z-index: 10;
        }
        .moon {
            position: absolute;
            top: 20%;
            left: 50%;
            width: 150px;
            height: 150px;
            background-color: #f1c40f;
            border-radius: 50%;
            box-shadow: 0 0 10px #f1c40f;
            transform: translateX(-50%);
        }
        .stars {
            position: absolute;
            width: 2px;
            height: 2px;
            background: white;
            border-radius: 50%;
            animation: twinkling 1.5s infinite alternate;
        }
        @keyframes twinkling {
            0% { opacity: 1.5; }
            100% { opacity: 1; }
        }
        .star-container {
            position: absolute;
            width: 100%;
            height: 100%;
            overflow: hidden;
        }
        .star-container div {
            position: absolute;
            width: 2px;
            height: 2px;
            background: white;
            border-radius: 50%;
            animation: twinkling 1.5s infinite alternate;
        }
        .star-container div:nth-child(even) { animation-duration: 2s; }
        .star-container div:nth-child(odd) { animation-duration: 1s; }
        .shooting-star {
            position: absolute;
            top: 20%;
            left: 50%;
            width: 3px;
            height: 100px;
            background: linear-gradient(white, rgba(255, 255, 255, 0));
            border-radius: 50%;
            transform: rotate(45deg);
            animation: shooting-star 3s infinite;
        }
        .shooting-star:nth-child(2) {
            animation-delay: 1s;
            left: 70%;
            animation-duration: 2s;
        }
        .shooting-star:nth-child(3) {
            animation-delay: 2s;
            left: 30%;
            animation-duration: 4s;
        }
        @keyframes shooting-star {
            0% { transform: translateY(100vh) translateX(-200vh) rotate(72deg); opacity: 1; }
            100% { transform: translateY(0) translateX(100vh) rotate(72deg); opacity: 0; }
        }
    </style>
</head>
<body>
    <div class="moon"></div>
    <div class="message">
        <h1>Buenas Noches</h1>
        <p>Si ves una estrella fugaz, pide un deseo. 🌠 <br>
            Yo ya pedí uno: que no ronques ❤️ </p>
    </div>
    <div class="star-container">
        <div style="transform: translate(50vw, -40vh) scale(1.5);"></div>
        <div style="transform: translate(60vw, -30vh) scale(1.8);"></div>
        <div style="transform: translate(70vw, -20vh) scale(1.7);"></div>
        <div style="transform: translate(80vw, -10vh) scale(1.9);"></div>
        <div style="transform: translate(90vw, 0vh) scale(1.6);"></div>
        <div style="transform: translate(40vw, -20vh) scale(1.4);"></div>
        <div style="transform: translate(30vw, -10vh) scale(1.3);"></div>
        <div style="transform: translate(20vw, 0vh) scale(1.7);"></div>
        <div style="transform: translate(10vw, 10vh) scale(1.5);"></div>
        <div style="transform: translate(50vw, 80vh) scale(1.8);"></div>
        <div style="transform: translate(35vw, 60vh) scale(1.9);"></div>
        <div style="transform: translate(70vw, 40vh) scale(1.6);"></div>
        <div style="transform: translate(80vw, 50vh) scale(1.4);"></div>
        <div style="transform: translate(90vw, 60vh) scale(1.7);"></div>
        <div style="transform: translate(30vw, 70vh) scale(1.5);"></div>
    </div>
    <div class="shooting-star"></div>
    <div class="shooting-star"></div>
    <div class="shooting-star"></div>
</body>
</html>