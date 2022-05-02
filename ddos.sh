sudo apt update
sleep 5s
sudo apt install software-properties-common
sleep 3s
sudo add-apt-repository ppa:deadsnakes/ppa
sleep 3s
sudo apt update
git clone https://github.com/MHProDev/MHDDoS.git
sleep 5s
pip install -r ~/MHDDoS/requirements.txt
