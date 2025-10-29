<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página de Boas-Vindas</title>
    <link rel="stylesheet" type="text/css" href="/static/css/pagina.css">

</head>
<body>
    <div class="container">
        <header class="header">
            <h1 id="welcome-title">Bem-vindo!</h1>
        </header>

        <main class="main-content">
            <div class="welcome-card">
                <p id="welcome-message">É um prazer ter você aqui!</p>
                <div class="time-display">
                    <span id="current-time">Carregando...</span>
                </div>
                <div class="counter-section">
                    <p>Você está aqui há: <span id="visit-counter">0</span> segundos</p>
                </div>
                <button id="theme-toggle" class="theme-btn">🌙 Modo Escuro</button>
                <button id="change-color" class="color-btn">🎨 Mudar Cor</button>
            </div>
        </main>

        <footer class="footer">
            <p id="footer-text">Tenha um excelente dia!</p>
        </footer>
    </div>

    <script src="/static/js/pagina.js"></script>
</body>
</html>
