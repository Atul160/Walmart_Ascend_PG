//program to show working of class in es6 

class Person {
    constructor(name, age = 18) {
        this.name = name;
        this.age = age;
    }

    display() {
        console.log(`Name: ${this.name}, age: ${this.age}`);
    }
}

class Employee extends Person {
    constructor(name, age, designation) {
        super(name, age);
        this.designation = designation;
    }
    display() {
        super.display();
        console.log("Designation :", this.designation);
    }
}


let p1 = new Person("Kumar", 34);
p1.display();
console.log(typeof (p1));

let p2 = new Person("Rakesh");
p2.display();

let e1 = new Employee("Harish", 23, "Developer")
e1.display();

