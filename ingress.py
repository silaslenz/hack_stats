import sys
import time
from multiprocessing import Process
ops_button_corner = (151, 636)


def find_line(rgb_im):
    if rgb_im[ops_button_corner][0] > 200 and rgb_im[ops_button_corner][1] > 200 and rgb_im[ops_button_corner][2] > 200:
        for y in range(700, 1150):
            for x in range(650, 680):
                b, g, r = rgb_im[y, x]
                # print r,g,b
                #print (rgb_im[y,x-500]==rgb_im[y,x]).all()
                # print b
                if (rgb_im[y, x - 500] == rgb_im[y, x]).all() and b > 200 and g > 150 and r < 50:
                    return (x, y)


def go_through_frames(fn):
    import cv2
    import time
    f = open("imfile.txt", "w")
    cap = cv2.VideoCapture("./screen.mp4")
    while not cap.isOpened():
        cap = cv2.VideoCapture("./screen.mp4")
        cv2.waitKey(1000)
        print ("Wait for the header")

    pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
    cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, pos_frame + 200)
    while True:
        pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
        cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, pos_frame + 9)
        flag, frame = cap.read()

        if flag:
            # The frame is ready and already captured
            if (fn(frame)) is not None:
                print (fn(frame))
            cv2.imshow('video', frame)
            pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
            print (str(pos_frame) + " frames")
        else:
            # The next frame is not ready, so we try to read it again
            cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, pos_frame - 1)
            print ("frame is not ready")
            # It is better to wait for a while for the next frame to be ready
            cv2.waitKey(1000)

        if cv2.waitKey(10) == 27:
            break
        if cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES) == cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT):
            # If the number of captured frames is equal to the total number of frames,
            # we stop
            break

go_through_frames(find_line)
