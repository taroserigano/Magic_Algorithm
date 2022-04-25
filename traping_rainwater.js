const elevationArray = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]

/*
1. Identify the pointer with the lesser value
2. Is this pointer value greater than or equal to max on that side
  yes -> update max on that side
  no -> get water for pointer, add to total
3. move pointer inwards
4. repeat for other pointer
 */

const getTrappedRainwater = function(heights) {

  let left = 0, 
      // very RIGHT END 
      right = heights.length - 1, 
      
      totalWater = 0, maxLeft = 0, maxRight = 0;
  
  // run from the LEFT to RIGHT  end 
  while(left < right) {
    // if this point lower than the RIGHT END 
    if(heights[left] <= heights[right]) {
      // if this point, higher than the current MAX LEFT 
      if(heights[left] >= maxLeft) { 
        // MAX LEFT is this point
        maxLeft = heights[left]
      } else { 
        // 
        totalWater += maxLeft - heights[left];
      }
      left++;
    } else {
      if(heights[right] >= maxRight) {
          maxRight = heights[right];
      } else {
          totalWater += maxRight - heights[right];
      }
        
      right--;
    }
  }

  return totalWater;
}


console.log(getTrappedRainwater(elevationArray));



----------------------------------------------------------------------

L= 0, R = height-1
maxL = 0, maxR = 0 


-Run from Left to Right
	IF: L point <= R point?
		IF: L point >= maxL ?
			maxLeft is now = L point
		ELSE:
			TotalWater += maxLeft - L point
			
			Left++ 
			
	ELSE: 
		IF: R point >= maxRight?	
			maxRight = R point 
		ELSE: 
			TotalWater += maxRight - R point 
		
			Right--
			
- Return TotalWater			
			
			















