from sshtunnel import SSHTunnelForwarder
import pymysql as db
import pandas as pd

class PickaDB(SSHTunnelForwarder):
    localhost = '127.0.0.1'
    def __init__(self):
        pass

    def connect(self, 
        host=None, ssh_username=None, ssh_private_key=None, 
        user=None, password=None, database=None):

       
        self.server =  SSHTunnelForwarder((host, 22),
            ssh_username=ssh_username,
            ssh_private_key=ssh_private_key,
            remote_bind_address=('127.0.0.1', 3306))

        self.server.start()

        self.conn = db.connect(host=self.localhost,
                    port=self.server.local_bind_port,
                    user=user,
                    passwd=password,
                    db=database,
                    charset='utf8')

        
    def query(self, query):    
        table = pd.read_sql_query(query, self.conn)

        output = []
        for idx, row in table.iterrows():
            output.append({
                'number' : row['from_number'],
                'sentence' : row['text']
            })

        return output

    def insert(self, query):
        curs = self.conn.cursor()
        ret = curs.execute(query)
        self.conn.commit()
        return ret

    def close(self):
        self.conn.close()

    def __del__(self):
        self.conn.close()
        self.server.stop()


def main():
    pica_db = PickaDB()
    pica_db.connect()
    result = pica_db.query()

if __name__=="__main__":
    main()