# install ssh server
sudo apt-get install openssh-server -y

# install sshpass utility
sudo apt-get install sshpass -y

# enable ssh server
sudo systemctl start ssh
