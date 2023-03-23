import cv2
import imutils
from imutils.video import VideoStream
rtsp_url = "rtsp://root:entc@192.168.0.101/axis-media/media.amp"
video_stream = VideoStream(rtsp_url).start()

writer= cv2.VideoWriter('basicvideo.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 30, (576,720))

while True:
    frame = video_stream.read()
    writer.write(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

video_stream.stop()
writer.release()
cv2.destroyAllWindows()