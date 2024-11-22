clear 
echo "Enter your choice of OS"
read os 

case $os in 
	MAC | mac) echo "you have MAC OS" 
		;;

	WINDOWS | windows) 
		echo "You have WINDOWS OS" 
		;; 
	
	LINUX | linux) 
		echo "You have LINUX OS" 
		;; 

	*) 
		echo "You have other OS " 
		;; 
esac 


