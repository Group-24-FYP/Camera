import cv2
import imutils
from imutils.video import VideoStream
rtsp_url = "rtsp://root:entc@192.168.0.101/axis-media/media.amp"
#video_stream = VideoStream(rtsp_url).start()
video_stream = cv2.VideoCapture(rtsp_url)

# fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
# writer= cv2.VideoWriter('basicvideo.mp4',fourcc, 30, (576,720))

w = video_stream.get(cv2.CAP_PROP_FRAME_WIDTH)
h = video_stream.get(cv2.CAP_PROP_FRAME_HEIGHT)
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
writer = cv2.VideoWriter('output.mp4',fourcc, 30, (576,720))

while True:
    frame = video_stream.read()
    writer.write(frame)
    cv2.imshow('frame', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

video_stream.stop()
writer.release()
cv2.destroyAllWindows()