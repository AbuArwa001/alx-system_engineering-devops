# configures a brand new Ubuntu machine 
# Install software-properties-common
package { 'software-properties-common':
  ensure => installed,
}

# Add NGINX stable repository
exec { 'add nginx stable repo':
  command     => 'add-apt-repository -y ppa:nginx/stable',
  path        => ['/usr/bin', '/bin'],
  environment => 'DEBIAN_FRONTEND=noninteractive',
  unless      => 'grep -q "^deb .*/nginx/stable" /etc/apt/sources.list /etc/apt/sources.list.d/*',
  require     => Package['software-properties-common'],
}

# update software packages list
exec { 'update packages':
  command => 'apt-get update',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# install nginx
package { 'nginx':
  ensure     => 'installed',
}

# allow HTTP
exec { 'allow HTTP':
  command => "ufw allow 'Nginx HTTP'",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  unless  => "dpkg -l nginx | grep 'îi.*nginx' > /dev/null 2>&1",
}


# change folder rights
exec { 'chmod www folder':
  command => 'chmod -R 755 /var/www',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# create index file
file { '/var/www/html/index.html':
  content => "Hello World!\n",
}

# Save file_path
$file_path = '/etc/nginx/sites-enabled/default'

# Copy file_path content to backup file
exec { 'backup_nginx_default_config':
  command => "/bin/cp -n ${file_path} ${file_path}.bak",
  unless  => "/usr/bin/test -f ${file_path}.bak",
  path    => ['/bin', '/usr/bin'],
}
# GET SERVER NAME AND SAVE IT TO  FILE
exec { 'get_server_name':
  command   => '/bin/hostname',
  logoutput => true,
  creates   => '/tmp/server_name.txt',
  provider  => shell,
  path      => ['/bin', '/usr/bin'],
  timeout   => 60,
}
#READ THE FILE AND SAVE IT TO A server VARIABLE
file { '/tmp/server_name.txt':
  ensure  => file,
  content => $server,
  notify  => Exec['insert-header-above-server_name'],
}
exec { 'get_web-server_name':
  command   => "web_server=\$(echo \$server | sed -n 's/^.*-\\(web-01\\|web-02\\)$/\\1/p')",
  logoutput => true,
  provider  => shell,
  path      => ['/bin', '/usr/bin'],
  timeout   => 60,
}

# ADD "X-Served-By" HEADER BEFORE SERVER NAME
exec { 'insert-header-above-server_name':
  command => "sed -i '/^\\s*server_name _;/i\\        add_header X-Served-By \"\$server\";' ${file_path}",
  path    => ['/bin', '/usr/bin', '/sbin', '/usr/sbin'],
  onlyif  => "grep -q -P '^\\s*server_name _;' ${file_path} && ! grep -q -P '^\\s*add_header X-Served-By \"\\\$web_server\";' ${file_path}",
}

# RESTART nginx
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}
