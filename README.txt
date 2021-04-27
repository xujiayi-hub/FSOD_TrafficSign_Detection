环境配置参考：https://github.com/facebookresearch/maskrcnn-benchmark/blob/master/INSTALL.md
额外需要的安装依赖项：
pip install pyqt5

更改配置文件config/caffe2/e2e_mask_rcnn_R_50_FPN_1x_caffe2.yaml
其中weight："****"更改为"当前项目路径*/newmodel/mode***"

运行方式：
python MPSR\demo2\demo\test2.py
https://github.com/xujiayi-hub/Sign-Detection-FSOD-.git