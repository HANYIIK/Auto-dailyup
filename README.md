# 西安电子科技大学(包含广州研究院)晨午晚检自动填报工具
本代码来自 [jiang-du/Auto-dailyup.git](https://github.com/jiang-du/Auto-dailyup.git) 的作品，在此基础上增加了`广州研究院`的填报位置信息。<br>
感谢大佬们的无私奉献，本代码仅供学术交流。
### 使用方法如下：
Windows系统：
```
pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple
```
```
python index.py
```
Linux系统：
```
pip3 install requests -i https://pypi.tuna.tsinghua.edu.cn/simple
```
```
python3 index.py
```
然后根据提示输入学号、位置、密码，在后台挂着不管它就行了。<br>
第一次登录成功后无需再次输入密码，如果后期更改了密码，建议删除`data/cookie.inf`文件，重新运行即可。<br>
##### 特别提醒 1：Mac系统第一次登录后无法实现清屏功能，为防止明文密码暴露，建议`Ctrl+C`停止一下，再重新`python index.py`即可隐藏密码。
##### 特别提醒 2：位置信息建议选`4：美国加利福尼亚州洛杉矶`，可以感受一下被校领导关心的感觉。
##### 特别提醒 3：脚本记录的cookie数据每隔一段时间会失效，若是无法上报可通过删除`data`文件夹下的`cookie.inf`后重新登录来刷新。

### 运行截图：
![image](https://github.com/HANYIIK/Auto-dailyup/blob/main/images/1.jpg)
![image](https://github.com/HANYIIK/Auto-dailyup/blob/main/images/2.jpg)
#### 终端每天正常的输出结果：
![image](https://github.com/HANYIIK/Auto-dailyup/blob/main/images/3.jpg)
* ### 关于Linux和Mac用户如何实现眼不见心不烦：
如果觉得终端一直挂在那里很烦的话，建议安装一个后台分屏软件`screen`:
```
sudo apt-get install screen
```
安装好后进入screen模式：
```
screen
```
按回车确认，进入该`screen`后运行程序:
```
python index.py
```
按住`Ctrl`+`A`键后，再按一个`D`键，即可将该窗口`detach`掉，然后你就看不见它了。<br>
<br>关于如何唤醒这个`screen`:
```
screen -ls
```
找到该`screen`的`id`号 `xxxxx`后：
```
screen -r xxxxx
```
即可。
