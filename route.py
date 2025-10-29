from app.controllers.application import Application
from bottle import Bottle, route, run, request, static_file
from bottle import redirect, template, response


app = Bottle()
ctl = Application()


#-----------------------------------------------------------------------------

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')

#-----------------------------------------------------------------------------
@app.route('/helper')
def action_helper(info= None):
    return ctl.helper()

#-----------------------------------------------------------------------------

@app.route('/')
@app.route('/index')
def action_index():
    return ctl.index()

@app.route('/formulario', methods=['GET'])
def action_formulario_novo():
    return ctl.formulario_novo()

@app.route('/formulario/salvar', methods=['POST'])
def action_salvar_novo():
    return ctl.salvar_novo()

@app.route('/editar/<jogador_id>', methods=['GET'])
def action_formulario_editar(jogador_id):
    return ctl.formulario_editar(jogador_id)

@app.route('/editar/salvar', methods=['POST'])
def action_salvar_edicao():
    return ctl.salvar_edicao()

@app.route('/deletar/<jogador_id>', methods=['GET'])
def action_deletar(jogador_id):
    return ctl.deletar(jogador_id)


#-----------------------------------------------------------------------------
if __name__ == '__main__':

    run(app, host='0.0.0.0', port=5000, debug=True)
