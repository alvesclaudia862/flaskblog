# Importa a classe Flask do módulo flask
from flask import Flask, render_template

# Cria uma instância da aplicação Flask
app = Flask(__name__)

# Define a rota para a URL raiz ('/')


@app.route('/')
def home():  # Função executada quando'/' é acessado

    # variável da página HTML
    toPage = {
        # Valor a tag <title>  → Título da página
        'title': 'Flaskblog',
        # Nome da folha de estilos desta página (opcional)
        'css': 'home.css'
        # Nome do JavaScript desta página (opcional)
        # 'js : 'home.js'
        # Outros pares "chave" : "valor" entram aqui
    }


# Abre a página de template → layout.html
  # Passa a variável local `toPage` para o template como `page`
    return render_template('layout.html', page=toPage)


@app.route('/contacts')  # Define a rota para a URL '/contatos'
def contacts():  # Função executada quando '/contacts' é acessado

    # Variável da página HTML
    toPage = {
        'title': 'Faça contato',
        'css': 'contacts.css',
    }

    # Retorna uma mensagem simples
      return render_template('contacts.html', page=toPage)


# Verifica se o script está sendo executado diretamente
if __name__ == '__main__':

    # Inicia o servidor Flask em modo debug
    app.run(debug=True)
