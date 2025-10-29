<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gerenciador de Elenco</title>
    <link rel="stylesheet" href="/static/css/futebol.css">
</head>
<body>

    <header>
        <h1>Gerenciador de Elenco de Futebol</h1>
    </header>

    <main>
        <h2>Elenco Principal</h2>
        
        <a href="/formulario" class="btn-novo">Adicionar Novo Jogador</a>

        <table>
            <thead>
                <tr>
                    <th>Nome</th>
                    <th>Posição</th>
                    <th>Número da Camisa</th>
                    <th>Ações</th>
                </tr>
            </thead>
            <tbody>
                %if not jogadores:
                    <tr>
                        <td colspan="4" style="text-align: center;">Nenhum jogador cadastrado ainda.</td>
                    </tr>
                %else:
                    %for j in jogadores:
                        <tr>
                            <td>{{j.get_nome()}}</td>
                            <td>{{j.get_posicao()}}</td>
                            <td>{{j.get_numero_camisa()}}</td>
                            <td class="acoes">
                                <a href="/editar/{{j.get_id()}}" class="btn-editar">Editar</a>
                                
                                <a href="/deletar/{{j.get_id()}}" class="btn-deletar">Deletar</a>
                            </td>
                        </tr>
                    %end
                %end
                </tbody>>
        </table>
    </main>

    <script src="/static/js/script.js"></script>
</body>
</html>