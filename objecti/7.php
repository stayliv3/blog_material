<?php
 
include '6.php';
 
// 创建一个对象
 
$obj = new LogFile();
 
// 设置文件名和要储存的日志数据
 
$obj->filename = 'somefile.log';
$obj->LogData('Test');
 
// php脚本结束啦，__destruct被调用，somefile.log文件被删除。
 
?>