# -*- mode: ruby -*-
# vi: set ft=ruby :
# author: tikicn

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "bento/ubuntu-16.04"
  config.vm.synced_folder "~/pwn", "/home/vagrant/pwn"
  config.vm.provision "shell", inline: <<-SHELL
	dpkg --add-architecture i386
	apt -y update
	apt -y upgrade
	apt install -y xsel socat gdb gdb-multiarch libc6-dbg libc6-dbg:i386 git binutils gcc-multilib g++-multilib curl wget make libssl-dev build-essential ruby ruby-dev radare2 netcat tmux nasm ltrace strace vim
	git clone https://github.com/longld/peda /home/vagrant/peda 
	git clone https://github.com/scwuaptx/Pwngdb.git /home/vagrant/Pwngdb 
	cp /home/vagrant/Pwngdb/.gdbinit /home/vagrant/ 
	mkdir /gef && wget https://github.com/hugsy/gef/raw/master/gef.py -O /home/vagrant/gef/gef.py
	wget https://github.com/downloads/0vercl0k/rp/rp-lin-x64 -O /usr/local/bin/rp++ && chmod +x /usr/local/bin/rp++
	apt install python3 -y
	wget https://github.com/slimm609/checksec.sh/archive/1.6.tar.gz && tar zxvf 1.6.tar.gz
	cp checksec.sh-1.6/checksec /usr/bin/checksec.sh
	apt install -y python3-dev python3-pip && python3 -m pip install --upgrade pip
	git clone https://github.com/Gallopsled/pwntools
	pip install --upgrade --editable ./pwntools
	gem install one_gadget
	echo "source ~/peda/peda.py" >> ~/.gdbinit
	cp /home/vagrant/pwn/tmux.conf /home/vagrant/.tmux.conf 
  SHELL
end
