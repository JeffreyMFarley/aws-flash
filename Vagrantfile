# -*- mode: ruby -*-
# vi: set ft=ruby :
require 'getoptlong'

project = "aws-flash"
container_root = "/home/vagrant"

PORTS = %w(8080 8081 8082 2345 2346 5000)

# -----------------------------------------------------------------------------
# Read options
# -----------------------------------------------------------------------------
opts = GetoptLong.new(
  [ '--clean', GetoptLong::OPTIONAL_ARGUMENT ],
)

clean = false

opts.each do |opt, arg|
  case opt
  when '--clean'
    clean = true
  end
end

# -----------------------------------------------------------------------------
# Configure the VM
# -----------------------------------------------------------------------------
Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.box_check_update = false

  PORTS.each do |p|
    config.vm.network "forwarded_port", guest: p, host: p
  end

  config.vm.synced_folder ".", "#{container_root}"

  config.vm.provider "virtualbox" do |v|
    v.name = project
    v.memory = 2000
    v.cpus = 2
  end

  # https://github.com/Varying-Vagrant-Vagrants/VVV/issues/517
  config.vm.provision "fix-no-tty", type: "shell" do |s|
    s.privileged = false
    s.inline = "sudo sed -i '/tty/!s/mesg n/tty -s \\&\\& mesg n/' /root/.profile"
  end

  config.vm.provision "shell", inline: "apt-get install python-dev python-pip"

  if clean
    config.vm.provision "shell", inline: "./clean.sh", run: "always"
  end
end
