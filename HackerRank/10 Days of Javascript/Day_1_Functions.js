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



function factorial(n){
    let factorial=1
    
    for (let i=1;i<=n;i++){
        factorial = factorial * i
    }
    return factorial;
    }


function main() {
    const n = +(readLine());
    
    console.log(factorial(n));
}