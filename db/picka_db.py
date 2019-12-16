from sshtunnel import SSHTunnelForwarder
import pymysql as db
import pandas as pd

class PickaDB():
    localhost = '127.0.0.1'
    def __init__(self):
        pass

    def connect(self, 
        host=None, ssh_username=None, ssh_private_key=None, 
        user=None, password=None, database=None):

        server = SSHTunnelForwarder((host, 22),
            ssh_username=ssh_username,
            ssh_private_key=ssh_private_key,
            remote_bind_address=(self.localhost, 3306))

        self.conn = db.connect(host=self.localhost,
            port=server.local_bind_port, user=user,
            passwd=password, db=database, charset='utf8')
        
    def query(self, query):    
        table = pd.read_sql_query(query, self.conn)

        output = []
        for row in table.rows:
            output.append({
                'number' : row['number'],
                'sentence' : row['sentence']
            })

        return output

    def insert(self, query):
        curs = self.conn.cursor()
        ret = curs.execute(q)
        self.conn.commit()
        return ret

    def close(self):
        self.conn.close()

    def __del__(self):
        self.close()


def main():

    pica_db = PicakDB()
    pica_db.connect()
    result = pica_db.query()



if __name__=="__main__":
    main()