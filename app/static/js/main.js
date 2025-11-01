document.addEventListener('DOMContentLoaded', function() {
    const botoesDeletar = document.querySelectorAll('.btn-deletar');
    
    botoesDeletar.forEach(function(botao) {
        
        botao.addEventListener('click', function(event) {
            
            const linhaTabela = event.target.closest('tr');

            if (linhaTabela) { 
                 let nomeItem = 'este item';
                 try {
                     nomeItem = linhaTabela.querySelector('td a, td').textContent.trim();
                 } catch (e) {}
                 
                 const confirmou = confirm(`Tem certeza que deseja deletar "${nomeItem}"?`);
                 
                 if (!confirmou) {
                     event.preventDefault(); 
                 }
            }
        });
    });
    const filtroInputJogadores = document.getElementById('filtro-jogadores');
    if (filtroInputJogadores) {
        const tabelaCorpoJogadores = filtroInputJogadores.closest('main').querySelector('table tbody');
        
        filtroInputJogadores.addEventListener('keyup', function() {
            
            const filtroTexto = filtroInputJogadores.value.toLowerCase();
            const linhas = tabelaCorpoJogadores.querySelectorAll('tr');
            
            linhas.forEach(function(linha) {
                const celulaNome = linha.querySelector('td');
                if (celulaNome) {
                    const nomeJogador = celulaNome.textContent.toLowerCase();
                    if (nomeJogador.includes(filtroTexto)) {
                        linha.style.display = "";
                    } else {
                        linha.style.display = "none";
                    }
                }
            });
        });
    }

    const filtroInputElencos = document.getElementById('filtro-elencos');
    if (filtroInputElencos) {
        const tabelaCorpoElencos = filtroInputElencos.closest('main').querySelector('table tbody');

        filtroInputElencos.addEventListener('keyup', function() {
            
            const filtroTexto = filtroInputElencos.value.toLowerCase();
            const linhas = tabelaCorpoElencos.querySelectorAll('tr');
            
            linhas.forEach(function(linha) {
                const celulaNome = linha.querySelector('td'); 
                if (celulaNome) {
                    const nomeElenco = celulaNome.textContent.toLowerCase().trim();
                    
                    if (nomeElenco.includes(filtroTexto)) {
                        linha.style.display = "";
                    } else {
                        linha.style.display = "none";
                    }
                }
            });
        });
    }

});