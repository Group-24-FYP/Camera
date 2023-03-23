import cv2
import imutils
from imutils.video import VideoStream
rtsp_url = "rtsp://root:entc@192.168.0.101/axis-media/media.amp"
video_stream = VideoStream(rtsp_url).start()

while True:
    frame = video_stream.read()
    if frame is None:
        continue

    frame = imutils.resize(frame,width=720,height=576)
    cv2.imshow('AsimCodeCam', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()
video_stream.stop()