#python classify_faces_cmd.py -p Detection_models/deploy.prototxt.txt -d Detection_models/ResNet_300x300.caffemodel -m Classification_model/model.model
import sys,os
sys.path.append(os.getcwd())
from imutils.video import VideoStream
from keras import models
import numpy as np
import argparse
import time
import cv2

# Required arguments are paths to prototxt, detection model and classification model to be used
ap = argparse.ArgumentParser(description='''<Facial emotion detection using deep learning,
                             make sure you have a webcamera connected to your computer before running.
                             At the top of the script there is a "copy-paste" cmd command to run given that you
                             are using the provided folder structure from github.\n To exit the application when running,
							 either press 'q' on your keyboard or close the terminal>
                             ''')
ap.add_argument("-p", "--prototxt", required=True,
	help="path to Caffe 'deploy.prototxt.txt' prototxt file")
ap.add_argument("-d", "--detect", required=True,
	help="path to CaffeModel 'ResNet_300x300.cafemodel for detection")
ap.add_argument("-m", "--classify", required=True,
    help="path to the classification model 'model.model'")
ap.add_argument("-c", "--confidence", type=float, default=0.8,
	help="minimum probability to filter weak detections, defaults at 0.8")
args = vars(ap.parse_args())

print("<loading detection model>")
detectM = cv2.dnn.readNetFromCaffe(args["prototxt"], args["detect"])
print("<loading classification model>")
classifyM = models.load_model(args["classify"])

print("<starting video stream and camera warmup>")
vs = VideoStream(src=0).start()
time.sleep(2.0)

while True:
    frame = vs.read()

    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,
		(300, 300), (104.0, 177.0, 123.0))
 
    detectM.setInput(blob)
    detections = detectM.forward()

	# loop over all detections
    for i in range(0, detections.shape[2]):
		# extract the probability for faces in frame(confidence)
        confidence = detections[0, 0, i, 2]

        if confidence < args["confidence"]:
            continue

        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")
        face = frame[int(startY):int(endY), int(startX):int(endX)]
        (fH, fW) = face.shape[:2]
        if fW > 40 and fH > 40:
            face = cv2.resize(face, (150,150))
            face = np.expand_dims(face, axis = 0)
            prediction = classifyM.predict(face)
            emotion = np.argmax(prediction[0])
            if emotion == 0:
                text = 'Happy'
            elif emotion == 1:
                text = 'Neutral'
            else:
                text = 'Sad'
    		# draw the bounding box of the face along with the associated
    		# probability
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