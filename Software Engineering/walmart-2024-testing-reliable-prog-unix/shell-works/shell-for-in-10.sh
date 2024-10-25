# program to show working of for in 

for name in adarsh diwya harish lingraj 
do	
	echo $name 
done 



# working with files 
echo "---------------------------------------------" 


for file in `ls`
do	
	if [ -f $file ] 
	then 
		echo $file 
	fi 
done
