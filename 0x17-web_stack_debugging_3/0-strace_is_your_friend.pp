# Finding out why Apache is returning a 500 error...

exec { 'Attempting fix':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}