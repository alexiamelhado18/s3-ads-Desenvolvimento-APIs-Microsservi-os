from flask import Flask, jsonify, request
import estrutura_interesses as i

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def ola():
    return "servidor do tinder"

#/pessoas, com GET, para pegar a lista de todas as pessoas
@app.route("/pessoas")
def pessoas():
    return jsonify(i.todas_as_pessoas())


#/pessoas, com POST, receber um dicionário de uma pessoa e colocar na lista
@app.route("/pessoas", methods=["POST"])
def coloca_na_lista():
    dic_recebido = request.json #representa um dicionario enviado pela rede
    i.adiciona_pessoa(dic_recebido)
    return "adicionado"

@app.route("/pessoas/<int:id_pessoa>"])
def localiza_pessoa(id_pessoa):
    try:
        a = i.localiza_pessoa(id_pessoa)
    except i.NotFoundError:
        return {"erro": "usuário não existe"}, 400
    return a

@app.route("/reseta", methods=["POST"])
def resetar_lista():
    return i.reseta()

    






if __name__ == '__main__':
    app.run(host='localhost', port=5003, debug=True)
