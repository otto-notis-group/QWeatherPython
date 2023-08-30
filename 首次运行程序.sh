@echo off
printf "运行此脚本需使用Python，如您没有安装Python，请在浏览器中输入下面的链接来下载。"
printf "https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe"
printf "下载完成后安装即可。如果您不知道如何安装，请参考下面的文章。"
printf "https://zhuanlan.zhihu.com/p/641659306"
printf "如果您已经拥有Python或您成功安装了Python请继续"
pause
sudo pip install -r requirements.txt
mv startbatinside 启动程序.command
start 启动程序.comand
rm 首次运行程序.bat
rm 首次运行程序.comand
