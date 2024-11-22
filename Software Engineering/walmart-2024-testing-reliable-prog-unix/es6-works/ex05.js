// how javascript works 
// in java script the functions can be delcared any where and can be invoked if needed you can invoke before it is written 

let retMsg = fnHello();
console.log("Message :", retMsg);


// all the function which are written are loaded in the VM + named function 
function fnHello() {
    return "Hello World";
}
///////////////////////////////////////
// when you have anonymous function you cannot call before its scope is available 
let greet = function () {
    return "Hello World1";
}

function dummyFunction(arg) {
    console.log(arg());
}

dummyFunction(function () {
    console.log("I'm passing function as arg to another function");
});

console.log(greet);

console.log(greet());




