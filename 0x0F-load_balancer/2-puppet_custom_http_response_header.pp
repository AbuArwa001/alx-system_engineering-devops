include stdlib

# Define a class for managing nginx installation and configuration
class nginx {
  # UPDATE SYSTEM
  exec { 'apt-update':
    command     => '/usr/bin/apt-get update',
    refreshonly => true,
  }

  # INSTALL nginx
  package { 'nginx':
    ensure => installed,
  }

  # Create index.html file and add content
  file { '/var/www/html/index.html':
    ensure  => 'file',
    content => 'Hello World!',
    require => Package['nginx'],
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
}
