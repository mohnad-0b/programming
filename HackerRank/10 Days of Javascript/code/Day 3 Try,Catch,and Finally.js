'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the reverseString function
 * Use console.log() to print to stdout.
 */
function reverseString(string) {
if (typeof(string) == "string"){
let bla=string
string = string.split('')
string = string.reverse()
string = string.join("")

if (string == bla){
   
    return 0
}else{
    console.log(string)
    return 0
}
}else{
    console.log("s.split is not a function")
    console.log(string)
    return 0
} 
}


function main() {
    const s = eval(readLine());
    
    reverseString(s);
}