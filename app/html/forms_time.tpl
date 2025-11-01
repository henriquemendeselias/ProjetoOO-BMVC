<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/futebol.css') }}">
    
    <title>{{ titulo_pagina or 'Novo Elenco' }}</title>
</head>
<body>
    <header>
        <h1>Gerenciador de Elenco</h1>
    </header>
    <main>
        <h2>{{ titulo_h2 or 'Cadastrar Novo Elenco' }}</h2>

        <form action="{{ url_destino }}" method="POST">
            
            <input type="hidden" name="id" value="{{ time.id or '' }}">

            <div class="form-grupo">
                <label for="nome">Nome do Elenco:</label>
                <input type="text" id="nome" name="nome" value="{{ time.nome or '' }}" required placeholder="Ex: Time Principal">
            </div>

            <div class="form-grupo">
                <label for="tipo">Tipo de Elenco:</label>
                <select id="tipo" name="tipo" required>
                    <option value="">Selecione o tipo...</option>
                    
                    <option value="Elenco Fixo" 
                            {% if (time.tipo or '') == 'Elenco Fixo' %}selected{% endif %}>
                        Elenco Fixo (Ex: Principal, Sub-20)
                    </option>
                    
                    <option value="Observação" 
                            {% if (time.tipo or '') == 'Observação' %}selected{% endif %}>
                        Observação (Lista de Compras)
                    </option>
                </select>
            </div>

            <button type="submit" class="btn-salvar">Salvar Elenco</button>
            
            <a href="{{ url_for('action_times_index') }}" class="btn-deletar" style="text-decoration: none; margin-left: 10px;">Cancelar</a>
        </form>
    </main>

    <footer>
        <p>Criado por Henrique Mendes</p>
    </footer>

    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
</body>
</html>