from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = "chave_secreta"

class Jogo:
    def __init__(self, id, nome, categoria, console):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.console = console



jogo1 = Jogo(1, 'Super Mario', 'Avantura', 'Nintendo')
jogo2 = Jogo(2, 'Pokemon', 'RPG', 'GBA')
lista_jogos = [jogo1, jogo2]

@app.route('/')
def home():
    return render_template('lista-jogos.html', titulo="Jogos", jogos=lista_jogos)

@app.route('/login')
def login():
    return render_template('login.html', titulo="Login")

@app.route('/autenticar', methods=['POST'])
def autenticar():
    formulario = request.form
    if(formulario['pass'] == '123'):
        session['usuario_logado'] = formulario['user']
        flash(formulario['user'] + ' logado com sucesso!')
        return redirect('/');
    
    flash('erro na tentativa de logar, usuario ou senha incorretas!')
    return redirect('/login');

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('usuário deslogado da sessão');
    return redirect('/login');

@app.route('/cadastro-jogos')
def novo_jogo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        flash('Usuario sem permissão de acesso')
        return redirect('/login');
    return render_template('cadastro-jogos.html', titulo='cadastro')

@app.route('/server-cadastro-jogos', methods=['POST'])
def insert_jogo():
    formulario = request.form
    jogo = Jogo(len(lista_jogos), formulario['nome'], formulario['categoria'], formulario['console'])
    lista_jogos.append(jogo)
    return redirect('/');

@app.route('/editar-jogos')
def editar_jogos():
    return render_template('editar-jogos.html',titulo="Editar", id=request.form['id'])

@app.route('/server-update-jogo', methods=['POST'])
def update_jogo():
    formulario = request.form
    #vai na lista global e verifica a existencia desse id e se houver ai traz o jogo
    #faz o update da lista e manda de volta
    return render_template('lista-jogos.html', titulo="Editar", jogos=lista_jogos)
    

app.run(debug=True)
