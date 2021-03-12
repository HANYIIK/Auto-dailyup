# 西安电子科技大学(包含广州研究院)晨午晚检自动填报工具
本代码来自 [/jiang-du/Auto-dailyup.git](https://github.com/jiang-du/Auto-dailyup.git) 的作品，在此基础上增加了`广州研究院`的填报位置信息。<br>
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
python index.py
```
然后根据提示输入学号、位置、密码即可，第一次登录成功后无需再次输入密码。<br>
如果后期更改了密码，建议删除`data/cookie.inf`文件，重新运行。<br>
###### 特别提醒：Mac系统第一次登录后无法实现清屏功能，为防止明文密码暴露，建议`Ctrl+C`停止一下，再重新`python index.py`即可隐藏密码。
