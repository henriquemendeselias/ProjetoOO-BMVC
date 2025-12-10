<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gerenciar Elencos</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/futebol.css') }}">
</head>
<body>
    <header>
        <h1>Gerenciador de Elenco</h1>

        <div style="position: absolute; top: 20px; right: 20px; font-size: 0.9em;">
            <span style="color: #fdb913;">Olá, {{ session['usuario_logado'] }}</span> | 
            <a href="{{ url_for('action_logout') }}" style="color: white; font-weight: bold;">Sair</a>
        </div>
    </header>
    <main>
        <h2>Gerenciar Elencos / Times</h2>
        
        <div class="controls-container">
        
            <div class="form-grupo">
                <label for="filtro-elencos">Filtrar Elencos por Nome:</label>
                <input type="text" id="filtro-elencos" placeholder="Digite um nome de elenco..." 
                       style="border: 2px solid #004d98;">
            </div>
            
            <div class="container-btn-novo">
                <a href="{{ url_for('action_time_novo') }}" class="btn-novo">Adicionar Novo Elenco</a>
            </div>
            
            <div class="container-btn-gerenciar">
                 <a href="{{ url_for('action_posicoes_index') }}" class="btn-editar" style="text-decoration: none;">Gerenciar Posições</a>
            </div>
            
        </div>
        <table>
            <thead>
                <tr>
                    <th>Nome do Elenco</th>
                    <th>Tipo</th>
                    <th>Ações</th>
                </tr>
            </thead>
            <tbody>
                {% if not times %}
                    <tr>
                        <td colspan="3" style="text-align: center;">Nenhum elenco cadastrado ainda.</td>
                    </tr>
                {% else %}
                    {% for t in times %}
                        <tr id="tr-time-{{ t.get_id() }}">
                            <td>
                                <a href="{{ url_for('action_elenco_detalhes', time_id=t.get_id()) }}" style="color: #004d98; font-weight: bold;">
                                    {{ t.get_nome() }}
                                </a>
                            </td>
                            <td>{{ t.get_tipo() }}</td>
                            <td class="acoes">
                                <a href="{{ url_for('action_time_editar', time_id=t.get_id()) }}" class="btn-editar">Config. Elenco</a>
                                <a href="{{ url_for('action_time_deletar', time_id=t.get_id()) }}" class="btn-deletar">Deletar</a>
                            </td>
                        </tr>
                    {% endfor %}
                {% endif %}
            </tbody>
        </table>
        
        </main>

    <footer>
        <p>Criado por Henrique Mendes</p>
    </footer>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js"></script>
    
    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
</body>
</html>