#! /usr/bin/bash

#定义函数
func()
{
	#输出变量x的值
	echo "$v1"
	#修改变量x的值
	v1=200
}
#在脚本中定义变量x
v1=100
#调用函
func
#输出变量x的值
echo "$v1"
