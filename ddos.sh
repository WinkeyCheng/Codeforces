echo "Updating System Software..."
sudo apt update
sleep 3
sudo apt install software-properties-common
sleep 3
echo "Adding new APT repository..."
sudo add-apt-repository ppa:deadsnakes/ppa
sleep 3
echo "Executing software update..."
sudo apt update
echo "Cloning files..."
sudo -u noobaswinkey git clone https://github.com/MHProDev/MHDDoS.git
sleep 5
echo "Installing requirements..."
pip install -r ~/MHDDoS/requirements.txt
sleep 3
echo "Installation finished!"
