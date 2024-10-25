# to work with while condition 

echo "Enter a number to loop"
read num

count=1 

while [ $count -lt $num ] 
do 
	echo $count
	count=$(($count + 1))
done

