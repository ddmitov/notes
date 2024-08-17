sudo apt -y install docker.io

sudo usermod -aG docker $USER
sudo chown $USER /var/run/docker.sock
sudo service docker restart
