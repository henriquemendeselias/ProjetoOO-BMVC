<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <link rel="stylesheet" href="{{ url_for('static', filename='css/futebol.css') }}">
    
    <title>{{ titulo_pagina or 'Novo Jogador' }}</title>
</head>
<body>

    <header>
        <h1>Gerenciador de Elenco de Futebol</h1>
    </header>

    <main>
        <h2>{{ titulo_h2 or 'Cadastrar Novo Jogador' }}</h2>

        <form action="{{ url_destino }}" method="POST">
            
            <input type="hidden" name="id" value="{{ jogador.id or '' }}">

            <div class="form-grupo">
                <label for="nome">Nome do Jogador:</label>
                <input type="text" id="nome" name="nome" value="{{ jogador.nome or '' }}" required placeholder="Ex: Vinícius Júnior">
            </div>

            <div class="form-grupo">
                <label for="posicao">Posição:</label>
                <select id="posicao" name="posicao" required>
                    <option value="">Selecione a posição...</option>
                    <option value="Goleiro" {% if (jogador.posicao or '') == 'Goleiro' %}selected{% endif %}>Goleiro (GK)</option>
                    <option value="Defensor" {% if (jogador.posicao or '') == 'Defensor' %}selected{% endif %}>Defensor (ZAG, LD, LE)</option>
                    <option value="Meio-Campo" {% if (jogador.posicao or '') == 'Meio-Campo' %}selected{% endif %}>Meio-Campo (VOL, MC, MEI)</option>
                    <option value="Atacante" {% if (jogador.posicao or '') == 'Atacante' %}selected{% endif %}>Atacante (SA, PD, PE, ATA)</option>
                </select>
            </div>

            <div class="form-grupo">
                <label for="numero_camisa">Número da Camisa:</label>
                <input type="number" id="numero_camisa" name="numero_camisa" value="{{ jogador.numero_camisa or '' }}" min="1" max="99" required placeholder="Ex: 7">
            </div>

            <button type="submit" class="btn-salvar">Salvar Jogador</button>
            
            <a href="{{ url_for('action_index') }}" class="btn-deletar" style="text-decoration: none; margin-left: 10px;">Cancelar</a>
        </form>

    </main>

    <footer>
        <p>Criado por Henrique Mendes</p>
    </footer>

    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
</body>
</html>