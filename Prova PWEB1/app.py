from flask import Flask, render_template, request, redirect

app = Flask(__name__)

topiks = []

@app.route('/')
def home():
    return render_template('index.html', topiks=topiks)


@app.route('/lista')
def lista():
    return render_template('lista.html', topiks=topiks)


@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        modelo = request.form['modelo']
        placa = request.form['placa']
        top = {'id':len(topiks)+1,'modelo': modelo, 'placa': placa}
        topiks.append(top)
        return redirect('/')
    return render_template('cadastrar.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def edit(id):
    for topik in topiks:
        if topik['id'] == id:
            if request.method == 'POST':
                topik['modelo'] = request.form['modelo']
                topik['placa'] = request.form['placa']
                return redirect('/')
    return render_template('editar.html', topiks=topiks, id=id)


@app.route('/excluir/<int:index>')
def excluir(index):
    if index < len(topiks):
        topiks.pop(index)
        return redirect ('/')
    return render_template('index.html')

if __name__ == '__main__':
 app.run(debug=True)

