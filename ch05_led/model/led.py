import pymysql

class LED:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',user='root',password='q1w2e3',database='study')
        self.cur = self.conn.cursor()
        print("connect ok!! good")

    def get(self):
        #모든 정보를 가져옴
        query = "select * from record_led"
        self.cur.execute(query)
        results = self.cur.fetchall()
        print(results)
        return results #클라이언트한테는 최종적으로 json형태가 되어야함

    def save(self,stauts):
        query = f"insert into recodr_led(stauts) values('{status}')"
        self.cur.excute(query)
        self.conn.commit()
