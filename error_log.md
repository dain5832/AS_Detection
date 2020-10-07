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
