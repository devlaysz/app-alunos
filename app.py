from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

lista_principal = []

@app.route('/')
def index():
    return render_template('index.html', alunos=lista_principal)

@app.route('/cadastrar', methods=['POST'])
def cadastrar_aluno():
    nome = request.form['nome']
    matricula = int(request.form['matricula'])
    idade = int(request.form['idade'])
    curso = request.form['curso']
    horario = request.form['horario']
    
    aluno = {'nome': nome, 'matricula': matricula, 'idade': idade, 'curso': curso, 'horario': horario}
    lista_principal.append(aluno)
    flash('Aluno cadastrado com sucesso!')
    
    return redirect(url_for('index'))

@app.route('/remover', methods=['POST'])
def remover_aluno():
    matricula = int(request.form['remover_matricula'])
    global lista_principal
    lista_principal = [aluno for aluno in lista_principal if aluno['matricula'] != matricula]
    flash('Aluno removido com sucesso!')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)