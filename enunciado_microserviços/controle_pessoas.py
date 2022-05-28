from flask import Flask,jsonify,abort
from flask import make_response, request, url_for


app = Flask(__name__)
#app.url_map.strict_slashes = False
professores = [
    {'nome':"joao", 'id_professor': 1},
    {'nome':"jose", 'id_professor': 2},
    {'nome':"maria", 'id_professor': 3}
    ]

alunos = [
    {'nome':"alexandre", 'id_aluno':1},
    {'nome':"miguel", 'id_aluno':2},
    {'nome':"janaina", 'id_aluno':3},
    {'nome':"cicero", 'id_aluno':4},
    {'nome':"dilan", 'id_aluno':5},
    ]

disciplinas = [
    {'nome':"apis e microservicos", 'id_disciplina':1, 'alunos':[1,2,3,4], 'professores':[1], 'publica': False},
    {'nome':"matematica financeira", 'id_disciplina':2, 'alunos':[2], 'professores':[3], 'publica': True},
    {'nome':"matematica basica", 'id_disciplina':3, 'alunos':[1,2], 'professores':[3,2], 'publica': False}
    
    ]

@app.route('/')
def index():
    return "Sistema de controle de pessoas"

'''
Vou deixar a primeira URL definida, pra facilitar o debug
'''
@app.route('/pessoas/ver_tudo/', methods=['GET'])
def get_all():
    return jsonify([professores,alunos,disciplinas])


'''
Crie uma URL /leciona/<int:id_professor>/<int:id_disciplina>/

Ela deve retornar se um professor leciona ou nao uma determinada disciplina

Se ele leciona, o retorno deve ser
{'isok':True, 'leciona':True}

Caso contrario,
{'isok':True, 'leciona':False}

Se a disciplina nao for encontrada, retorne
{'isok':False, 'erro':'disciplina nao encontrada'}
e o codigo de status será 404
'''
@app.route('/leciona/<int:id_professor>/<int:id_disciplina>')
def verifica_leciona(id_professor, id_disciplina):
    for disciplina in disciplinas:
        if disciplina['id_disciplina'] == id_disciplina:
            if id_professor in disciplina['professores']:
                return {'isok':True, 'leciona':True}
            return {'isok':True, 'leciona':True}


'''
Sua função leciona vai estar pronta quando você tiver passado os testes 000,
001a e 001b. 

Quando isso acontecer, vá para o arquivo acesso.py
'''



if __name__ == '__main__':
   app.run(debug=True, host='localhost', port=5000)
