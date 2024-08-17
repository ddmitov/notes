sudo apt install build-essential
sudo ./VBoxLinuxAdditions.run

sudo apt -y upgrade && sudo apt clean && sudo apt -y autoremove

sudo usermod -a -G vboxsf `whoami`
sudo chown -R `whoami` /media/linux-shared/
sudo chmod -R 777 /media/linux-shared/
