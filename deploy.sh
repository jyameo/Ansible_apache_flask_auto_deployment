if [ ! $(which ansible-playbook) ]; then
  if grep -q 'Fedora' /etc/system-release || grep -q 'Amazon Linux' /etc/system-release; then
    yum clean all
    rm -rf /var/cache/yum
    # Install Ansible
    sudo `which pip` install ansible
  fi
fi

if [ ! $(which virtualenv) ]; then
  sudo rm /usr/bin/virtualenv
fi

# Run Ansible playbook
ansible-playbook ./flask_app.yml

# Test Application
./run-tests.sh
