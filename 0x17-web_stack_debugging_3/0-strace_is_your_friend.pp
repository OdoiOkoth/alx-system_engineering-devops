# puppet script to look for and fix typo error line in a file on a server
$file_root = '/var/www/html/wp-settings.php'
#replace line containing "phpp" with "php"
exec { 'edit_line':
  command => "sed -i 's/phpp/php/g' ${file_root}",
  path    => ['/bin','/usr/bin']
}
