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








// var searchRange = function(nums, target) {
//     let answer = [-1, -1];

//     for (let i = 0; i < nums.length; i++) {
//         if (nums[i] === target) {
//             if (answer[0] === -1) {
//                 answer[0] = i; 
//             }
//             answer[1] = i; 
//         }
//     }

//     return answer;
// }
// console.log(searchRange([1, 1], 1))





// var fizBuzz = function(n){
//     let newNums = []
//     for(let i = 1; i <= n; i++){
//         if(i % 5 === 0 && i % 3 === 0){
//             newNums.push("fizzBuzz")
//         }else if(i % 3 === 0){
//             newNums.push("Fizz")
//         }else if(i % 5 === 0){
//             newNums.push("Buzz")
//         }else{
//             newNums.push(i)
//         }
//     }
//     return newNums
// }
// console.log(fizBuzz(15))



/* completed
week1:
-
two sum
contains duplicate
best time to buy stock and sell
valid anagram

*/


// contains duplicate
// [1,1,1,3,3,4,3,2,4,2] === true [1,2,3,4] === false
// function containsDuplicate(nums){
//     let numStorage = {}
//     for(let i = 0; i < nums.length; i++){
//         if(numStorage[nums[i]] === undefined){
//             numStorage[nums[i]] = 0
//         }else{
//             return true
//         }
//     }
//     return false
// }

// console.log(containsDuplicate([1,1,2,3,4,5]))



// var isAnagram = function(s,t){

//     if(s.length != t.length){
//         return false
//     }

//     let strArr = Array.from(s)
//     let trArr = Array.from(t)
//     sorted1 = strArr.sort()
//     sorted2 = trArr.sort()
//     let placeholder = []

//     for(let i = 0; i < sorted1.length; i++){
//         if(sorted1[i] === sorted2[i]){
//             placeholder.push(sorted2[i])
//         }
//     }

//     placeholder = placeholder.join('')
//     sorted1 = sorted1.join('')

//     return placeholder === sorted1 ? true:false


// }
// console.log(isAnagram("a", "ab"))


/*COMPLETED WEEK 2
-


*/

// var reverseList = function(head) {
//     class LinkedList {
//         constructor() {
//             this.head = null
//         }
//         add(data){
//             const node = new Node(data)
//             node.next = this.head
//             this.head = node;
//         }
//     }
// };




// s = () output true 
// s = [(]) output false

// function isValid(s){

// }















function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
  }

  var addTwoNumbers = function(l1, l2) {
    
    let carry = 0
    let start = new ListNode(0)
    let current = start

    while(l1 || l2 || carry){
        let val1 = l1 ? l1.val : 0;
        let val2 = l2 ? l2.val : 0;
        
        total = val1 + val2 + carry
        carry = Math.floor(total / 10);
        digit = total % 10

        current.next = new ListNode(digit)
        current = current.next

        if(l1){
            l1 = l1.next
        }
        if(l2){
            l2 = l2.next
        }    
    }
    return start.next
}

