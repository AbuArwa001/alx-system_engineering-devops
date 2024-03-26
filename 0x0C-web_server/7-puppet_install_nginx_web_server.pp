# execute a command
# Update apt packages
exec { 'apt-update':
  command => '/usr/bin/apt-get update',
  path    => '/usr/bin',
}

# Install Nginx
package { 'nginx':
  ensure => 'latest',
}

# Allow Nginx through firewall
exec { 'allow-nginx':
  command => 'ufw allow "Nginx HTTP"',
  path    => '/usr/bin',
}

# Serve "Hello World!" at the root
file { '/var/www/html/index.nginx-debian.html':
  content => 'Hello World!',
}

# Restart Nginx service
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}
