# A CNN based image classifier for walking surface identification.

This repository contains a simple script to train a TensorFlow Lite image classifier based on MobileNetV2 and an iOS application to host that model for real-time walking surface classification.

# MotionTerrain Scripts and Code

## Description

Each project or script available in subdirectories of this directory contains its own README file, explaining usage.

Alphabetically:

1) `motionterrain_classifier_app_ios`. An image classification application for iOS based on the TensorFlow Lite example application. When built, this application copies and uses the TensorFlow Lite model named `motionterrain_simple.tflite`. This project uses CocoaPods, so don't forget to run `pod install` in that directory prior to opening the XCode file.


2) `train.py`. A surprisingly simple script that, in just a few lines of code, trains a TensorFlow Lite model from the [L-AVATeD database](https://github.com/davewhipps/l-avated) (which must have been downloaded separately). The resulting .tflite model is written into `motionterrain_simple.tflite`.


## Authors

David Whipps


## License

This project is licensed under the [Creative Commons License](https://creativecommons.org/licenses/by/4.0/)