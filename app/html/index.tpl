<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <link rel="stylesheet" href="{{ url_for('static', filename='css/futebol.css') }}">
    
    <title>Gerenciador de Elenco</title>
</head>
<body>
    <header>
        <h1>Gerenciador de Elenco de Futebol</h1>

        <div style="position: absolute; top: 20px; right: 20px; font-size: 0.9em;">
            <span style="color: #fdb913;">Olá, {{ session['usuario_logado'] }}</span> | 
            <a href="{{ url_for('action_logout') }}" style="color: white; font-weight: bold;">Sair</a>
        </div>
    </header>
    <main>
        <h2>Elenco: {{ time.get_nome() }}</h2>
        <h3 style="text-align: center; margin-top: -15px; color: #555;">(Tipo: {{ time.get_tipo() }})</h3>
        
        <div class="controls-container">
        
            <div class="form-grupo" style="min-width: 300px;">
                <label for="filtro-jogadores">Filtrar Elenco por Nome:</label>
                <input type="text" id="filtro-jogadores" placeholder="Digite um nome para filtrar..." 
                       style="border: 2px solid #004d98;">
            </div>
            
            <div class="container-btn-novo">
                <a href="{{ url_for('action_formulario_novo', time_id=time.get_id()) }}" class="btn-novo">
                    Adicionar Jogador
                </a>
            </div>
            
            <div class="container-btn-gerenciar">
                 <a href="{{ url_for('action_posicoes_index') }}" class="btn-editar" style="text-decoration: none;">Gerenciar Posições</a>
            </div>
            
        </div>
        <table>
            <thead>
                <tr>
                    <th>Nome</th>
                    <th>Posição</th>
                    <th>Camisa</th>
                    <th>Idade</th>
                    <th>Nacionalidade</th>
                    <th>Ações</th>
                </tr>
            </thead>
            <tbody>
                {% if not jogadores %}
                    <tr>
                        <td colspan="6" style="text-align: center;">Nenhum jogador cadastrado neste elenco.</td>
                    </tr>
                {% else %}
                    {% for j in jogadores %}
                        <tr id="tr-jogador-{{j.get_id()}}">
                            <td>{{ j.get_nome() }}</td>
                            <td>{{ posicoes_map.get(j.get_posicao_id(), 'N/A') }}</td>
                            <td>{{ j.get_numero_camisa() }}</td>
                            <td>{{ j.get_idade() }}</td>
                            <td>{{ j.get_nacionalidade() }}</td>
                            <td class="acoes">
                                <a href="{{ url_for('action_formulario_editar', jogador_id=j.get_id()) }}" class="btn-editar">Editar</a>
                                <a href="{{ url_for('action_deletar', jogador_id=j.get_id()) }}" class="btn-deletar">Deletar</a>
                            </td>
                        </tr>
                    {% endfor %}
                {% endif %}
            </tbody>
        </table>

        <div style="text-align: center; margin-top: 20px;">
            <a href="{{ url_for('action_times_index') }}" class="btn-editar" style="text-decoration: none;">Voltar para Lista de Elencos</a>
        </div>
    </main>
    
    <footer>
        <p>Criado por Henrique Mendes</p>
    </footer>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js"></script>
    
    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
</body>
</html>