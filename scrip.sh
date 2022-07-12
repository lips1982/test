#!/bin/sh
while getopts k:a: option
do 
    case "${option}"
        in
        k)key=${OPTARG};;
        a)accname=${OPTARG};;
    esac
done

echo "KEY_ACCES : $key"
echo "ACC_NAME  : $accname"
echo "INICIANDO"

 
pip3 install pymongo
apt update python3.10
sudo apt update
sudo apt -y upgrade
wget -P ~/Downloads/ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i ~/Downloads/google-chrome*.deb
wget https://chromedriver.storage.googleapis.com/102.0.5005.61/chromedriver_linux64.zip
unzip chromedriver_linux64

sudo mv chromedriver /usr/local/share/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver

pip3 install selenium
pip3 install webdriver-manager
pip3 install pymongo
pip3 install "pymongo[srv]"
pip3 freeze
whereis chromedriver
whereis google-chrome

git clone https://github.com/lips1982/test.git #cambiar cuando este completamente desarrollado
cd test
sed -i "s|REEMPLAZARKEY_ACCESS|${key}|g" mainStart.py
sed -i "s|REEMPLAZARACCNAME|${accname}|g" mainStart.py
ls
echo "SCRIP FINALIZANDO--- LANZANDO PYTHON ----"
exit
