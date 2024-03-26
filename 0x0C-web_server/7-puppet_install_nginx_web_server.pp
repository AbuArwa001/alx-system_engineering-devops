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
  content => "# Redirect /redirect_me to another page
              server {
                listen 80;
                listen [::]:80;
                server_name _;
                location /redirect_me {
                  return 301 https://www.example.com/new_page;
                }
                # Include the original configuration
                include /etc/nginx/sites-available/default;
              }",
}
# Restart Nginx service
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}
