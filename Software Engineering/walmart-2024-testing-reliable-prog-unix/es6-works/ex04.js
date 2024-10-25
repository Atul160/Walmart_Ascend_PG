// working with template strings with function 

function fnMyFunction(string, arg1, arg2) {
    console.log("String got is " + string)
    console.log("Arg 1 ", arg1);
    console.log("Arg 2 ", arg2);
    console.log(arguments);
}

let firstName = "Diwya";
let age = 30;

let s1 = fnMyFunction`${firstName} is ${age} old`;


// function with spread operator 

function fnMyFunction1(string, ...values) {
    console.log("The string got: " + string);
    console.log("Values are " + values);
    return "From MyFunction1";
}

let address = "Bengaluru";

let s2 = fnMyFunction1`${firstName} is ${age} old and lives in ${address}`;

