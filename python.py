from flask import Flask, render_template

app = Flask(__name__)

# Dados das mulheres inspiradoras
mulheres_inspiradoras = [
    {"nome": "Ada Lovelace", "imagem": "ada_lovelace.jpg"},
    {"nome": "Grace Hopper", "imagem": "grace_hopper.jpg"},
    {"nome": "Katherine Johnson", "imagem": "katherine_johnson.jpg"},
    # Adicione mais mulheres inspiradoras aqui
]

@app.route('/')
def pagina_inicial():
    return render_template('pagina.html', mulheres=mulheres_inspiradoras)

if __name__ == '__main__':
    app.run(debug=True)
