import requests


'''
Crie uma funcao que retorna True 
se um professor leciona uma disciplina
e False caso contrario

Se a disciplina nao existe, retorne uma tupla: (False,'disciplina inexistente')

IMPORTANTE: essa função deve consultar o servidor definido
no controle pessoas, através da rede. Nao deve de nenhuma forma
dar import no arquivo controle pessoas ou acessar os dados
de alguma outra forma

A assinatura da função:

def leciona(id_professor, id_disciplina):
    pass
'''
def leciona(id_professor, id_disciplina):
    resp = requests.get(f'http://localhost:5000/leciona/{id_disciplina}/{id_professor}')
    dic_disciplina = json.dumps(resp)

    if dic_disciplina['isok'] == False:
        return (False, 'disciplina inexistente')
    return dic_disciplina['leciona']


'''
Agora, de runtests.

Se esta tudo ok, (passou testes 002a e 002b) siga para o arquivo 
sistema_atividades.py

'''


