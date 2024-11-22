// to show working of div with id

function fnFetchedValue() {

    // assume that the data will from the cloud we shall use fetch or axios 
    let myMates = [
        { firstName: "Atul", lastName: "Kumar" },
        { firstName: "Diwya", lastName: "Sinha" },
        { firstName: "Lingraj", lastName: "Sembelle" },
        { firstName: "Rakesh", lastName: "Kumar" },
        { firstName: "Sudharsan", lastName: "TCM" },
    ];

    console.log(myMates);

    if (myMates.length === 0) {
        document.getElementById("mydiv").innerHTML = "No Records"
    } else {
        const mateListDiv = document.getElementById('mydiv');

        // Iterate through each mate
        myMates.forEach(function (mate) {
            // Create a new div element
            const myDiv = document.createElement('div');
            myDiv.classList.add("mate-class");

            // Set the inner HTML of the div with the mate's name
            myDiv.innerHTML = `<strong>First Name:</strong> ${mate.firstName} <br> <strong>Last Name:</strong> ${mate.lastName}`;

            // Add some margin for spacing
            myDiv.style.marginBottom = '5px';

            // Append the new div to the main div
            mateListDiv.appendChild(myDiv);
        });
    }
}





// sample comment 
function fnPreDefinedFunction() {
    let myName = "Atul Kumar";
    console.log("Lenght of the Name ", myName.length);
    console.log("Uppercase of the Name ", myName.toUpperCase());
    console.log("Lowercase of the Name ", myName.toLowerCase());
    console.log("Index position of the char n ", myName.indexOf("n"));
    console.log("Substring position from (0,3)  ", myName.substring(0, 3));
    console.log("substr of (5,2) ", myName.substr(5, 2));
    console.log("Char @ 2 ", myName.charAt(2));


    console.log("Get ascii equivalents of A ", myName.charAt(0).charCodeAt());

    console.log("replace function tul with mit ", myName.replace("tul", "mit"));

    console.log("Split function ", "India:China:Nepal:Bhutan".split(":"));

}

function fnRegExp1() {
    let vRegExp = /ll/;
    let myString = "Hello";

    console.log(myString.match(vRegExp));

    let myOctals = "023432";
    console.log(myOctals.match(/0[0-7]/)); // match exactly 1 character
    console.log(myOctals.match(/0[0-7]+/)); // match 1 or more 

    // validate the ip address with regular expressions
    console.log("192.168.1.123".match(/\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/));

}



function fnValidateEmail() {

    let email = "atul@walmart.com";

    let validatedEmail = email.match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/);

    console.log(validatedEmail);

    if (email == validatedEmail) {
        console.log("Valid Email");
    } else {
        console.log("Invalid Email");
    }

}