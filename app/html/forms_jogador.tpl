<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <link rel="stylesheet" href="/static/css/futebol.css">
    
    <title>{{ get('titulo_pagina', 'Novo Jogador') }}</title>
</head>
<body>

    <header>
        <h1>Gerenciador de Elenco de Futebol</h1>
    </header>

    <main>
        <h2>{{ get('titulo_h2', 'Cadastrar Novo Jogador') }}</h2>

        <form action="{{ url_destino }}" method="POST">
            
            <input type="hidden" name="id" value="{{ get('id', '') }}">

            <div class="form-grupo">
                <label for="nome">Nome do Jogador:</label>
                <input type="text" id="nome" name="nome" value="{{ get('nome', '') }}" required placeholder="Ex: Vinícius Júnior">
            </div>

            <div class="form-grupo">
                <label for="posicao">Posição:</label>
                <select id="posicao" name="posicao" required>
                    <option value="">Selecione a posição...</option>
                    <option value="Goleiro" {{ 'selected' if get('posicao') == 'Goleiro' else '' }}>Goleiro (GK)</option>
                    <option value="Defensor" {{ 'selected' if get('posicao') == 'Defensor' else '' }}>Defensor (ZAG, LD, LE)</option>
                    <option value="Meio-Campo" {{ 'selected' if get('posicao') == 'Meio-Campo' else '' }}>Meio-Campo (VOL, MC, MEI)</option>
                    <option value="Atacante" {{ 'selected' if get('posicao') == 'Atacante' else '' }}>Atacante (SA, PD, PE, ATA)</option>
                </select>
            </div>

            <div class="form-grupo">
                <label for="numero_camisa">Número da Camisa:</label>
                <input type="number" id="numero_camisa" name="numero_camisa" value="{{ get('numero_camisa', '') }}" min="1" max="99" required placeholder="Ex: 7">
            </div>

            <button type="submit" class="btn-salvar">Salvar Jogador</button>
            
            <a href="/" class="btn-deletar" style="text-decoration: none; margin-left: 10px;">Cancelar</a>
        </form>

    </main>

    <script src="/static/js/main.js"></script>
</body>
</html>