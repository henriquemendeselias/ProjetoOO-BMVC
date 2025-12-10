document.addEventListener('DOMContentLoaded', function() {

    if (typeof io !== 'undefined') {
        var socket = io();

        socket.on('connect', function() {
            console.log('Conectado ao WebSocket');
        });

        function montarHTMLCelulas(dados) {
            return `
                <td>${dados.nome}</td>
                <td>${dados.nome_posicao}</td>
                <td>${dados.numero_camisa}</td>
                <td>${dados.idade}</td>
                <td>${dados.nacionalidade}</td>
                <td class="acoes">
                    <a href="/editar/${dados.id}" class="btn-editar">Editar</a>
                    <a href="/deletar/${dados.id}" class="btn-deletar">Deletar</a>
                </td>
            `;
        }

        socket.on('jogador_inserido', function(dados) {
            const tabelaCorpo = document.querySelector('table tbody');
            
            const cabecalhoCamisa = Array.from(document.querySelectorAll('table th')).find(th => th.textContent.includes('Camisa'));
            
            if (!tabelaCorpo || !cabecalhoCamisa) {
                return;
            }
            

            const linhaVazia = tabelaCorpo.querySelector('td[colspan="6"]');
            if (linhaVazia) {
                linhaVazia.parentElement.remove();
            }

            const novaLinha = document.createElement('tr');
            novaLinha.id = 'tr-jogador-' + dados.id; 
            novaLinha.innerHTML = montarHTMLCelulas(dados);

            tabelaCorpo.appendChild(novaLinha);
            
            novaLinha.style.backgroundColor = "#ffffcc";
            setTimeout(() => novaLinha.style.backgroundColor = "", 1000);
        });

        socket.on('jogador_editado', function(dados) {
            const linha = document.getElementById('tr-jogador-' + dados.id);
            if (linha) {
                linha.innerHTML = montarHTMLCelulas(dados);
                
                linha.style.backgroundColor = "#e6f7ff";
                setTimeout(() => linha.style.backgroundColor = "", 1000);
            }
        });

        socket.on('jogador_removido', function(dados) {
            const linha = document.getElementById('tr-jogador-' + dados.id);
            if (linha) {
                linha.style.backgroundColor = "#ffcccc";
                setTimeout(() => linha.remove(), 500);
            }
        });

        function montarHTMLCelulasTime(dados) {
            return `
                <td>
                    <a href="/elenco/${dados.id}" style="color: #004d98; font-weight: bold;">
                        ${dados.nome}
                    </a>
                </td>
                <td>${dados.tipo}</td>
                <td class="acoes">
                    <a href="/time/editar/${dados.id}" class="btn-editar">Config. Elenco</a>
                    <a href="/time/deletar/${dados.id}" class="btn-deletar">Deletar</a>
                </td>
            `;
        }

        socket.on('time_inserido', function(dados) {
            const tabelaCorpo = document.querySelector('table tbody');
            
            const cabecalho = document.querySelector('table th:nth-child(2)');
            if (!tabelaCorpo || !cabecalho || cabecalho.textContent !== 'Tipo') return;

            const linhaVazia = tabelaCorpo.querySelector('td[colspan="3"]');
            if (linhaVazia) {
                linhaVazia.parentElement.remove();
            }

            const novaLinha = document.createElement('tr');
            novaLinha.id = 'tr-time-' + dados.id;
            novaLinha.innerHTML = montarHTMLCelulasTime(dados);

            tabelaCorpo.appendChild(novaLinha);
            
            novaLinha.style.backgroundColor = "#ffffcc";
            setTimeout(() => novaLinha.style.backgroundColor = "", 1000);
        });

        socket.on('time_editado', function(dados) {
            const linha = document.getElementById('tr-time-' + dados.id);
            if (linha) {
                linha.innerHTML = montarHTMLCelulasTime(dados);
                
                linha.style.backgroundColor = "#e6f7ff";
                setTimeout(() => linha.style.backgroundColor = "", 1000);
            }
        });

        socket.on('time_removido', function(dados) {
            const linha = document.getElementById('tr-time-' + dados.id);
            if (linha) {
                linha.style.backgroundColor = "#ffcccc";
                setTimeout(() => linha.remove(), 500);
            }
        });

        function montarHTMLCelulasPosicao(dados) {
            return `
                <td>${dados.nome}</td>
                <td>${dados.sigla}</td>
                <td class="acoes">
                    <a href="/posicao/editar/${dados.id}" class="btn-editar">Editar</a>
                    <a href="/posicao/deletar/${dados.id}" class="btn-deletar">Deletar</a>
                </td>
            `;
        }

        socket.on('posicao_inserida', function(dados) {
            console.log("--- DEBUG SOCKET POSIÇÃO ---");
            console.log("Dados recebidos:", dados);
            console.log("URL Atual:", window.location.pathname);

            const tabelaCorpo = document.querySelector('table tbody');
            const cabecalho = document.querySelector('table th:nth-child(2)');
            const textoCabecalho = cabecalho ? cabecalho.textContent.trim() : "N/A";
            
            console.log("Texto do Cabeçalho encontrado:", textoCabecalho);

            const urlCorreta = window.location.pathname.indexOf('posic') !== -1;
            const cabecalhoCorreto = textoCabecalho.includes('Sigla');

            if (!tabelaCorpo || (!urlCorreta && !cabecalhoCorreto)) {
                console.log("IGNORADO: O sistema julgou que não estamos na tela de posições.");
                console.log("Motivo: URL contém 'posic'? " + urlCorreta);
                console.log("Motivo: Cabeçalho contém 'Sigla'? " + cabecalhoCorreto);
                return;
            }

            const linhaVazia = tabelaCorpo.querySelector('td[colspan="3"]');
            if (linhaVazia) linhaVazia.parentElement.remove();

            const novaLinha = document.createElement('tr');
            novaLinha.id = 'tr-posicao-' + dados.id;
            novaLinha.innerHTML = montarHTMLCelulasPosicao(dados);
            tabelaCorpo.appendChild(novaLinha);
            
            novaLinha.style.backgroundColor = "#ffffcc";
            setTimeout(() => novaLinha.style.backgroundColor = "", 1000);
        });

        socket.on('posicao_editada', function(dados) {
            const linha = document.getElementById('tr-posicao-' + dados.id);
            if (linha) {
                linha.innerHTML = montarHTMLCelulasPosicao(dados);
                linha.style.backgroundColor = "#e6f7ff";
                setTimeout(() => linha.style.backgroundColor = "", 1000);
            }
        });

        socket.on('posicao_removida', function(dados) {
            const linha = document.getElementById('tr-posicao-' + dados.id);
            if (linha) {
                linha.style.backgroundColor = "#ffcccc";
                setTimeout(() => linha.remove(), 500);
            }
        });
    }

    document.addEventListener('click', function(event) {
        
        const botaoClicado = event.target.closest('.btn-deletar');

        if (botaoClicado) {
            const linhaTabela = botaoClicado.closest('tr');

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
        }
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