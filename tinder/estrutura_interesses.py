database = {} #um dicionário, que tem a chave interesses para o controle
#dos interesses (que pessoa se interessa por que outra), e pessoas para o controle de pessoas 
#(quem sao as pessoas e quais sao os dados pessoais de cada pessoa no sistema)
#voce pode controlar as pessoas de outra forma se quiser, nao precisa mudar nada
#do seu código para usar essa váriavel
database['interesses'] = { 
    100: [101, 102, 103],
    200: [100]
}
database['PESSOA'] = [] #esse voce só faz se quiser guardar nessa lista os dicionários das pessoas

#em todo esse codigo que estou compartilhando, as variaveis interessado, 
# alvo de interesse, pessoa, pessoa1 e pessoa2 sao sempre IDs de pessoas

class NotFoundError(Exception):
    pass

def todas_as_pessoas():
   return database['PESSOA']

def adiciona_pessoa(dic_pessoa):
    database['PESSOA'].append(dic_pessoa)
    id_pessoa = dic_pessoa['id']
    database['interesses'][id_pessoa] = []

def localiza_pessoa(id_pessoa):
    for pessoa in database['PESSOA']:
        if pessoa["id"] == id_pessoa:
            return pessoa
    raise NotFoundError    


def reseta():
    database['PESSOA'].clear()
    database['interesses'].clear()


def adiciona_interesse(id_interessado, id_alvo_de_interesse):
    localiza_pessoa(id_interessado)
    localiza_pessoa(id_alvo_de_interesse)
    database['interesses'][id_interessado].append(id_alvo_de_interesse)
    
def consulta_interesses(id_interessado):
    for c,v in database['interesses'].items():
        if c == id_interessado:
            return v
    raise NotFoundError
    # OR
    # localiza_pessoa(id_interessado)
    # return database['interesses'][id_interessado]

def remove_interesse(id_interessado,id_alvo_de_interesse):
    localiza_pessoa(id_interessado)
    localiza_pessoa(id_alvo_de_interesse)
    database['interesses'][id_interessado].remove(id_alvo_de_interesse)    

#essa funcao diz se o 1 e o 2 tem match. (retorna True se eles tem, False se não)
#ela não está testada, só existe para fazer aquecimento para a próxima
def verifica_match(id1,id2):
    interesse_id1 = consulta_interesses(id1)
    interesse_id2 = consulta_interesses(id2)
    if id1 in interesse_id2 and id2 in interesse_id1:
        return True
    return False
    # OR
    # verifica1gosta2 = id2 in interesse_id1
    # verifica1gosta1 = id1 in interesse_id2
    # return verifica1gosta1 and verifica1gosta2
    
      
def lista_matches(id_pessoa):
    

