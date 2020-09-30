# appache w zebi  w zebbeks
exec { 'setting.php':
  command => "sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php",
  path    => '/bin/',
}