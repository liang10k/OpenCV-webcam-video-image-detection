For YOLO + OpenCV method
======
Requirements:  
***Tensorflow and OpenCV***  
1. download Darkflow repository: https://github.com/thtrieu/darkflow unzip the files to a directory you like  
2. build the `darkflow` as an usable library:   
        *open a command prompt **-->**  
        *cd to the `darkflow-master` directory(e.g. D:\darkflow-master>) **-->**  
        *type `pip install -e .` or you can use `python setup.py build_ext --inplace`(Unfortunately the second command didn't work for me)  
3. download weights file or build your own weights file:  
  *Yolov2 608x608.weights file: https://pjreddie.com/media/files/yolov2.weights (You can try other weighs as well)  
  *put the weights file into `D:\darkflow-master\bin`, you need creat the **bin** folder. The folder name doesn't matter.  
  
