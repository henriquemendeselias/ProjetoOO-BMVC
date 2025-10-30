document.addEventListener('DOMContentLoaded', function() {

    const botoesDeletar = document.querySelectorAll('.btn-deletar');

    botoesDeletar.forEach(function(botao) {
        
        botao.addEventListener('click', function(event) {
            
            let nomeJogador = 'este item';
            try {
                nomeJogador = event.target.closest('tr').querySelector('td').textContent;
            } catch (e) {
            }

            const confirmou = confirm(`Tem certeza que deseja deletar "${nomeJogador}"? \n\nEsta ação não pode ser desfeita.`);
            
            if (!confirmou) {
                event.preventDefault(); 
            }
        });
    });

});