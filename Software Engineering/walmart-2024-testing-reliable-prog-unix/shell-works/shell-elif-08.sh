echo "Enter Your state" 

read state


if [ $state = "Karnataka" ]
then 
	echo "Hello you are in Karnataka" 

	echo "Please enter your City "
	read city 

	if [ $city = "Bengaluru" ] 
	then 
		echo "you live in silicon valley of india" 
	else 	
		echo "you live in city : $city"
	fi 

elif [ $state = "Maharastra" ]
then
	echo "Hello You are in Maharastra" 
else
	echo "You live in other state $state"
fi

