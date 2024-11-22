echo "with for loop " 

for name in `ls *.sh`
do
	if [ -f $name ] 
	then 
	
		echo $name 
	fi 
done


echo " ------------- with shift ------------------"



if [ $# -eq 0 ];then 
	echo "please pass arguments" 
	exit 1 
fi 

while [ $# -gt 0 ]; do
	echo "Processing Argument : $1"

	if [ -f $1 ]; then 
		echo "$1 is a file "
	elif [ -d $1 ]; then
		echo "$1 is a directory" 
	else 
		echo "Sorry neither file or directory" 
	fi 
	shift 
done






