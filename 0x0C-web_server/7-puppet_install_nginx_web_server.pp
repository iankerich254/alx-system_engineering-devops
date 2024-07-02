# 7-puppet_install_nginx_web_server.pp

# Ensure the package 'nginx' is installed
package { 'nginx':
  ensure => installed,
}

# Ensure the service 'nginx' is running and enabled at boot
service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  require    => Package['nginx'],
}

# Create the custom 404 error page
file { '/var/www/html/custom_404.html':
  ensure  => file,
  content => 'Ceci n\'est pas une page',
  require => Package['nginx'],
}

# Create the custom index.html
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
}

# Configure the Nginx server
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

# Template for the default site configuration
file { '/etc/nginx/templates/default.erb':
  ensure  => file,
  content => @("EOF"),
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location = /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /custom_404.html;
    location = /custom_404.html {
        internal;
    }
}
  | EOF
}

