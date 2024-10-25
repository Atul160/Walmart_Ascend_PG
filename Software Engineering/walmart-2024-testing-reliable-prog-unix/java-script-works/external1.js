// this is single line comment 
/* multi line 
comment */


function fnDataType() {
    let myStr = "Hello";
    let myInt = 123;
    let myBoolean = true;


    if (typeof (myStr) === 'string') {
        console.log("myStr Datatype is String");
    }

    console.log(myInt + 1);
    console.log(myInt + myBoolean);

    console.log(myStr + myBoolean);

    console.log(10 * "123");
    console.log("123" * 10);

    console.log(10 / "3a");

    if (10 / "3a" == NaN) {
        console.log("True for NaN");
    } else {
        console.log("False for NaN");
    }
    // second version 

    if (isNaN(10 / "3a")) {
        console.log("True for NaN");
    } else {
        console.log("False for NaN");
    }


}

gOuterInteger = 200;
function fnDataTypeScope() {
    gInteger = 100; // this variable will be considered as global variable from this line onwards 
    {
        var myVar1 = 300; // since we have said this is var then scope will be local to the function 
        let myLetVar1 = 400;
    }
    console.log("in fnDataTypeScope() gOuterInteger-> " + gOuterInteger);
    console.log("in fnDataTypeScope()  gInteger-> " + gInteger);
    console.log("in fnDataTypeScope() myVar1-> " + myVar1);
    console.log("in fnDataTypeScope() myLetVar1 -> " + myLetVar1);
}

function fnCheckScope() {
    console.log("in fnCheckScope() gOuterInteger-> " + gOuterInteger);
    console.log("in fnCheckScope()  gInteger-> " + gInteger);
    // console.log("in fnCheckScope() myVar1-> " + myVar1); // this will give an error 
}
fnDataTypeScope();
fnCheckScope();
// fnDataType();