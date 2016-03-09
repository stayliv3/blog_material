<?php 
 
// … 一些include ...
 
class FileClass
{
    // 文件名
 
    public $filename = 'error.log';
 
    //当对象被作为一个字符串会读取这个文件
 
    public function __toString()
    {
        return file_get_contents($this->filename);
    }
}
 
// Main User class
 
class User
{
    // Class data
 
    public $age = 0;
    public $name = '';
 
    // 允许对象作为一个字符串输出上面的data
 
    public function __toString()
    {
        return 'User ' . $this->name . ' is ' . $this->age . ' years old. <br />';
    }
}
 
// 用户可控
 
$obj = unserialize($_GET['usr_serialized']);
 
// 输出 __toString
 
echo $obj;
 
?>