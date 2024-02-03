#!/bin/bash

apt update&&apt upgrade -y  #アップデート
apt install -y git         #gitインストール
#拡張機能インストール

code --install-extension ms-python.python  
             
#code --install-extension KevinRose.vsc-python-indent    #Pythonのインデントを調整  
# code --install-extension MS-vsliveshare.vsliveshare   #リアルタイム共同作業
# code --install-extension pkief.material-icon-theme    #アイコンテーマ
# code --install-extension VisualStudioExptTeam.vscodeintellicode #AI補完

