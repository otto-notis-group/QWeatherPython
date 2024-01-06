echo off
chcp 65001
echo 运行此脚本需使用Python，如您没有安装Python，请在浏览器中输入下面的链接来下载。
echo https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe
echo 下载完成后安装即可。如果您不知道如何安装，请参考下面的文章。
echo https://zhuanlan.zhihu.com/p/641659306
echo 如果您已经拥有Python或您成功安装了Python请继续
pause
pip install -r requirements.txt
rename startbatinside 启动程序.bat
start 启动程序.bat
del /f /q 首次运行程序.bat
