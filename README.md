# Emotion-detection
Real-time face and emotion detection

This is a partial result of one part of the implementations made during a bachelor thesis work in face and emotion detection done between August 2018 through January 2019.
Simply clone or download and choose the way you want to run the detection. There are two ways instructed below.

# Instructions
Check the README.txt for full installation instructions. The easiest way to run is to follow the given instructions and not
manipulate the original folder structure. There are currently three scripts with different purposes. You can either run face detection for multiple faces in video footage or run emotion detection for either webcamera or your own input video. Please see instructions in the README.txt for further info.

# Examples of face detection and emotion detection
<img src="Example_Images/classify_happy.png" width="400" height="260"><img src="Example_Images/classify_neutral.png" width="400" height="260">
<img src="Example_Images/classify_sad.png" width="400" height="260">

<img src="Example_Images/haar_detection.png" width="400" height="260"><img src="Example_Images/resNet_detection.png" width="400" height="260">

# Other info

The model is implemented with Keras using tensorflow backend, see the image in the Classification_model subfolder for more reference
on each layer included. There is another repository using the same CNN model as a feature extractor and then training machine learning
models on these features that will be put up in a week.

