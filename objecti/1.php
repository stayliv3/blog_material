<?php
 
class TestClass
{
    // 一个变量
 
    public $variable = 'This is a string';
 
    // 一个简单的方法
 
    public function PrintVariable()
    {
        echo $this->variable;
    }
}
 
// 创建一个对象
 
$object = new TestClass();
 
// 调用一个方法
 
$object->PrintVariable();
 
?>