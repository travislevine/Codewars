// return the two oldest/oldest ages within the array of ages passed in.
function getMaxNumArray(ages){
    var max = 0;
    for (let i = 0; i < ages.length; i++) {
        if (ages[i] > max) {
            max = ages[i];
            } 
    }
    return max;
}

console.log(getMaxNumArray([4, 8, 3, 12, 24, 10, 367]));