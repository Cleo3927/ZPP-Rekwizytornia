import cv2

class Camera():
    def __init__(self):
        self.camera = cv2.VideoCapture(2)
        self.photo = 0
        
    def gen_frames(self):  # generate frame by frame from camera
        while True:
            success, frame = self.camera.read() 
            if success:
                try:
                    ret, buffer = cv2.imencode('.jpg', cv2.flip(frame,1))
                    frame = buffer.tobytes()
                    yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
                except Exception as e:
                    pass
                
            else:
                pass

    def make_photo(self, photo_name):
        success, frame = self.camera.read() 
        cv2.imwrite('../../photos/' + photo_name + '.jpg', frame)
    
    def close_camera(self):
        self.camera.release()
