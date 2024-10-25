// working with for loop

function test() {
    for (let i = 0; i < 5; i++) {
        console.log("i value is ", i);
    }

    // this will not work as the local variable scope is within for loop
    // console.log("Value of i outside function is ", i); 
}


test();