#task adv
exec { 'user':
command  => "sudo sed -i 's/holberton hard nofile 5/holberton hard nofile 6003/g' /etc/security/limits.conf
sudo sed -i 's/holberton soft nofile 4/holberton soft nofile 6003/g' /etc/security/limits.conf",
path     => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
provider => shell,
}