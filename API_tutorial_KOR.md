# Tensorflow object detection API with custom dataset
Object detection on custom dataset using TFOD API

For English version, check out [README.md](/README.md)

이 프로젝트는 tensorflow object detection api의 공식 documentation과 tutorial을 활용하여 진행되었습니다. 

저 역시 초보자로써 많은 시행착오를 겪었던만큼, 초보자 분들의 눈높이에 맞추어 작성하려고 노력하였습니다!:relaxed:

-공식 document link: https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/ \
-tutorial link: https://github.com/tensorflow/models/tree/master/research/object_detection/

## System information
- __OS Platform and Ditribution:__ Ubuntu 18.04 
- __CUDA:__ 10.1*  
- __CuDNN:__ 7.6.5* 
- __Tensorflow Version:__ 1.14(api가 tf1만을 지원하던 시절) -> 2.2 -> 2.3 
  (마지막에 2.3으로 upgrade하였는데, 2.2를 사용하셔도 무방합니다.) \
- __Python Version:__ 3.8? 
- __GPU model:__ Titan RTX ?GB

*CUDA version과 CuDNN version은 공식 document에서 제안하는 version을 설치하였습니다.

## Installation
API documentation에 나온 것을 그대로 따라하였고, anaconda 가상환경을 만들어 설치하였습니다. \

설치 과정 중에는 별다른 에러를 경험하지 못했습니다.

## Process
각 과정에 대한 보다 자세한 설명은 공식 [documentation](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/training.html)을 참고하여주세요.

만약 anaconda의 가상환경에서 진행할 경우, \
시작 전에 `conda activate tensorflow(또는 가상환경이름)` 로  반드시! 가상환경을 불러와야합니다.

### 1) workspace 구축
저는 다음과 같이 폴더를 만들었습니다.(Documentation과 거의 유사합니다.)
```
TensorFlow/
├─ models/(API를 git clone)
│  ├─ community/
│  ├─ official/
│  └─ ...
├─ scripts/ (프로젝트에 사용한 모든 코드파일)
│  └─ preprocessing/ (preprocessing에 사용한 코드파일)
└─ workspace/
   └─ training_demo/
```

```
training_demo/
├─ annotations/ (csv파일, label_map파일, tfrecord파일)
├─ exported-models/ (training이 완료된 모델을 저장)
├─ images/
│  ├─ test/
│  └─ train/
├─ models/ (training에 사용할 모델+trainig과정 중 생성되는 파일들)
└─ pre-trained-models/ (pre-train된 raw 모델)
```


### 2) Dataset 준비
0. 정답 박스 그리기(annotation 작업) 
-> 저는 ImageJ라는 tool을 사용하였고, 모든 annotation의 정보를 하나의 `csv`파일에 모았습니다. \
Documentation의 경우 이미지 한 장당 하나의 `xml`파일을 만들어 저장하고 있습니다.

1. train set과 test set으로 분류
-> 저는 `scripts/train_test_split`와 같이 구현하였습니다. \
여기서는 1) train과 test set을 나누어, 2) 해당되는 이미지를 train폴더와 test폴더에 담고, 3) annotation정보도 train과 test에 맞게 따로 생성해주는 작업을 해야합니다.

2. label_map.txt 파일 생성
각 label을 다음과 같은 형식으로 적어 `.pbtxt`로 저장합니다.
* 예시
```
item {
    id: 1
    name: 'cat'
}

item {
    id: 2
    name: 'dog'
}
```

2. tfrecord 파일 생성 
-> 저는 `scripts/preprocessing/build_ankylosing_records_tf2.py`와 같이 구현하였습니다. \
터미널 실행코드는 아래와 같습니다.
```
python ./preprocessing/build_ankylosing_records_tf2.py --csv_dir [PATH_TO_MODEL_DIR]train.csv --labels_path [PATH_TO_ANNOTATION_FOLDER]label_map.pbtxt" --output_path [PATH_TO_ANNOTATION_FOLDER]train.record --image_dir [PATH_TO_IMAGES_FOLDER]train/
```

### 3) Configure
1. Pre-Trained Model 다운받기 \

[링크](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md)에서 원하는 모델을 다운로드하신 뒤, 압축해제후 `pre-trained-models`폴더에 저장하시면 됩니다.
-> 저는 EfficientDet-d4를 사용하였습니다. \
(EfficientDet-d6에서 OOM이 발생하여 d4로 낮추었는데 결과가 괜찮아 d5는 시도해보지 않았습니다.)

2. `pipeline.config` 파일 변형.
`pre-trained-models/모델명`에 있는 pipeline.config파일을 `models/모델명`으로 복사합니다.
이 파일 내에 preprocessing부터 hyperparameter와 그 외 각종 정보들이 들어있는데요,
이 값을 입맛에 맞게 바꾸시면 됩니다.(기본 수정사항은 documentation에 나와있습니다.)
-> 제가 training에 사용한 config파일은 [여기](/models/efficientdet_d4_coco17_tpu-32/pipeline.config)에서 확안하실 수 있습니다

### 4) Training
1. model training하기
`model_main_tf2.py`를 이용해 모델을 train합니다.
터미널에는 model경로(`--model_dir`)와 `pipeline.config`파일(`--pipeline_config_path`)의 경로를 넣습니다.

2. tensorboard check하기
tensorboard에서 training loss를 확인합니다.

3. training이 완료된 모델 export하기 
`exporter_main_v2.py`를 이용해 training이 끝난 모델을 `.pb`파일로 저장합니다.

### 5) Evaluation
-> evaluation은 documentation에서 나와있는 방식이 아닌, jupyter notebook tutorial을 조금 변형하여 작업하였습니다. \
API 측에서 terminal에서 돌릴 경우 box에 대한 metric(ex. COCO MAP score)만 볼 수 있도록 지원하고 있는데, 저희 프로젝트의 경우에는 각 이미지의 classification 결과가 필요했기 때문이었습니다.

따라서 앞서 export한 `.pb`형식의 model파일을 이용해 evaluation을 진행하였습니다.

이에 대한 코드는 `scripts/inference_using_saved_model.ipynb` 에서 확인하실 수 있습니다.

* 유의사항 \
앞서 anaconda 가상환경에 api를 설치하였기 때문에, evaluation을 할 때도 `conda activate tensorflow(또는 가상환경이름)`를 해주어야합니다. \
그런데 저의 경우 가상환경을 불러왔음에도 `anaconda-navigator` 를 통해 .pynb파일을 열면 api를 import하지 못하더군요. \
그래서 tenminal에서 `cd TensorFlow` 를 해준 뒤, `jupyter notebook` 커맨드를 통해 쥬피터 노트북에 들어가 파일을 실행하는 방식을 사용하였습니다. 


## Error log
API를 사용하면서 엄청나게 많은 에러를 경험하였는데, 추후 도움이 될까 싶어 에러 내용과 해결방법을 따로 기록해두었습니다! \

행여나 error가 발생하셨다면 저의 [error_log](/error_log.md)를 참고해보세요.

error 해결에 가장 많은 도움을 얻었던 사이트는 Stackoverflow와 api의 공식 github repository의 [issue탭](https://github.com/tensorflow/models/issues)이었습니다.
