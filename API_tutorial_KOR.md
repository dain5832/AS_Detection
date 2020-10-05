# Tensorflow object detection API with custom dataset
Object detection on custom dataset using TFOD API

For English version, check out [README.md](/README.md)

이 프로젝트는 tensorflow object detection api의 공식 documentation과 tutorial을 활용하여 진행되었습니다. 

저 역시 초보자로써 많은 시행착오를 겪었던만큼, 초보자 분들의 눈높이에 맞추어 작성하려고 노력하였습니다!:relaxed:

-공식 document link: https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/ \
-tutorial link: https://github.com/tensorflow/models/tree/master/research/object_detection/

## Basic Settings
```
__Environment:__ Ubuntu 18.04
__CUDA:__ 10.1*
__CuDNN:__ 7.6.5* 
__Tensorflow Version:__ 1.14(api가 tf1만을 지원하던 시절) -> 2.2 -> 2.3
(마지막에 2.3으로 upgrade하였는데, 2.2를 사용하셔도 무방합니다.)
```
*CUDA version과 CuDNN version은 공식 document에서 제안하는 version을 설치하였습니다.

* CUDA와 CuDNN version확인법 \
CUDA: terminal에서 nvcc --version 타입 후 엔터 \
CuDNN: ??

## Installation
API documentation에 나온 것을 그대로 따라하였고, anaconda 가상환경을 만들어 설치하였습니다. \
설치 과정 중에는 별다른 에러를 경험하지 못했습니다.

## Process
각 과정에 대한 보다 자세한 설명은 공식 [documentation](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/training.html)을 참고하여 주세요.

### 1) workspace 구축
'''

'''

### 2) Dataset 준비
X-ray영상 n장
class는 normal과 positive 2개였고, 각각 장과 장이었습니다.

### 3) Configure
[링크](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md)에서 원하는 모델을 다운로드합니다.

### 4) Training
- tensorboard check하기
- 
### 5) Evaluation


## Performance

## Error log
I recorded all the errors I faced while using api. Those error logs can be found here. \
Check out stackoverflow or issus tab in official git repositories when you face unknown error!
