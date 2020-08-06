# connection 
file_line {'nonononono':
  line =>'PasswordAuthentication no',
  path =>'/etc/ssh/ssh_config',
}
file_line {'vezvez':
  line =>'IdentityFile ~/.ssh/holberton',
  path =>'/etc/ssh/ssh_config',
}