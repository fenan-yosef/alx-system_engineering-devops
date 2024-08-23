# This Puppet manifest optimizes Nginx to handle high traffic by adjusting worker processes and connection limits.

file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => template('nginx/nginx.conf.erb'),
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  subscribe  => File['/etc/nginx/nginx.conf'],
}

exec { 'optimize_nginx':
  command => '/usr/sbin/nginx -s reload',
  onlyif  => 'grep -q "worker_processes auto;" /etc/nginx/nginx.conf',
  notify  => Service['nginx'],
}

# Ensure the file ends with a new line
