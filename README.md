# Detect Ankylosing Spondylitis using Deep Learning Framework
Draw bounding box on sacroiliac joint and classify ankylosing spondylitis.

If you want to know more about how to use the tensorflow object detection API, check out [API_tutorial(EN)](API_tutorial.md) or [API_tutorial_KOR(KOR)](API_tutorial_KOR.md)

## Introduction
* Ankylosing Spondylitis(AS)

* sacroiliac join(SIJ)

## Dataset
* n X-ray images(n normal, m positive)
* train: , test: , stratified(proportion of two classes was maintained).
* example(??)

## Method
* preprocessing \
: Resized to 1024X1024 maintaining aspect ratio.

* model \
: EfficientDet-D4 1024X1024, pre-trained on COCO 2017 dataset([link](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md))

* hyperparameter (for detailed info, check out [pipeline.config](models/efficientdet_d4_coco17_tpu-32/pipeline.config)) \
-batch size: 4 \
-learning_rate_base: 0.003999999821186066 \
-warmup_learning_rate: 0.000010000000474974513 \
-warmup_steps: 2500 \
-total_steps: 20000

* augmentation \
: random horizontal flip and random scale cropping was applied

## Results
* Confusion Matrix

* Classification Report

* COCO MAP score


## Reference
