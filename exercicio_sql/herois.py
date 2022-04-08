from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = create_engine('sqlite:///rpg.db')

# Essa classe só representa uma exception com
#novo nome. Não mexa dentro dela.
# Escreva os imports (acima dela)
# E suas funcoes (depois dela)
class HeroiNaoExisteException(Exception):
    pass

#escreva suas funcoes aqui

def heroi_existe(id_h):
    with engine.connect() as con:
        #query com "buraco" com o nome Heroi    
        statement = text ("""SELECT * FROM Heroi WHERE id = :heroi""")
        rs = con.execute(statement, heroi=id_h) #e usei esse buraco
        heroi = rs.fetchone()
        if heroi != None:                        
            return True
        else:
            return False
        return dict(jogador)

def consultar_heroi(id_h):
    with engine.connect() as con:

        statement = text ("""SELECT * FROM Heroi WHERE id = :heroi""")
        rs = con.execute(statement, heroi=id_h) 
        heroi = rs.fetchone()

        if heroi != None:
            return dict(heroi)
        else:                                    
            raise HeroiNaoExisteException

