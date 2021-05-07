#importing libraries

from flask import Flask,render_template,Response
import main  #main.py
app = Flask(__name__)

#function to get the streaming from main.py
def gen():
    while True:
        #get camera frame
        frame = main.face_recogntion()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

#default page
@app.route('/')
def index():
    return render_template('index.html')

#for video
@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

# srrver (localhost)
if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)