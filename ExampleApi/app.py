from flask import Flask, jsonify, request

app = Flask((__name__))

livros = [
    {
        'id': 1,
        'titulo': "O Senhor dos Anéis - A Sociedade do Anel",
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'titulo': "O Senhor dos Anéis - Duas Torres",
        'autor': 'J.R.R Tolkien'
    },
]

@app.route('/livros')
def getAll():
    return jsonify(livros)

@app.route('/livros/<int:id>', methods = ['GET'])
def getById(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify (livro)

app.run(port=5000, host='localhost', debug=True)