from flask import Flask, render_template, request, redirect

app = Flask(__name__)


clientes = []
id_cliente = 1 

@app.route('/')
def index():
    return render_template('index.html', clientes=clientes)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    global id_cliente  
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        telefone = request.form['telefone']
        email = request.form['email']
        clientes.append({'id': id_cliente, 'nome': nome, 'cpf': cpf, 'telefone': telefone,'email': email})  
        id_cliente += 1 
        return redirect('/')
    return render_template('cadastro.html')

@app.route('/cliente/<int:id>')
def cliente(id):
    cliente = None
    for c in clientes:
        if c['id'] == id:
            cliente = c
            break
    return render_template('cliente.html', cliente=cliente)

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
