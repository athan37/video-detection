from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import cv2
from process_frame import process

def main():
    print("[Info] Starting video stream...")
    vs = VideoStream(src=0).start()

    time.sleep(2.0)

    print("[Info] Initiation finished")
    fps = FPS().start()

    while True:
        frame = vs.read()
        frame = imutils.resize(frame, width=600)

        process(frame)

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"): break

        fps.update()

    fps.stop()
    print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
    # do a bit of cleanup
    cv2.destroyAllWindows()
    vs.stop()

if __name__ == "__main__":
    main()
