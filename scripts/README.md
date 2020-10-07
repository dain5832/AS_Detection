# Scripts Description
이 문서는 scripts 폴더 내의 각 파일에 대한 정보를 담고 있습니다.

## train_test_split.ipynb
training 전, 전체 이미지를 train_set과 test_set으로 나누는 작업을 진행하는 코드입니다.
* 과정 \
train/test나누기 -> train/test 폴더에 이미지 복사 -> annotation 정보를 담은 train.csv와 test.csv 생성 으로 구성되어 있습니다.
* documentation에서는 annotation 정보가 이미지 1장당 xml파일로 존재한다는 가정하에 코드를 제공하고 있는데, \
저의 경우 전체 annotation 정보가 하나의 csv 파일에 들어있어 그에 맞는 코드를 따로 만들었습니다.

## create_test_train_csv.ipynb
`train_test_split.ipynb` 코드 중 annotation 정보를 담은 csv 파일을 생성하는 과정만을 담은 코드입니다. 

## inference_using_checkpoints.ipynb
api에서는 training을 할 때 일정 step마다 checkpoint file을 생성합니다.(default 값은 1000입니다.) \
그 때 생성된 checkpoint file(.ckpt)을 이용하여 evaluation을 할 수 있도록 하는 코드입니다. 
* 각 이미지에 대한 결과와 함께, classification report와 classification matrix를 볼 수 있습니다.

## inference_using_saved_model.ipynb
training이 완료된 model을 export하면 `.pb` 형식으로 저장이 됩니다. \
`.pb` 파일의 경우 모델의 graph를 포함한 모든 변수에 대한 정보를 담고 있어 곧바로 evaluation에 사용할 수 있습니다. \
(더욱 자세한 설명은 [여기]()를 참고하세요.) \
`.pb` 파일을 불러와 evaluation을 할 수 있도록 하는 코드입니다. 
* 각 이미지에 대한 결과와 함께, classification report와 classification matrix를 볼 수 있습니다.

## inference_using_saved_models.ipynb
for loop를 통해 `saved_models` 폴더에 있는 여러 모델(.pb 파일)을 불러와 evaluation을 하는 코드입니다. \
(위의 `inference_using_saved_model.ipynb` 를 반복한다고 생각하시면 됩니다.)

## repeat_whole_training_process
train_test_split의 random_state를 달리하여 training의 처음부터 끝까지를 여러번 반복하는 코드입니다. 
