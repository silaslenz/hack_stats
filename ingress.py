import sys
import time
import analyse
from multiprocessing import Process
ops_button_corner = (151, 636)


def go_through_frames(fn):
    import cv2
    import time
    cap = cv2.VideoCapture("./screen.mp4")
    lastfound = []
    while not cap.isOpened():
        cap = cv2.VideoCapture("./screen.mp4")
        cv2.waitKey(1000)
        print ("Wait for the header")

    pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
    cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, pos_frame + 900)
    while True:
        #pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
        #cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, pos_frame + 9)
        flag, frame = cap.read()

        if flag:
            # The frame is ready and already captured
            pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
            if (fn(frame)) is not None:
                if analyse.color_of_hack(frame, fn(frame)) != lastfound:
                    lastfound = analyse.color_of_hack(frame, fn(frame))
                    print lastfound

            cv2.imshow('video', frame)
            #print (str(pos_frame) + " frames")
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

go_through_frames(analyse.find_line)
