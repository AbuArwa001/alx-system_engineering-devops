#setup client config
file { '/etc/ssh/ssh_config':
  ensure  => file,
  path    => '/etc/ssh/ssh_config',
  mode    => '0744',
  content => 'Host *
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
'
}
