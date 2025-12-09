// return the two oldest/oldest ages within the array of ages passed in.
function twoOldestAges(ages){
    let emptyArray = [];
    let max = 0;
    for (let i = 0; i < ages.length; i++) {
        if (ages[i] > ages[i + 1]) {
            max = ages[i];
            } else {
                max = ages[i + 1];
            }
    }
    return max;
}

console.log(twoOldestAges([4, 8, 3, 12, 24, 10, 367]));