// working with  templage string 


let s1 = "Rakesh";
let s2 = "Kumar";
let s3 = "this is es6 training";

console.log("s1=" + s1 + ", s2=" + s2);
console.log("S3 is : ", s3);

// templage string 
let s4 = `this is templage 
string in multiple
lines`;

console.log("s4 = " + s4);

let name = "Naveen";
let email = "naveen.srinivas@u-next.com";
let s5 = `email of ${name} is ${email}`;

console.log("s5 = " + s5);

let age = 10;
let s6 = `${name} is ${age < 18 ? 'Minor' : 'Major'}`;
console.log("s6 = " + s6);