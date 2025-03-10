# Custom HTTP header

exec { 'update server':
  command  => 'apt-get update',
  user     => 'root',
  provider => 'shell',
}
->
# install nginx
package { 'nginx':
  ensure   => present,
  provider => 'apt'
}
->
# custom Nginx response
file_line { 'add HTTP header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;'
}
->
# start core service
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx']
}
