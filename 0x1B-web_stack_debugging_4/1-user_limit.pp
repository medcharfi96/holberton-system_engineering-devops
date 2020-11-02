#task adv
exec { 'user':
command => "sudo /bin/sed -i 's/nofile 6895/g' /etc/security/limits.conf",
path    => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
}