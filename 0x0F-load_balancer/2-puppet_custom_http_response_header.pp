# Define a class for managing nginx installation and configuration
class nginx_setup {
    package { 'nginx':
        ensure  => 'installed',
        require => Package['nginx'],
    }

    file { '/var/www/html/index.html':
        ensure  => 'file',
        content => 'Hello World!',
        require => Package['nginx'],
    }

    file { '/etc/nginx/sites-enabled/default':
        ensure  => 'file',
        content => template('nginx/default.erb'),
        require => Package['nginx'],
        notify  => Service['nginx'],
    }

    service { 'nginx':
        ensure    => 'running',
        enable    => true,
        hasstatus => true,
        hasrestart => true,
    }
}

# Apply the nginx_setup class to the node
node 'web-01' {
    include nginx_setup
}
