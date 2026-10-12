from flask import Flask, render_template
import pymysql

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")

#상단에 import pymysql 추가

@app.route("/<num>")
def up(num):
    print(num)
    '''
        1. numcount 테이블 생성(id, num, insert_at)
        2. pymysql로 연결

        3. 증가 한 수만큼 추가
        4. 연결끊기
        5. db 접속해서 조회
    '''
    dbdb = pymysql.connect(host='localhost', user='root', password='q1w2e3', db='study2')
    cur = conn.cursor() #SQL 문을 실행하거나 실행된 결과를 돌려받는 통로
    cur.execute("insert into numcount(num)values(%s)",num)
    dbdb.commit()
    dbdb.close()
    return render_template("index.html")

@app.get("/<int:number>")
def receive_number(number):
    print(f"[백엔드가 받은 숫자] {number}", flush=True)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
