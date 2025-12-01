<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro - Gerenciador de Elenco</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/futebol.css') }}">
    <style>
        /* (Mesmo estilo centralizado do login) */
        body { display: flex; flex-direction: column; min-height: 100vh; }
        main { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; }
        form { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); width: 100%; max-width: 400px; }
    </style>
</head>
<body>
    <header>
        <h1>Acesso Restrito</h1>
    </header>

    <main>
        <h2>Criar Nova Conta</h2>

        <form action="{{ url_for('action_processar_cadastro') }}" method="POST">
            
            <div class="form-grupo">
                <label for="nome">Escolha um Usuário:</label>
                <input type="text" id="nome" name="nome" required placeholder="Novo usuário">
            </div>

            <div class="form-grupo">
                <label for="senha">Escolha uma Senha:</label>
                <input type="password" id="senha" name="senha" required placeholder="Nova senha">
            </div>

            <button type="submit" class="btn-salvar" style="width: 100%; background-color: #28a745;">Cadastrar</button>
            
            <div style="text-align: center; margin-top: 15px;">
                <span>Já tem acesso?</span>
                <br>
                <a href="{{ url_for('action_login') }}" style="color: #004d98; font-weight: bold; text-decoration: none;">Fazer Login</a>
            </div>
        </form>
    </main>

    <footer>
        <p>Copyright &copy; 2025 - Criado por Henrique Mendes</p>
    </footer>
</body>
</html>