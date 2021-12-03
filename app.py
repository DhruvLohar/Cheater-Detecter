import cv2
from flask import *
from database.db import DataBase

app = Flask(__name__)
db = DataBase()

camera=cv2.VideoCapture('http://@192.168.0.102:8080/video')

def generate_frames():
    while True:
            
        ## read the camera frame
        success,frame=camera.read()
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()

        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/admin')
def index():
    return render_template('admin.html')

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/login/")
def login_view():
    return render_template("login.html")


@app.route('/login/auth/', methods=['POST'])
def authenticate():
    if request.method == "POST":
        data = request.get_json()
        db_data = db.fetch(data['email'])
        if db_data is not None:
            if data['password'] == db_data[3]:
                return jsonify({'success': 'true'})
            else:
                return jsonify({'success': 'false', 'msg': 'Invalid Credentials'})


@app.route("/exam/physics/")
def exam_view():
    questions = db.fetch_que(0)
    response_data = {
        'questions': [],
        '_que': db.fetch_que(1)
    }
    for data in questions:
        response = {
            'que_id': data[0],
            'que': data[1]
        }
        response_data['questions'].append(response)
    return render_template("exam.html", data=response_data)


@app.route("/dbcontent/questions/<int:que_id>/", methods=['GET'])
def get_db_content(que_id):
    if request.method == "GET":
        data = db.fetch_que(que_id)
        return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)