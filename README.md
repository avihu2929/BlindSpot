
Besides some of the default coco classes we have added scooters and crosswalks.
The crosswalk class was added with the help of the reposetory https://github.com/kairess/crosswalk-traffic-light-detection-yolov5
The scooter class was trained using a manually labeled dataset. 
We use TextToSpeech feature of android to speak the detected classes aloud for the user, We also calculate the postion of the detected object reltive to 
the screen and add it to the spoken line. ("Theres a scooter to your left").
(HelpMeSee/android/app/src/main/java/org/tensorflow/lite/examples/detection/tflite/YoloV5Classifier.java)

The final yolo model was trained on ~2000 images taken from the streets and labeled automatically using pretrained single class models (HelpMeSee/models/scooter.pt)
See also  HelpMeSee/labelcustomdata.py to label automatically your own classes.

(This project was made as final assignment for college)

Below you can find instructions on how to build an android app using https://github.com/zldrobit/yolov5.git

## Info
<del>This branch provides detection and Android code complement to branch `tf-only-export`.</del>
Since the release of YOLOv5 v6.0, TFLite models can be exported by `export.py` in ultralytics' master branch. Using `models/tf.py` to export models is deprecated, and this repo is mainly for Anrdroid demo app.
`models/tf.py` uses TF2 API to construct a tf.Keras model according to `*.yaml` config files and reads weights from `*.pt`, without using ONNX.

<del>**Because this branch persistently rebases to master branch of ultralytics/yolov5, use `git pull --rebase` or `git pull -f` instead of `git pull`.**</del>


## Usage
### 1. Git clone Ultralytics `yolov5`
```
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
```

### 2. Convert and verify
- Convert weights to fp16 TFLite model, and verify it with
```
python export.py --weights yolov5s.pt --include tflite --img 320
python detect.py --weights yolov5s-fp16.tflite --img 320
```
or 
- Convert weights to int8 TFLite model, and verify it with
```
python export.py --weights yolov5s.pt --include tflite --int8 --img 320 --data data/coco128.yaml
python detect.py --weights yolov5s-int8.tflite --img 320
```
Note that:
* int8 quantization needs dataset images to calibrate weights and activations, and the default COCO128 dataset is downloaded automatically.
* Change `--img` to the input resolution of your model, if it isn't 320. 

### 3. Clone this repo (tf-android branch) for Android app
```
git clone https://github.com/zldrobit/yolov5.git yolov5-android
```

### 4. Put TFLite models in `assets` folder of Android project, and change 
- `inputSize` to `--img`
- `output_width` according to new/old `inputSize` ratio
- `anchors` to `m.anchor_grid` as https://github.com/ultralytics/yolov5/pull/1127#issuecomment-714651073 
in android/app/src/main/java/org/tensorflow/lite/examples/detection/tflite/DetectorFactory.java
- `labelFilename` according to the classes of the model
in https://github.com/zldrobit/yolov5/blob/522d65e848d3e5a378eb0f29a9fbb204221400e8/android/app/src/main/java/org/tensorflow/lite/examples/detection/tflite/DetectorFactory.java#L19-L48. 

Then run the program in Android Studio.


