// passing function as argument 

// setInterval(() => console.log("Welcome to es6"), 1000);

let names = ['Diwya', 'Rakesh', 'Lingraj', 'Sudharshan'];


// legacy code 
// for (let index = 0; index < names.length; index++) {
//     console.log(names[index].charAt(0))
// }


let firstChars = names.map((value) => value.charAt(0));
console.log(firstChars);

// to check if the name exists at cetain position 
let position = names.findIndex((value) => value === 'Lingraj');
console.log(`Name ${position == -1 ? "Not Found" : "Found At " + position}`);


