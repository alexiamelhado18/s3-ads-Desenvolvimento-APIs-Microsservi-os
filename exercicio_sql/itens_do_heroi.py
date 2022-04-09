from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = create_engine('sqlite:///rpg.db')

class ItemNaoExisteException(Exception):
    pass

def heroi_tem_item(id_h):
    with engine.connect() as con:
        statement = text ("""SELECT * FROM ItemDoHeroi WHERE idheroi = :heroi""")
        rs = con.execute(statement, heroi=id_h) 
        heroi = rs.fetchone()
        if heroi != None:
            return True
        else:
            return False
