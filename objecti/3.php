<?php
 
// 某类
 
class User
{
    // 类数据
 
    public $age = 0;
    public $name = '';
 
    // 输出数据
 
    public function PrintData()
    {
        echo 'User ' . $this->name . ' is ' . $this->age
             . ' years old. <br />';
    }
}
 
// 创建一个对象
 
$usr = new User();
 
// 设置数据
 
$usr->age = 20;
$usr->name = 'John';
 
// 输出数据
 
$usr->PrintData();
 
// 输出序列化之后的数据
 
echo serialize($usr);
 
?>