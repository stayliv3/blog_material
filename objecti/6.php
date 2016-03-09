<?php 
 
class LogFile
{
    // log文件名
 
    public $filename = 'error.log';
 
    // 某代码，储存日志进文件
 
    public function LogData($text)
    {
        echo 'Log some data: ' . $text . '<br />';
        file_put_contents($this->filename, $text, FILE_APPEND);
    }
 
    // Destructor 删除日志文件
 
    public function __destruct()
    {
        echo '__destruct deletes "' . $this->filename . '" file. <br />';
        unlink(dirname(__FILE__) . '/' . $this->filename);
    }
}
 
?>