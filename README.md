# 一个简单的简谱转调程序

利用课余时间制作的一个简谱转调工具

根据转调的定义后，移动的Do的位置

用户的输入都是各自调的1,2,3,4...... 程序做的是移动他们输入调的Do到目标调上。

## 核心文件

[StartWindows.py](https://github.com/dccif/TuneChange/blob/master/StartWindow.py)

[GUI.py](https://github.com/dccif/TuneChange/blob/master/GUI.py)

~~[setup.py](https://github.com/dccif/TuneChange/blob/master/setup.py)为打包文件~~

## ~~TODO~~ 

我也不知道什么时候能实现的天坑

- 实现OCR读谱
- 利用多线程实时转换

## Release Notes

1.0.1.0 (2017-11-26)

- 优化正则

1.0.0.1 (2017-11-26)

- 添加输入判断
- 使用正则验证输入
- 更换Windows下的打包文件
- 添加图标和版本信息

1.0.0.0 (2017-08-07)

- 实现基本功能
- 使用[wxPython](https://www.wxpython.org/)实现GUI