
// function divide(num1, num2, callback) {

//     if (typeof callback != 'function') {
//         throw "Please pass callback function";
//     }

//     setTimeout(() => {

//         if (typeof num1 != 'number') {
//             callback("Please enter 1st arg as number");
//             return;
//         }
//         if (typeof num2 != 'number') {
//             callback("Please enter 2nd arg as number");
//             return;
//         }

//         if (num2 == 0) {
//             callback("Sorry number cannot be divided");
//             return;
//         }

//         callback(null, num1 / num2);
//     }, 0);
// }

function divide(num1, num2) {


    return new Promise((resolve, reject) => {

        if (typeof num1 != 'number') {
            reject("Please enter 1st arg as number");
            return;
        }
        if (typeof num2 != 'number') {
            reject("Please enter 2nd arg as number");
            return;
        }

        if (num2 == 0) {
            reject("Sorry number cannot be divided");
            return;
        }

        resolve(num1 / num2);
    });



}


console.log("Start of Script");
let num1 = 12;
let num2 = 5;


// divide(num1, num2, (err, result) => {
//     if (err) {
//         console.log("Error is ", err);
//     } else {
//         console.log("Result is ", result);
//     }
// });


divide(num1, num2)
    .then(result => console.log("Result " + result))
    .catch(err => console.log("Error " + err));


console.log("End of Script");

