#python detect_faces_cmd.py -p Detection_models/deploy.prototxt.txt -d Detection_models/ResNet_300x300.caffemodel
import sys,os
sys.path.append(os.getcwd())
from imutils.video import VideoStream
import numpy as np
import argparse
import time
import cv2

# Required arguments are paths to prototxt, detection model and classification model to be used
ap = argparse.ArgumentParser(description='''<Face detection using deep learning,
                             make sure you have a webcamera connected to your computer before running.
                             At the top of the script there is a "copy-paste" cmd command to run given that you
                             are using the provided folder structure from github.\n To exit the application when running,
							 either press 'q' on your keyboard or close the terminal>
                             ''')
# Required arguments are paths to prototxt and model to be used
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototxt", required=True,
	help="path to Caffe 'deploy.prototxt.txt' prototxt file")
ap.add_argument("-d", "--detect", required=True,
	help="path to CaffeModel 'ResNet_300x300.cafemodel for detection")
ap.add_argument("-c", "--confidence", type=float, default=0.7,
	help="minimum probability to filter weak detections, defaults at 0.7")
args = vars(ap.parse_args())

print("<loading model>")
detectM = cv2.dnn.readNetFromCaffe(args["prototxt"], args["detect"])

print("<starting video stream>")
vs = VideoStream(src=0).start()
time.sleep(1.0)

while True:
	frame = vs.read()

	(h, w) = frame.shape[:2]
	blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,
		(300, 300), (104.0, 177.0, 123.0))
 
	detectM.setInput(blob)
	detections = detectM.forward()

	# loop over the detections
	for i in range(0, detections.shape[2]):
		# extract the probability for faces in frame(confidence)
		confidence = detections[0, 0, i, 2]

		if confidence < args["confidence"]:
			continue

		box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
		(startX, startY, endX, endY) = box.astype("int")
 
		text = "{:.2f}%".format(confidence * 100)
		y = startY - 10 if startY - 10 > 10 else startY + 10
		cv2.rectangle(frame, (startX, startY), (endX, endY),
			(0, 0, 255), 2)
		cv2.putText(frame, text, (startX, y),
			cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

cv2.destroyAllWindows()
vs.stop()