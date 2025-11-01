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
    </header>
    <main>
        <h2>Gerenciar Elencos / Times</h2>
        
        <div class="container-btn-novo">
            <a href="{{ url_for('action_time_novo') }}" class="btn-novo">Adicionar Novo Elenco</a>
        </div>

        <div class="form-grupo" style="width: 50%; margin: 20px auto;">
            <label for="filtro-elencos">Filtrar Elencos por Nome:</label>
            <input type="text" id="filtro-elencos" placeholder="Digite um nome de elenco para filtrar..." 
                   style="border: 2px solid #004d98;">
        </div>

        <table>
            <thead>
                <tr>
                    <th>Nome do Elenco</th> <th>Tipo</th>
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
                        <tr>
                            <td>
                                <a href="{{ url_for('action_elenco_detalhes', time_id=t.get_id()) }}" style="text-decoration: none; color: #004d98; font-weight: bold;">
                                    {{ t.get_nome() }}
                                </a>
                            </td>
                            
                            <td>{{ t.get_tipo() }}</td>
                            <td class="acoes">
                                <a href="{{ url_for('action_time_editar', time_id=t.get_id()) }}" class="btn-editar">Renomear Elenco</a>
                                <a href="{{ url_for('action_time_deletar', time_id=t.get_id()) }}" class="btn-deletar">Deletar</a>
                            </td>
                        </tr>
                    {% endfor %}
                {% endif %}
            </tbody>
        </table>
        
        <div style="text-align: center; margin-top: 20px;">
             <a href="{{ url_for('action_posicoes_index') }}" class="btn-editar" style="text-decoration: none;">Gerenciar Posições</a>
        </div>
    </main>

    <footer>
        <p>Copyright &copy; 2025 - Criado por Henrique Mendes</p>
    </footer>

    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
</body>
</html>