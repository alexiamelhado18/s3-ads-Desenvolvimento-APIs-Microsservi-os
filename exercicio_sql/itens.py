from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = create_engine('sqlite:///rpg.db')

class ItemNaoExisteException(Exception):
    pass

def consultar_item(id_i):
    with engine.connect() as con:
        statement = text ("""SELECT * FROM Item WHERE id = :item""")
        rs = con.execute(statement, item=id_i) 
        item = rs.fetchone()
        if item != None:                        
            return dict(item)
        else:
            raise ItemNaoExisteException

