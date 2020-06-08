sudo apt -y install build-essential libevent-dev libncurses5-dev

mkdir ~/tmux
cd ~/tmux
curl -LO https://github.com/tmux/tmux/releases/download/2.8/tmux-2.8.tar.gz
tar xfvz tmux-2.8.tar.gz
cd tmux-2.8/
./configure && make

sudo cp -p ~/tmux/tmux-2.8/tmux /usr/local/sbin/
