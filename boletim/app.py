from flask import Flask, redirect, url_for, session, request, render_template
from authlib.integrations.flask_client import OAuth
import requests

app = Flask(__name__)
app.debug = True
app.secret_key = 'development'
oauth = OAuth(app)

oauth.register(
    name='suap',
    client_id= "tJIwB2VZ5WUmVThDMIisVsUYXrYlJ4Tz5JzEcy6y",
    client_secret= "2vw9Gw8sGge7qChFx2SjGsQBxA24D6v2IckpGkI0Yo2ivIdpI1LJgBxTmzmo0sDDZES1n0oDdJ4PLVdD1WIlPZ3nGgAfO7LHiqadFIWBVJblQF8BWKtDJ4j1cMlQYV9u",
    api_base_url='https://suap.ifrn.edu.br/api/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://suap.ifrn.edu.br/o/token/',
    authorize_url='https://suap.ifrn.edu.br/o/authorize/',
    fetch_token=lambda: session.get('suap_token')
)

def get_boletim(ano, bimestre):
    if ano and bimestre:
        token = session.get('suap_token')['access_token']
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(f'https://suap.ifrn.edu.br/api/v2/minhas-informacoes/boletim/{ano}/{bimestre}/', headers=headers)
        return response.json()
    return None

@app.route('/')
def index():
    if 'suap_token' in session:
        meus_dados = oauth.suap.get('v2/minhas-informacoes/meus-dados')
        return render_template('user.html', user_data=meus_dados.json())
    else:
        return render_template('index.html')

@app.route('/login')
def login():
    redirect_uri = url_for('auth', _external=True)
    return oauth.suap.authorize_redirect(redirect_uri)

@app.route('/logout')
def logout():
    session.pop('suap_token', None)
    return redirect(url_for('index'))

@app.route('/login/authorized')
def auth():
    token = oauth.suap.authorize_access_token()
    session['suap_token'] = token
    return redirect(url_for('index'))

# Função principal para a rota '/user'
@app.route('/user', methods=['GET', 'POST'])
def user():
    if 'suap_token' not in session:
        return redirect(url_for('index'))

    boletim_data = None
    ano = None
    bimestre = None

    if request.method == 'POST':
        ano = request.form.get('ano')
        bimestre = request.form.get('periodo')

        # Chamada da função para obter o boletim
        boletim_data = get_boletim(ano, bimestre)

    meus_dados = oauth.suap.get('v2/minhas-informacoes/meus-dados')
    return render_template('user.html', user_data=meus_dados.json(), boletim=boletim_data, ano=ano, bimestre=bimestre)

if __name__ == '__main__':
    app.run()