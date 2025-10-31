<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/futebol.css') }}">
    
    <title>{{ titulo_pagina or 'Nova Posição' }}</title>
</head>
<body>
    <header>
        <h1>Gerenciador de Elenco</h1>
    </header>
    <main>
        <h2>{{ titulo_h2 or 'Cadastrar Nova Posição' }}</h2>

        <form action="{{ url_destino }}" method="POST">
            
            <input type="hidden" name="id" value="{{ posicao.id or '' }}">

            <div class="form-grupo">
                <label for="nome">Nome da Posição:</label>
                <input type="text" id="nome" name="nome" value="{{ posicao.nome or '' }}" required placeholder="Ex: Atacante">
            </div>

            <div class="form-grupo">
                <label for="sigla">Sigla (3-4 letras):</label>
                <input type="text" id="sigla" name="sigla" value="{{ posicao.sigla or '' }}" required placeholder="Ex: ATA" maxlength="4">
            </div>

            <button type="submit" class="btn-salvar">Salvar Posição</button>
            
            <a href="{{ url_for('action_posicoes_index') }}" class="btn-deletar" style="text-decoration: none; margin-left: 10px;">Cancelar</a>
        </form>
    </main>

    <footer>
        <p>Copyright &copy; 2025 - Criado por Henrique Mendes</p>
    </footer>

    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
</body>
</html>