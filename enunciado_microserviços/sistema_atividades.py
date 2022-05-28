from flask import Flask,jsonify,abort
from flask import make_response, request, url_for
import acesso

app = Flask(__name__)
#app.url_map.strict_slashes = False
atividades = [
    {
        'id_atividade':1,
        'id_disciplina':1,
        'enunciado': 'crie um app de todo em flask',
        'respostas': [
            {'id_aluno': 1, 'resposta':'todo.py', 'nota':9},
            {'id_aluno': 2, 'resposta':'todo.zip.rar'},
            {'id_aluno': 4, 'resposta':'todo.zip', 'nota':10}
            ]
    },

    {
        'id_atividade':2,
        'id_disciplina':1,
        'enunciado': 'crie um servidor que envia email em Flask',
        'respostas': [
            {'id_aluno': 4, 'resposta':'email.zip', 'nota':10}
            ]
    },

    ]
@app.route('/atividade/<int:id_atividade>/')
def busca_atividade(id_atividade):

    request.args #dicionario da query string 
                 # ex: /atividade/1/?id_professor=20
                 #  request.args['id_professor'] vale 20
                 #  chave id_professor, valor 20
    for atividade in atividades:
        if atividade['id_atividade'] == id_atividade:
            copia = atividade.copy()
            copia['url'] = f'/atividade/{id_atividade}/'
            if 'id_professor' in request.args.keys():
                id_professor = request.args['id_professor']
                if not acesso.leciona(id_professor,atividade['id_disciplina']):
                    copia.pop('respostas')
                return {'isok': True, 'atividade': copia, 'id_professor': id_professor}
            copia.pop('respostas')
            return {'isok': True, 'atividade': copia}
            
    return {'isok': False, 'erro': 'atividade nao encontrada'},404

@app.route('/')
def index():
    return "Sistema de entrega de atividades"

'''
Vou deixar a primeira URL definida, pra facilitar o debug.
Nao mude ela em nada
'''
@app.route('/atividades/ver_tudo/', methods=['GET'])
def get_all():
    return jsonify(atividades)

'''
Crie uma URL para exibir uma atividade,
em /atividade/<int:id_atividade>/

Ela deve retornar 
{'isok': True, 'atividade': dicionario_da_atividade}
Se a atividade existir

Repare, o retorno é um dicionario com duas chaves, isok
e atividade. O dicionário da atividade em si aparece 
como valor associado à chave atividade

Se a atividade não existir, retorne
{'isok': False, 'erro': 'atividade nao encontrada'} com codigo de status 404

Para terminar essa tarefa, passe os testes 003 e 004
'''


'''
Agora, vamos alterar o comportamento da URL anterior.

Ela deve adicionar na atividade a URL em que ela se encontra,
usando uma chave 'url' no dicionário. (Exemplo: No dicionário,
o valor "/atividade/10/", associado à chave "url")

Normalmente retornamos as IDs dos objetos, mas é mais conveniente
para o programador (ou programadora) que está do outro lado
se a gente retornar a URL de uma vez. Menos coisa pra ele (ela)
lembrar!
Para terminar essa tarefa, passe os testes 005a e 005b
(mas veja abaixo para explicacao do 005b)
'''
'''
Outro detalhe: sua melhoria anterior pode estar salvando
a URL no servidor. 

Cuidado para não fazer a URL aparecer na
estrutura de dados do servidor. Ela deve ser enviada,
mas sem alterar os dados salvos no servidor
(esse bug é verificado no teste 005b)

Como fazer? Você pode gerar uma cópia do dicionário e alterar 
a cópia.

Exemplo:
d_copy = d.copy()
'''

'''
Vamos fazer mais um upgrade na url anterior

Esse aqui faz pouco sentido, confesso. Ele só existe pra
ajudar você com o proximo teste.

Sua url agora deve receber como parametro de query uma id_professor.

Devolva esse parametro no dicionario retornado , 
usando a chave id_professor.

Ou seja, o dicionario que tinha as chaves 'isok' e 'atividade'
agora terá 'isok', 'atividade' e 'id_professor' (assumindo que a url tenha vindo com esse parametro)

Com isso, voce passa o teste 006
---------------------------------------------------------------------
Parametro de query??

Estamos falando de algo como
requests.get('http://localhost:5050/atividade/1/?id_professor=15')

(talvez você lembre, há muito tempo, da aula de redes...)

Nesse caso, o dicionario retornado deve ter uma chave id_professor, com um valor 15
---------------------------------------------------------------------
Dica de flask

Para pegar a id_professor enviada, voce 
pode consultar o dicionario request.args dentro da
funcao do Flask. Verifique primeiro se ele
TEM a chave id_professor, pois muitos dos requests
de testes anteriores nao tinham esse parametro na url!

id_professor = request.args["id_professor"] -- pega o valor da
'''

'''
Vamos fazer mais um upgrade na url anterior

Ela já recebe como parametro de query uma id_professor.

Ela só deve retornar as respostas dos alunos se o professor
for um professor da disciplina. Caso contrario, deve suprimir
as respostas, só retornar o resto da atividade

Para isso vamos usar o acesso.py, que já tem uma função
adequada para perguntar ao controle_pessoas se um professor
leciona uma disciplina
Se voce terminar essa, vai passar o teste 007a e 007b (e construiu
um sisteminha baseado em microservicos!)
'''

'''
Um ultimo upgrade: Se eu não mandar professor nenhum, 
excluir da mesma forma as respostas dos alunos
Esse é o 007c

dica de python

"id_professor" in request.args -- verifica se a chave existe no dicionário
'''

'''
FINAL BOSS - Testes 008a 008b e 008c

Faça esse mesmo ciclo (controle_pessoas > acesso > sistema_atividades)
para definir uma url notas no servidor sistema_atividades

Ao acessar /notas/<nome_do_aluno>/id_disciplina/,
devo receber um dicionário, com a chave notas
e uma lista das notas do aluno naquela disciplina

Repare que, como estamos usando nome do aluno e não id, 
teremos que fazer uma consulta ao servidor de controle_pessoas.

Vamos definir uma URL no controle_pessoas, acessar ela pelo acesso.py,
e usar aqui.

Dica: para definir URLs com buracos para números, a gente usa <int:nome_var>;
Se o buraco for ser preenchido com uma string, use apenas <nome_var>
'''



'''
Desafio (sem testes) 
o que acontece com a sua funcao de atividades quando 
o servidor de pessoas esta caido?

Seria conveniente que o sistema desse um erro 500 e devolvesse
um dicionário descritivo do erro.

Para isso, você poderia lançar uma excessão no arquivo de acesso, e tratar ela nesse arquivo.
'''

if __name__ == '__main__':
   app.run(debug=True, host='localhost', port=5050)
