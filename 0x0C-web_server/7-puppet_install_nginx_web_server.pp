# Setting up a server using Puppet.

package {'nginx':
	ensure     => 'present',
	provider   => 'apt',

}

exec { 'enable and configure ufw for Nginx HTTP':
  command     => '/usr/bin/sudo /usr/sbin/ufw --force enable && /usr/bin/sudo /usr/sbin/ufw allow "Nginx HTTP"',
  path        => ['/usr/bin', '/usr/sbin'],
  provider    => 'shell',
  unless      => "/usr/bin/sudo /usr/sbin/ufw status | /bin/grep -q 'Nginx HTTP'",
  require     => Package['nginx'],
}

file {'index.nginx-debian.html':
	path    => '/var/www/html/index.nginx-debian.html',
	ensure  => 'file',
    owner   => 'ubuntu',
	content => "Hello World!",
}

file { 'configuration file':
  path    => '/etc/nginx/sites-available/default',
  ensure  => 'file',
  owner   => 'ubuntu',
  content => "server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;

        index index.html index.htm index.nginx-debian.html;

        server_name _;
        location / {
                try_files \$uri \$uri/ =404;
        }
        location /redirect_me {
            return 301 https://www.alxafrica.com;
        }
        error_page 404 /404.html;
        location = /404.html {
            root /var/www/html;
            internal;
        }
    }"
}


file {'/var/www/html/404.html':
    path    =>  '/var/www/html/404.html',
	ensure  => 'file',
	owner   => 'ubuntu',
	content => "Ceci n'est pas une page"
}
exec { 'update nginx configuration and restart':
  command  => "/usr/bin/sudo /bin/sed -i 's@try_files \\$uri \\$uri/ =404;@try_files \\$uri \\$uri/ /404.html;@' /etc/nginx/sites-available/default && /usr/bin/sudo /usr/sbin/service nginx restart",
  path     => ['/usr/bin', '/bin', '/usr/sbin'],
  provider => 'shell',
}
