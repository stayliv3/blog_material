<?php
 
// 某类
 
class User
{
    // Class data
 
    public $age = 0;
    public $name = '';
 
    // Print data
 
    public function PrintData()
    {
        echo 'User ' . $this->name . ' is ' . $this->age . ' years old. <br />';
    }

    
}
 
// 重建对象
 
$usr = unserialize('O:4:"User":2:{s:3:"age";i:20;s:4:"name";s:4:"John";}');
 
// 调用PrintData 输出数据
 
$usr->PrintData();
 
?>