# This Puppet manifest optimizes the Nginx configuration to handle high traffic by adjusting worker processes and connection limits

# Ensuring the Nginx configuration file contains the necessary optimizations
file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => template('nginx/nginx.conf.erb'),
  notify  => Service['nginx'],
}

# Applying Nginx service restart after configuration change
service { 'nginx':
  ensure     => running,
  enable     => true,
  subscribe  => File['/etc/nginx/nginx.conf'],
}

# Increase worker processes and connections to improve handling of simultaneous requests
exec { 'optimize_nginx':
  command => '/usr/sbin/nginx -s reload',
  onlyif  => 'grep -q "worker_processes auto;" /etc/nginx/nginx.conf',
  notify  => Service['nginx'],
}

