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

# Configure 301 redirect for /redirect_me
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => "server {
\tlisten 80;
\tlisten [::]:80;
\tserver_name _;
\tlocation /redirect_me {
\t\treturn 301 http://www.youtube.com/;
\t}
\t# Include the original configuration
\tinclude /etc/nginx/sites-available/default;
}",
}
# Restart Nginx service
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}
