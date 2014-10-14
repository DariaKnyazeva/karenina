# -*- mode: ruby -*-

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    ENV['VAGRANT_DEFAULT_PROVIDER'] = 'docker'

    config.vm.provider "docker" do |d|
        d.build_dir = "docker"
        d.has_ssh = true
    end

    config.ssh.username = "viewsite"
    config.ssh.private_key_path = "docker/insecure_key"
    config.vm.network "forwarded_port", guest: 8000, host: 9000
    config.vm.synced_folder ".", "/srv/viewsite"
end
