from yolo_opencv import obj_detect
import cv2
import imagezmq
image_hub = imagezmq.ImageHub(open_port='tcp://10.0.0.40:5555')
while True:  # show streamed images until Ctrl-C
    rpi_name, image = image_hub.recv_image()
    print(rpi_name)
    cv2.imshow(rpi_name, image) # 1 window for each RPi
    im = obj_detect(image)
    cv2.imshow("detected", im)
    cv2.waitKey(1)
    image_hub.send_reply(b'OK')