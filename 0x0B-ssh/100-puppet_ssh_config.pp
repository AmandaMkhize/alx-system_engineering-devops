# Puppet manifest to configure SSH client settings

# Define the SSH client configuration file path
$file_path = "/home/ubuntu/.ssh/config"

# Ensure SSH client configuration file exists
file { $file_path:
  ensure => file,
}

# Configure SSH client settings
file_line { 'Turn off passwd auth':
  ensure => present,
  path   => $file_path,
  line   => '    PasswordAuthentication no',
}

file_line { 'Declare identity file':
  ensure => present,
  path   => $file_path,
  line   => '    IdentityFile ~/.ssh/school',
}
