import pymysql
class TodoDB:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',user='root',password='q1w2e3',db='study')  
        self.cur = self.conn.cursor()
        print("connect ok")

    def get(self):
        sql = "select * from todos"
        self.cur.execute(sql)
        values = self.cur.fetchall()
        return values
    def add(self,title):
        sql =  f"insert into todos(task) values('{title}')"
        self.cur.execute(sql)
        self.conn.commit()
    def remove(self,todo_index):
        sql = f"delete form todos where todo_index = {}"
        self.cur.execute(sql)
        self.conn.commit();
