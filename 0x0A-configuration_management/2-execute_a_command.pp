# This Puppet manifest kills a process named 'killmenow' using pkill

exec { 'kill killmenow':
  command => '/usr/bin/pkill -f killmenow',
  path    => ['/bin', '/usr/bin'],
  onlyif  => '/usr/bin/pgrep -f killmenow',
}

