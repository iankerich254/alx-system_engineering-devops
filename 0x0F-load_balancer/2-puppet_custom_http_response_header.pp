# This Puppet manifest installs Nginx and configures it to include a custom HTTP header with the server's hostname.

node default {
  package { 'nginx':
    ensure => installed,
  }

  # Ensure the Nginx service is running and enabled at boot
  service { 'nginx':
    ensure     => running,
    enable     => true,
    subscribe  => File['/etc/nginx/sites-available/default'],
  }

  # Get the hostname of the server
  $hostname = $facts['networking']['hostname']

  # Configure Nginx to add the custom header
  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => template('nginx/default.erb'),
    notify  => Service['nginx'],
  }

  # Template for the Nginx default site configuration
  file { '/etc/puppetlabs/code/environments/production/modules/nginx/templates/default.erb':
    ensure  => file,
    content => @(END),
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        try_files $uri $uri/ =404;
        add_header X-Served-By <%= @hostname %>;
    }
}
    | END
  }
}
