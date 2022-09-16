# Puppet file to kill a process, killmenow
exec { 'pkill killmenow':
  command  => 'pkill killmenow',
  provider => 'shell'
}
