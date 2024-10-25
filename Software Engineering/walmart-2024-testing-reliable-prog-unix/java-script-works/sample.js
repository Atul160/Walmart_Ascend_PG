function fnFirst() {
    console.log("hi you invoded fnFirst");

}


function fnSecond(myname) {
    console.log("Hello " + myname);
}

function fnThird() {
    myarr = ["hi", "hell", "how", "are", "you"];

    for (temp in myarr) {
        console.log(myarr[temp])
    }

}


function fnGetData() {
    fetch("https://jsonplaceholder.typicode.com/posts/1")
        .then(data => console.log(data));
}


function fnDatatypes() {
    let myStr = "India";
    let myInt = 123;
    let myBoolean = true;

    console.log(myStr);
    console.log(myInt);
    console.log(myBoolean);

    console.log(typeof (myStr));
    console.log(typeof (myInt));
}


function fnCheckVote() {
    let name = prompt("Enter Your Name");
    let age = parseInt(prompt("Enter Your Age"));

    if (age > 18) {
        alert("You can vote " + name);
    } else {
        alert("you cannot vote " + name + " wait for " + (18 - age) + " Years");
    }

}

function fnEqualCheck() {
    console.log("30" === 30);
}


function fnOverLoad() {
    console.log(fnOverLoad.arguments.length);

    console.log(fnOverLoad.arguments);


} 
