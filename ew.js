// function ninetyNine(num){
// do{
//     if(num === 1) {
//         console.log(`Take one down and pass it around, ${num} bottle of beer on the wall. \n ${num} bottle of beer on the wall, ${num} bottle of beer.`)
//         num = num - 1        
//     }else{
//         console.log(`${num} bottles of beer on the wall, ${num} bottles of beer. \n Take one down and pass it around, ${num - 1} bottles of beer on the wall.`)
//             num = num - 1   
//     }
// }while(num > 0)
//     console.log(`Take one down and pass it around, no more bottles of beer on the wall. \n No more bottles of beer on the wall, no more bottles of beer. \n Go to the store and buy some more, 99 bottles of beer on the wall.`)
// }
// ninetyNine(10)

function ninetyNine(num){
        if(num === 0){
            console.log(`Take one down and pass it around, no more bottles of beer on the wall. \n No more bottles of beer on the wall, no more bottles of beer. \n Go to the store and buy  some more, 99 bottles of beer on the wall.`)
        }else if(num === 1) {
            console.log(`Take one down and pass it around, ${num} bottle of beer on the wall. \n ${num} bottle of beer on the wall, ${num} bottle of beer.`)
            return ninetyNine(num - 1)        
        }else{
            console.log(`${num} bottles of beer on the wall, ${num} bottles of beer. \n Take one down and pass it around, ${num - 1} bottles of beer on the wall.`)
                return ninetyNine(num - 1)  
        }
    }
ninetyNine(99)

