## tf1 버전만을 지원하는 동안 발생한 문제

### 05.09
~~* pycoco, pycocotools를 둘러싼 문제들 (또는 어떤 모듈이 존재하지 않는다 등등) \
: 공식 github에 설치 설명이 linux와 mac 버전으로만 나와있어 발생하는 오류다.~~
-> tf2 버전 지원과 함께 공식 documentation에 windows 환경에 맞는 설치법이 나와있다!

* dicom image를 사용하면서 발생한 문제들 \
1) by, bx, width, height 값이 pixel단위가 아닌 mm단위로 저장되었다.(심지어 파일마다 변환시에 곱해지는 수가 다른다.)
-> imageJ 내의 메크로를 이용해 pixel per mm 값을 얻을 수 있다. pixel per mm 값을 저장하고 csv에서 함수를 이용해 mm을 pixel로 바꿔주어 해결하였다.

2) `main_model.py`(tf2버전의 `model_main_tf2.py`)를 돌리면서 발생한 오류
```Unable to decode bytes as JPEG, PNG, GIF, or BMP```
초반에 dicom으로 training을 시키려고 해서 발생한 오류였다. \
dicom파일을 읽어와 numpy 또는 bytes로 변환하도록 하여도 같은 오류가 발생. \
-> 간단하게 dicom을 jpg로 변환하면 된다! (micro dicom viewer라는 프로그램이 매우 편리합니다.)

* tensorboard를 불러오는 문제에서 발생한 오류 (windows 환경에서)
->시도1: terminal에 `--host=localhost` 추가 => 실패
->시도2: 주소입력시 https대신 http로 한다 => 실패
->시도3: terminal에 `--host=localhost --port=8008`추가 => 성공

* ```numpy.float64 object cannot be interpreted as integer```
-> numpy version을 1.17.4로 downgrade

* training 과정 중 발생한 문재들
```uft8 can't decode byte ...```
-> .config 파일에 경로부분에 오타가 있었다.

```module nets doesn't exists```
:PYTHONPATH가 지정되어있지 않아서 생기는 문제였다.
-> `nano ~/.bashrc`에서 경로 추가해 해결.

* `killed`
:메모리 부족 문제. 알고보니 GPU가 사용되고 있지 않았다.

* ```OOM when allocating tensor with shape[,,] and type int32 on ...```
:메모리 부족 문제. gpu메모리가 부족한 것이다.
-> 

## tf2 버전 지원 이후 발생한 문제


```
/home/user/TensorFlow/workspace/training_AS/images/test/10638946_2621_0.jpg
/home/user/TensorFlow/workspace/training_AS/images/test/10638946_2621_0.jpg
2 root error(s) found.
  (0) Invalid argument:  Incompatible shapes: [1,1025,1024] vs. [1,1,3]
	 [[{{node StatefulPartitionedCall/Preprocessor/sub}}]]
	 [[StatefulPartitionedCall/Postprocessor/BatchMultiClassNonMaxSuppression/MultiClassNonMaxSuppression/Reshape_1/_88]]
  (1) Invalid argument:  Incompatible shapes: [1,1025,1024] vs. [1,1,3]
	 [[{{node StatefulPartitionedCall/Preprocessor/sub}}]]
0 successful operations.
0 derived errors ignored. [Op:__inference_signature_wrapper_47342]

Function call stack:
signature_wrapper -> signature_wrapper
```
