// working de-structuring and spread operator 


let numbers = [1, 2, 4, 7, 12, 45, 76, 22];

console.log(numbers);

let numbers1 = [100, 200, 300, ...numbers];
console.log(numbers1);

let person = { firstName: "Kumar", lastName: "Naveen", email: "naveen.srinivas@u-next.com" };
let fullDetails = { city: "Bengaluru", ...person, country: "India" }
console.log(fullDetails);


let numbers2 = { ...numbers };
console.log(numbers2);
numbers.push(888);
console.log(numbers2);
console.log(numbers === numbers2);


////////////////// 

let { firstName, lastName, email } = person;
console.log("First Name ", firstName);
console.log("Last name ", lastName);
console.log("company email ", email);



