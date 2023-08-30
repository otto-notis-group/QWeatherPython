printf "运行此脚本需使用Python，如您没有安装Python，请在shell中输入下面的命令来下载。"
printf "sudo apt install python3.11"
printf "如果您已经拥有Python或您成功安装了Python请继续"
pause
sudo pip install -r requirements.txt
mv startbatinside 启动程序.sh
start 启动程序.sh
rm 首次运行程序.bat
rm 首次运行程序.sh
