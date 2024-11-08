import sqlalchemy as sqla
import database

CONNECTION_STRING = "mysql+pymysql://root@localhost/db"

class Database():
    def __init__(self):
        self.engine = sqla.create_engine(CONNECTION_STRING)
        self.connaction = self.engine.connect()

    def translate_to_dict(self, result_raw):
        result = []
        for r in result_raw:
            result.append(r._asdict())    
        return result
    
    def get_animals(self):
        query = sqla.text("SELECT * FROM animals")
        result_raw = self.connaction.execute(query).all()
        return self.translate_to_dict(result_raw)
    
    def del_animals(self,id):
        query = sqla.text("DELETE FROM animals WHERE id = :id")
        query = query.bindparams(sqla.bindparam("id", id))
        self.connaction.execute(query)
        self.connaction.commit()        

    def add_animals(self, name):
        query = sqla.text("INSERT INTO animals (name) VALUES (:name) ")
        query = query.bindparams(sqla.bindparam("name", name))
        self.connaction.execute(query)
        self.connaction.commit()

    def edit_animals(self, name, id):
        query = sqla.text("UPDATE animals SET name = :name WHERE id = :id")
        query = query.bindparams(sqla.bindparam("name", name))
        query = query.bindparams(sqla.bindparam("id", id))
        self.connaction.execute(query)
        self.connaction.commit()
  
    
if __name__ == "__main__":
    db = Database()
    print(db.get_animals())