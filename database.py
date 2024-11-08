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
    
  
    
if __name__ == "__main__":
    db = database.Database()
    print(db.get_animals())