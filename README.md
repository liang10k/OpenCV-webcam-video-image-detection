# OpenCV-webcam-video
 
The origin files come from Tensorflow models:  
https://github.com/tensorflow/models/tree/master/research/object_detection  
You need download this and put "webcam_detection.py" into this directory

---
***You may need install Tensorflow***

For CPU  
`pip install tensorflow`  
For GPU  
`pip install tensorflow-gpu`

---

***Protobuf Compilation***  
download protobuf 3.4.0 https://github.com/google/protobuf/releases/tag/v3.4.0  
I tried version 3.5.0 of protobuf on Windows but it didn't work on me.  
unzip the file, find "bin" open it, copy the "protoc.exe" into the "tensorflow/models/tree/master/research/object_detection" directory  
open command prompt-->go to the directory where you put "tensorflow/models/.../research/object_detection"-->  
type: `protoc object_detection/protos/*.proto --python_out=.` this will compile all the .proto files in the protos folder  

---
Then you can run the "webcam_detection.py"
