include stdlib

# add stable version of nginx
exec { 'add nginx stable repo':
  command => 'sudo add-apt-repository ppa:nginx/stable',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
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
  onlyif  => '! dpkg -l nginx | egrep \'îi.*nginx\' > /dev/null 2>&1',
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

# GET SERVER NAME AND SAVE IT TO server VARIABLE
exec { 'get_server_name':
  command     => '/bin/hostname',
  logoutput   => true,
  environment => ['server='],
  provider    => shell,
  path        => ['/bin', '/usr/bin'],
  timeout     => 60,
}

# ADD "X-Served-By" HEADER BEFORE SERVER NAME
exec { 'insert-header-above-server_name':
  command => "sed -i '/^\\s*server_name _;/i\\        add_header X-Served-By \"\$server\";' ${file_path}",
  path    => ['/bin', '/usr/bin', '/sbin', '/usr/sbin'],
  onlyif  => "grep -q -P '^\\s*server_name _;' ${file_path} && ! grep -q -P '^\\s*add_header X-Served-By \"\\\$server\";' ${file_path}",
}

# RESTART nginx
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}
