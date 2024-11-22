// to work with arrays and associated functions 


function fnArray1() {
    arr1 = new Array(5);
    arr1[0] = "Hello";
    arr1[1] = 123;
    arr1[2] = "Bye";
    arr1[3] = new Object();
    arr1[4] = false;

    console.log("Length of the array " + arr1.length);

    for (const temp of arr1) {
        console.log(temp);
    }
}

function fnArray2() {
    let arr2 = ["sun", "mon", "tue", "wed", "thu"];

    console.log("Lenght is " + arr2.lenght);

    console.log(arr2);
    // add another element with unshift 
    arr2.unshift("New Day");
    console.log(arr2);

    // add element at the last 
    arr2.push("FRIDAY", "SATURDAY");
    console.log(arr2);

    // to remove from the last is pop 
    arr2.pop();
    console.log(arr2);

    // to remove from the start of the array 
    arr2.shift();
    console.log(arr2);

    arr2.splice(1, 1, "MONDAY");
    console.log(arr2);
}
// fnArray2();

// working with associative arrays in java with functions 

function fnAssociativeArray() {
    console.log(fnAssociativeArray.arguments);
}

fnAssociativeArray(1, 2, 3, 4, 5, "Hello");
fnAssociativeArray(1, 2, "Hello");