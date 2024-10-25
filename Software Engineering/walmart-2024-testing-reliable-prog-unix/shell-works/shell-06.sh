num1=10
num2=20 

echo $(( $num1 < $num2 ))    # ouput to 1 -> meaning true 

[ $num1 -lt $num2 ]
echo $? # this should be 0 




