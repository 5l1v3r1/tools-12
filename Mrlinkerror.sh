echo "\033[34;1m Selamat Datang di Tool Mrlinkerrorsystem"
sleep 5
echo "\033[35;1m Anda disini dapat menginstall berbagai tools" | lolcat
sleep 2
echo "\033[36;1m Tetapi tool ini masih beta jadinya masih akan dikembangin lagi" | lolcat
sleep 3
echo "\033[31;1m:)  Semoga Bermanfaat  (:"
sleep 2
clear


echo "[01] LiteDDos untuk website" | lolcat
echo "[02] Lazymux" | lolcat
echo "[03] webdav" | lolcat
echo "[04] HackFb" | lolcat
echo "[05] Litespam untuk spam sms" | lolcat
echo "[06] Hammer untuk ddos website" | lolcat
echo "[07] Red_Hawk untuk scan website" | lolcat
echo "[08] Install WPScan" | lolcat
echo "[09] install sqlscan" | lolcat
echo "[10] Install sqlmap" | lolcat

echo "\033[35;1m Silahkan pilih yang mau anda install"

read -p "#Mrlinkerrorsystem ~>#" pilihan


if [ $pilihan = "01" ] || [ $pilihan = "1" ]
then
apt update
apt upgrade
pkg install git
pkg install python2
git clone https://github.com/4L13199/LITEDDOS
cd LITEDDOS
python2 liteDDOS.py
fi

if [ $pilihan = "02" ] || [ $pilihan = "2" ]
then
apt update && apt upgrade
apt install git
git clone https://github.com/Gameye98/Lazymux
cd Lazymux
ls
python2 lazymux.py
fi

if [ $pilihan = "04" ] || [ $pilihan = "4" ]
then
apt update && apt upgrade
pkg install python2 git
pip2 install mechanize
git clone https://github.com/pirmansx/mbf
ls
cd mbf
python2 MBF.py
fi

if [ $pilihan = "03" ] || [ $pilihan = "3" ]
then
apt update && upgrade
 apt install python2
 pip2 install urllib3 chardet certifi idna requests
 apt install openssl curl
 pkg install libcurl
ln -s /sdcard
 cd sdcard
 mkdir webdav
 cd webdav
 curl -k -O https://pastebin.com/raw/HnVyQPtR
mv HnVyQPtR webdav.py
python2 webdav.py
cd
cd /sdcard/webdav
python2 webdav.py
fi

if [ $pilihan = "05" ] || [ $pilihan = "05" ]
then
apt update
apt upgrade
pkg install toilet
pkg install php
pkg install git
git clone https://github.com/4L13199/LITESPAM
cd LITESPAM
sh LITESPAM.sh
fi

if [ $pilihan = "06" ] || [ $pilihan = "6" ]
then
pkg update
pkg upgrade
pkg install python
pkg install git
git clone https://github.com/cyweb/hammer
cd hammer
python hammer.py
fi 

if [ $pilihan = "07" ] || [ $pilihan = "7" ]
then
apt update && apt upgrade
apt install git 
apt install php
apt install php-curl
apt install php-xml
git clone https://github.com/Tuhinshubhra/RED_HAWK
cd RED_HAWK
php rhawk.php
fi

if [ $pilihan = "08" ] || [ $pilihan = "8" ]
then
apt update && apt upgrade
apt install git
apt install ruby
git clone https://github.com/wpscanteam/wpscan/
cd wpscan
chmod 777 wpscan.rb
gem install bundle
bundle install -j5
ruby wpscan.rb
fi

if [ $pilihan = "09" ] || [ $pilihan = "9" ]
then
pkg install php
pkg install git
git clone http://www.github.com/Cvar1984/sqlscan.git
cd sqlscan
chmod +x sqlscan.php
php sqlscan.php
fi

if [ $pilihan = "10" ] || [ $pilihan = "10" ]
then
apt update
apt upgrade
apt install python
apt install python2
apt install git
git clone https://github.com/sqlmapproject/sqlmap.git
cd sqlmap
python2 sqlmap.py
fi

