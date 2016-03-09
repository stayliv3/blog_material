<?php
 
class TestClass
{
    // 一个变量
 
    public $variable = 'This is a string';
 
    // 一个简单的方法
 
    public function PrintVariable()
    {
        echo $this->variable . '<br />';
    }
 
    // Constructor
 
    public function __construct()
    {
        echo '__construct <br />';
    }
 
    // Destructor
 
    public function __destruct()
    {
        echo '__destruct <br />';
    }
 
    // Call
 
    public function __toString()
    {
        return '__toString<br />';
    }
}
 
// 创建一个对象
//  __construct会被调用
 
$object = new TestClass();
 
// 创建一个方法
//  'This is a string’ 这玩意会被输出
 
$object->PrintVariable();
 
// 对象被当作一个字符串
//  __toString 会被调用
 
echo $object;
 
// End of PHP script
// php脚本要结束了， __destruct会被调用
 
?>