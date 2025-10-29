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
                <tr>
                    <td>Exemplo: Neymar</td>
                    <td>Atacante</td>
                    <td>10</td>
                    <td class="acoes">
                        <a href="/editar/1" class="btn-editar">Editar</a>
                        <a href="/deletar/1" class="btn-deletar">Deletar</a>
                    </td>
                </tr>
                 <tr>
                    <td>Exemplo: Vini Jr.</td>
                    <td>Atacante</td>
                    <td>7</td>
                    <td class="acoes">
                        <a href="/editar/2" class="btn-editar">Editar</a>
                        <a href="/deletar/2" class="btn-deletar">Deletar</a>
                    </td>
                </tr>
            </tbody>
        </table>
    </main>

    <script src="/static/js/script.js"></script>
</body>
</html>