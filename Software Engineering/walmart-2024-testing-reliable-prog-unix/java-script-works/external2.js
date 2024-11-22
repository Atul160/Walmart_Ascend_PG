// program to show working of object based features

// in java script there is no class, function itself is treated as class 


obj = new Object();

obj.firstName = "Naveen";
obj.lastName = "Kumar";


function Person(firstName, lastName, age) { // this is treated as constructor 
    this.firstName = firstName;
    this.lastName = lastName;
    this.age = age;
}


Person.prototype.display = function () {
    console.log("First Name " + this.firstName);
    console.log("LastName " + this.lastName);
    console.log("Age " + this.age);

}



p = new Person("Atul", "Kumar", "34");
p.display();
