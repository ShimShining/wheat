#! /bin/awk -f

{
	#如果大于90 输出A,否则输出B
	grade=($2>90?"A":"B")
	print grade
}
