from flask import Flask, request, jsonify
from models.user import User
from database import db
from flask_login import LoginManager, login_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key" # A chave secreta é usada para proteger as sessões e os cookies do aplicativo.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # Configura a URI do banco de dados para usar SQLite. O banco de dados será armazenado em um arquivo chamado "database.db" no diretório do projeto.

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)
#view login
login_manager.login_view = 'login' # Especifica a rota de login para redirecionar os usuários não autenticados quando tentarem acessar rotas protegidas.


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id) # Carrega o usuário com base no ID fornecido. O ID é convertido para um inteiro antes de consultar o banco de dados.

@app.route('/login', methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        #login
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
                login_user(user)
                print(current_user.is_authenticated) # Verifica se o usuário está autenticado
                return jsonify({"message": "Autenticação realizada com sucesso"})

    return jsonify({"message": "Credenciais inválidas"}), 400

@app.route("/hello-world", methods=["GET"])
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)