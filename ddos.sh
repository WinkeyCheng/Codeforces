sudo apt update
sleep 5
sudo apt install software-properties-common
sleep 3
sudo add-apt-repository ppa:deadsnakes/ppa
sleep 3
sudo apt update
git clone https://github.com/MHProDev/MHDDoS.git
sleep 5
pip install -r ~/MHDDoS/requirements.txt
