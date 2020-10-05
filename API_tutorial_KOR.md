# Tensorflow object detection API with custom dataset
Object detection on custom dataset using TFOD API

For English version, check out [README.md](/README.md)

이 프로젝트는 tensorflow object detection api의 공식 documentation과 tutorial을 활용하여 진행되었습니다. 

저 역시 초보자로써 많은 시행착오를 겪었던만큼, 초보자 분들의 눈높이에 맞추어 작성하려고 노력하였습니다!:relaxed:

-공식 document link: https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/ \
-tutorial link: https://github.com/tensorflow/models/tree/master/research/object_detection/

## Basic Settings
__OS Platform and Ditribution:__ Ubuntu 18.04 \
__CUDA:__ 10.1* \
__CuDNN:__ 7.6.5* \ 
__Tensorflow Version:__ 1.14(api가 tf1만을 지원하던 시절) -> 2.2 -> 2.3 \
__Python Version:__ 3.8? \
__GPU model:__ Titan RTX ?GB
(마지막에 2.3으로 upgrade하였는데, 2.2를 사용하셔도 무방합니다.)

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
1. Pre-Trained Model 다운받기 \

[링크](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md)에서 원하는 모델을 다운로드하시면 됩니다.
-> 저는 EfficientDet-d4를 사용하였습니다. \
(EfficientDet-d6에서 OOM이 발생하여 d4로 낮추었는데 결과가 괜찮아 d5는 시도해보지 않았습니다.)

2. `pipeline.config` 파일 변형.

이 파일 내에 preprocessing부터 hyperparameter와 그 외 각종 정보들이 들어있는데요,
이 값을 입맛에 맞게 바꾸시면 됩니다.(기본 수정사항은 documentation에 나와있습니다.)
-> 제가 training에 사용한 config파일은 [여기]()에서 확안하실 수 있습니다

### 4) Training
- tensorboard check하기
- 
### 5) Evaluation


## Performance

## Error log
API를 사용하면서 엄청나게 많은 에러를 경험하였는데, 추후 도움이 될까 싶어 에러 내용과 해결방법을 따로 기록해두었습니다! \

행여나 error가 발생하셨다면 저의 [error_log](/error_log.md)를 참고해보세요.

error 해결에 가장 많은 도움을 얻었던 사이트는 Stackoverflow와 api의 공식 github repository의 [issue탭](https://github.com/tensorflow/models/issues)이었습니다.
