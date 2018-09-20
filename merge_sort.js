// This merge sort implementation follows merge sort idea from CLRS, Chapter 2

function merge_sort (input){
    
    // Checking input length
    if (input.length>1) {
        
        var l_length = parseInt( (input.length + 1) / 2 )
        var left = []
        var right = []

        // Deviding  input
        for (i = 0; i < input.length; i++) { 
            if (i < l_length) {
                left[i] = input [i]
            } else {
                right[i-l_length] = input [i]
            }
        }
   
        // Conquering input
        if ( left.length==1 && right.length==1 ) {
            // Initial conquering
            var sortedArr =[]
            if ( left[0] < right [0] ) {
                sortedArr = [left[0], right [0]] 
            } else {
                sortedArr = [right[0], left [0]] 
            }
            return sortedArr

        } else {
            // Conquering following the initial conquering
             var sortedArrL = merge_sort(left)  
             var sortedArrR = merge_sort(right)
             
             var resultingArr = []
             var l = 0
             var r = 0
             
             // Merging sorted subarrays
             for (i = 0; i <  sortedArrL.length + sortedArrR.length ; i++) { 
                 if (r==sortedArrR.length) {
                     resultingArr[i] = sortedArrL[l]
                     l++  
                 } else if (l==sortedArrL.length) {
                     resultingArr[i] = sortedArrR[r]
                     r++  
                 } else {
                     if (sortedArrL[l] < sortedArrR[r]) {
                         resultingArr[i] = sortedArrL[l] 
                         l++
                     } else {
                         resultingArr[i] = sortedArrR[r]
                         r++
                     }
                 }
             }
             return resultingArr
        }
                    
    } else {
        return input
    }
        
}


// Running merge_sort function on a simple example
input = [38, 27, 43, 3, 9, 82, 10, 1]

sortedArr = merge_sort(input)
console.log('sortedArr: ' + sortedArr)
