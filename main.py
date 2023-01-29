from flask import Flask, render_template, url_for
from forms import FormsCriarConta, FormsLogin

app = Flask(__name__)

lista_usuarios = ['Lira', 'João', 'Alon', 'Alessandra', 'Amanda', 'Jeremias', 'Jarbas Vasconselos', 'Aristides', 'Toim']

app.config['SECRET_KEY'] = 'f2be536d261f3ba1ff76ceac95231969'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormsLogin()
    form_criar_conta = FormsCriarConta()
    return render_template('login.html', form_login = form_login, form_criar_conta = form_criar_conta)

if __name__ == '__main__':
    app.run(debug=True)