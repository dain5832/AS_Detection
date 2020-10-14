# Detect Ankylosing Spondylitis using Deep Learning Framework
Draw bounding box on sacroiliac joint and classify ankylosing spondylitis.

If you want to know more about how to use the tensorflow object detection API, check out [API_tutorial(EN)](API_tutorial.md) or [API_tutorial_KOR(KOR)](API_tutorial_KOR.md)

## Introduction
* Ankylosing Spondylitis(AS)

* Sacroiliac joint(SIJ)

## Dataset
* 946 X-ray images(normal: 468, positive: 478)
* train: 756, test: 190(최종 115장), stratified(proportions of two classes were maintained), random_state=42.
** test 과정에서 shape error로 75장 누락됨.(total 115, normal ?? positive??)

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
### Training Loss(Tensorboard)

![alt_text][tensorboard]

### Classification Report & Confusion Matrix

![alt text][confusion_matrix]

### COCO MAP score

### Example
- Negative
![alt text][negative]

-Positive
![alt text][positive]

-Half
![alt text][half]


[tensorboard]: exported-models/my_model_200925/model_200925_tensorboarddd.png 
[confusion_matrix]: exported-models/my_model_201014/confusion_matrix.png
[negative]: exported-models/my_model_201014/negative.png
[positive]: exported-models/my_model_201014/positive.png
[half]: exported-models/my_model_201014/index.png

## Reference
