<?php
 
include '6.php';
 
// ... 一些狗日的代码和 LogFile 类 ...
 
// 简单的类定义
 
class User
{
    // 类数据
 
    public $age = 0;
    public $name = '';
 
    // 输出数据
 
    public function PrintData()
    {
        echo 'User ' . $this->name . ' is ' . $this->age . ' years old. <br />';
    }
}
 
// 重建 用户输入的 数据
 
$usr = unserialize($_GET['usr_serialized']);
 
?>