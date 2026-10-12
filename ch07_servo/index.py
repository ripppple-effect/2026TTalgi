from flask import Flask, request, render_template, jsonify
from servo import setAngle

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/angle', methods=['POST'])
def control_servo():
    data = request.get_json()
    angle = data.get('angle')  # POST 요청에서 'angle' 값을 가져옴
    if angle is not None:
        setAngle(int(angle))  # 서보 모터 각도 설정
        return jsonify({'message': 'angle set to {}'.format(angle)})
    else:
        return jsonify({'message': 'fail! check your parameter'})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False, use_reloader=False)
