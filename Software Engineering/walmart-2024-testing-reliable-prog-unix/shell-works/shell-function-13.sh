# working to show use of functions in shell script 
clear
add() {
	sum=$(( $1 + $2 ))
	echo $sum 
}

function upperCase () {
	echo $1 | tr 'abcdefghijklmnopqrstuvwxyz' 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'	
}


function upperCase1 () {
	echo $1 | tr [a-z] [A-Z] 
}


echo "Enter first number" 
read num1 
echo "Enter second number" 
read num2

add $num1 $num2 


# to read the word in any case and to convert to upper case 

upperCase "India"
upperCase1 "Hindustan" 


