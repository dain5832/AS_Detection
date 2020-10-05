# Detect Ankylosing Spondylitis using Deep Learning Framework
Draw bounding box on sacroiliac joint and classify ankylosing spondylitis.

If you want to know more about how to use the tensorflow object detection API, check out [API_tutorial(EN)](API_tutorial.md) or [API_tutorial_KOR(KOR)](API_tutorial_KOR.md)

## Introduction
* Ankylosing Spondylitis(AS)

* Sacroiliac join(SIJ)

## Dataset
* n X-ray images(n normal, m positive)
* train: , test: , stratified(proportion of two classes was maintained).
* example(??)

## Method
* Preprocessing \
: Resized to 1024X1024 maintaining aspect ratio.

* Model \
: EfficientDet-D4 1024X1024, pre-trained on COCO 2017 dataset ([model_link](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md))

* Hyperparameter (for detailed info, check out [pipeline.config](models/efficientdet_d4_coco17_tpu-32/pipeline.config)) \
-batch size: 4 \
-learning_rate_base: 0.003999999821186066 \
-warmup_learning_rate: 0.000010000000474974513 \
-warmup_steps: 2500 \
-total_steps: 20000

* Augmentation \
: random horizontal flip and random scale cropping was applied

## Results
* training loss(Tensorboard)
![alt_text][tensorboard]

* Classification Report & Confusion Matrix
![alt text][confusion_matrix]

* COCO MAP score

[tensorboard]: exported-models/my_model_200925/model_200925_tensorboard.png 
[confusion_matrix]: exported-models/my_model_200925/Screenshot&#32;from&#32;2020-09-29&#32;17-07-49.png

## Reference
