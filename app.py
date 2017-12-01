from flask import Flask, render_template, Response, jsonify, make_response
import cv2


app = Flask(__name__)


def gen():
    """Video streaming generator function."""
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        ret, bufer = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + bufer.tobytes() + b'\r\n')
    cap.release()

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # imageObject.save_image()
    app.run(host='0.0.0.0', debug=True, threaded=True)
