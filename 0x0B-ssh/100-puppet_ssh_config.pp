#Using Puppet to make changes to our configuration file.

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "
  	  #ssh client configuration
	  host*
	  IdentityFile ~/.ssh/school
	  PasswordAuthentication no
	  ",
}
