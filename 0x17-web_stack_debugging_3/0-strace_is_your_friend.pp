# appache w zebi  w zebbeks
exec { 'replacing my php':
  command => "sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php",
  path    => '/bin/',
}