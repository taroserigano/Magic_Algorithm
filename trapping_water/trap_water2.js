 
function findWater(arr,n)
{
        // initialize output
        let result = 0;
  
        // maximum element on left and right
        let left_max = 0, right_max = 0;
  
        // indices to traverse the array
        let left = 0, right = n - 1;
  
        while (left <= right) {
            if (arr[left] < arr[right]) {
                if (arr[left] > left_max)
  
                    // update max in left
                    left_max = arr[left];
                else
  
                    // water on curr element =
                    // max - curr
                    result += left_max - arr[left];
                left++;
            }
            else {
                if (arr[right] > right_max)
  
                    // update right maximum
                    right_max = arr[right];
  
                else
                    result += right_max - arr[right];
                right--;
            }
        }
  
        return result;
}
 
 /* Driver program to test above function */
let arr=[0, 1, 0, 2, 1, 0, 1,
                      3, 2, 1, 2, 1];
let n = arr.length;
document.write("Maximum water that "
                           + "can be accumulated is "
                           + findWater(arr, n));// Online Javascript Editor for free
// Write, Edit and Run your Javascript code using JS Online Compiler
