# Install Flask version 
require 'uri'

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

URI.encode_www_form_component('flask')

