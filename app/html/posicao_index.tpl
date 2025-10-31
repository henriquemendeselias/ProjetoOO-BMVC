<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gerenciar Posições</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/futebol.css') }}">
</head>
<body>
    <header>
        <h1>Gerenciador de Elenco</h1>
    </header>
    <main>
        <h2>Gerenciar Posições</h2>
        
        <div class="container-btn-novo">
            <a href="{{ url_for('action_posicao_nova') }}" class="btn-novo">Adicionar Nova Posição</a>
        </div>

        <table>
            <thead>
                <tr>
                    <th>Nome da Posição</th>
                    <th>Sigla</th>
                    <th>Ações</th>
                </tr>
            </thead>
            <tbody>
                {% if not posicoes %}
                    <tr>
                        <td colspan="3" style="text-align: center;">Nenhuma posição cadastrada ainda.</td>
                    </tr>
                {% else %}
                    {% for p in posicoes %}
                        <tr>
                            <td>{{ p.get_nome() }}</td>
                            <td>{{ p.get_sigla() }}</td>
                            <td class="acoes">
                                <a href="{{ url_for('action_posicao_editar', posicao_id=p.get_id()) }}" class="btn-editar">Editar</a>
                                <a href="{{ url_for('action_posicao_deletar', posicao_id=p.get_id()) }}" class="btn-deletar">Deletar</a>
                            </td>
                        </tr>
                    {% endfor %}
                {% endif %}
            </tbody>
        </table>
        
        <div style="text-align: center; margin-top: 20px;">
            <a href="{{ url_for('action_index') }}" class="btn-editar" style="text-decoration: none;">Voltar ao Elenco Principal</a>
        </div>
    </main>

    <footer>
        <p>Copyright &copy; 2025 - Criado por Henrique Mendes</p>
    </footer>

    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
</body>
</html>