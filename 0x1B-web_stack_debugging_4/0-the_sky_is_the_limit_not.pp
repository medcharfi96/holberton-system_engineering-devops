# zab
exec {'fixing task':
command => "sudo sed -i 's/15/4098/g' /etc/default/nginx; service nginx restart",
path    => ['/usr/bin', '/bin'],
}