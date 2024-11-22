# program to show working of until loop 


count=1 

until [ $count -gt 10 ] 
do
	echo $count 
	count=$(($count + 1)) 
done


# with while loop 
echo "------- using while loop ------ " 

count=1

while [ $count -lt 10 ] 
do
	echo $count 
	count=$(($count + 1)) 
done


