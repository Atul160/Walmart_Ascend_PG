# to show working of basic file attributes 

# to check if its a directory 
[ -d $1 ]
echo $? 

# to check if its a file 
[ -f $1 ]
echo $? 

# to check if the file has read permission 
[ -r $1 ]
echo $? 




