// var productExceptSelf = function(nums) {
//     let newNums = []
//     let objNums = {}

//     for(let i = 0; i < nums.length; i++){
//         let currentNum = nums[i]
//             if(!objNums[currentNum]){
//                 objNums[currentNum] = currentNum
//         }else{
//             objNums[currentNum] = currentNum
//         }
//     }
        
//     let answer;
//     for(let key in objNums){
//         if(nums[key] !== key){
//             if (answer){
//             answer = answer * objNums[key]
//             }else{
//                 answer = nums[key] * objNums[key]
//             }
//     }
//         newNums.push(answer)
//     }
//     console.log(newNums)
// }
//     console.log(productExceptSelf([1,2,3,4]))








var searchRange = function(nums, target) {
    let answer = [-1, -1];

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === target) {
            if (answer[0] === -1) {
                answer[0] = i; 
            }
            answer[1] = i; 
        }
    }

    return answer;
}
console.log(searchRange([1, 1], 1))