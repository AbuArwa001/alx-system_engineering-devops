# Install Flask version 
package { 'python3':
  ensure => installed,
}

package { 'python3-pip':
  ensure => installed,
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
