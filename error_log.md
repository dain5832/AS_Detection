## tf1 버전만을 지원하는 동안 발생한 문제

### Windows에서 pycoco, pycocotools를 둘러싼 문제들 (또는 어떤 모듈이 존재하지 않는다 등등)
~~: 공식 github에 설치 설명이 linux와 mac 버전으로만 나와있어 발생하는 오류다.~~ \
-> tf2 버전 지원과 함께 공식 documentation에 windows 환경에 맞는 설치법이 나와있다!



###  dicom 형식을 사용하면서 발생한 문제들 
#### by, bx, width, height 값이 pixel단위가 아닌 mm단위로 저장되었다.(심지어 파일마다 변환시에 곱해지는 수가 다르다.) 
-> imageJ 내의 메크로를 이용해 pixel per mm 값을 얻을 수 있다. pixel per mm 값을 저장하고 csv에서 함수를 이용해 mm을 pixel로 바꿔주어 해결하였다.


#### `main_model.py`(tf2버전의 `model_main_tf2.py`)를 돌리면서 발생한 오류
```Unable to decode bytes as JPEG, PNG, GIF, or BMP``` \
초반에 dicom으로 training을 시키려고 해서 발생한 오류였다. \
dicom파일을 읽어와 numpy 또는 bytes로 변환하도록 하여도 같은 오류가 발생. \
-> 간단하게 dicom을 jpg로 변환하면 된다! (micro dicom viewer라는 프로그램이 매우 편리합니다.)



### tensorboard를 불러오는 문제에서 발생한 오류 (windows 환경에서)
->시도1: terminal에 `--host=localhost` 추가 => 실패 \
->시도2: 주소입력시 https대신 http로 한다 => 실패 \
->시도3: terminal에 `--host=localhost --port=8008`추가 => 성공



### training 과정 중 발생한 문제들
* ```numpy.float64 object cannot be interpreted as integer``` \
-> numpy version을 1.17.4로 downgrade

* ```uft8 can't decode byte ...``` \
-> .config 파일에 경로부분에 오타가 있었다.

* ```module nets doesn't exists``` \
:PYTHONPATH가 지정되어있지 않아서 생기는 문제였다. \
-> `nano ~/.bashrc`에서 경로 추가해 해결.




### 메모리 부족문제
* `killed` \
:알고보니 GPU가 사용되고 있지 않았다.

* ```OOM when allocating tensor with shape[,,] and type int32 on ...``` \
:gpu메모리 부족. \
-> 시도1: `batch_size` 줄이기 => 이미 batch_size가 1로 지정되어있었음. \
-> 시도2: `config` 파일의 `keep_aspect_ratio_image_resizer` 값 낮추기 => 실패 \
-> 시도3: `per_process_gpu_memory_fraction=0.7`, `gpu_options.allow_growth=True` 등등 tensorflow로 하여금 gpu memory를 조금씩 먹도록 하는 코드들 추가 => 실패 \
==> 결국 해결이 안돼서 detectron2를 사용하다 tf2 버전을 지원한다는 소식을 듣고 다시 넘어왔다.




## tf2 버전 지원 이후 발생한 문제
### loss가 nan인 경우
: training loss가 explode해서 생기는 문제. \
-> `learning_rate`을 줄이면 됨. (만약 `batch_size`를 줄였다면 `learning_rate`도 비슷한 비율로 줄일 것.) \
-> `efficientdet`의 경우 raw `pipline.config` 파일에서 `batch_size`가 128이었던 것으로 기억하는데, 이것을 4로 줄이면서 loss가 nan이 나왔다.




### tensorboard 불러오는 도중 생긴 문제
```No such file or directory: 'home/user/anaconda3/envs/tensorflow/lib/python3.8/site-packages/numpy-1.19.1.dist-info/METADATA'```
-> 해당 폴더 (`numpy-1.19.1.dist-info`)를 삭제. \
(만약 삭제 후 `site-packages`안에 `numpy`라는 이름 폴더가 따로 존재하지 않는다면 `conda`나 `pip`을 이용해서 새로 설치해주어야한다.)




### evaluation에서 발생한 문제
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
-> shape이 맞지 않아 생기는 오류인 것 같은데 정확한 원인은 파악하지 못함. 이미지를 수동으로 resize해준 뒤에 넣어 해결.



### 기타 error
error message를 따로 기록하지는 않았지만, 보통 error의 대부분은 `.config`파일에 오타가 있었거나 GPU 메모리 부족인 경우였습니다.
