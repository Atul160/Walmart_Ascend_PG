echo "Enter file to be copied" 
read srcfile 

echo "Enter destination file "
read destfile 

if [ -f $srcfile -a -s $srcfile ] 
then 
	echo "The file copy in place"

	cp ./$srcfile ./copyfolder/$destfile 
else 
	echo "The file cannot be copied" 
fi 
