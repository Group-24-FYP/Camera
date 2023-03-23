import cv2

rtsp_url = "rtsp://root:entc@192.168.0.101/axis-media/media.amp"
cap = cv2.VideoCapture(rtsp_url)

width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer= cv2.VideoWriter('basicvideo.mp4', cv2.VideoWriter_fourcc(*'mp4v') , 30, (width,height))

while True:
    ret,frame= cap.read()
    writer.write(frame)
    cv2.imshow('frame', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()
