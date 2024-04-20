# to terminate a program called killmenow
exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
