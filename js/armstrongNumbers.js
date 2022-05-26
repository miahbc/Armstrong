// How can you make this more scalable and reusable later?

exports.findArmstrongNumbers = function (n) {

let armNums = []
let sum = 0
for (let i=0; i<n.length; i++) {
    // console.log(n[i].toString().split(''))
    let arr = n[i].toString().split('')
    for (let j=0; j<arr.length; j++) {
        sum += (arr[j]**(arr.length))
        // console.log(sum)
        if (sum === n[i]) {
            if (!armNums.includes(sum)) {
                armNums.push(sum)
            }   
        }
    } sum = 0
} 

 return armNums
} 








// console.log(shallowEqualArrays(arm.findArmstrongNumbers([0]),[0]));
// console.log(shallowEqualArrays(arm.findArmstrongNumbers(createArrayOfNum(8)), [0, 1, 2, 3, 4, 5, 6, 7]));
// console.log(shallowEqualArrays(arm.findArmstrongNumbers(createArrayOfNum(99)), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]));
// console.log(shallowEqualArrays(arm.findArmstrongNumbers(createArrayOfNum(999)), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]));
