
# "(1+(4+5+2)-3)+(6+8)"

# Declare 4 and Digit, +-, () 


class Solution:
    def calculate(self, s: str) -> int:
        # total = total amount
        # cur = current value to be added to total 
        # sign = + or - ? Add or Deduct 
        # stack ( and also either + or - before "(" 
      
        total, cur, sign, stack = 0, 0, 1, [] 

        for c in s: 
            
            # Digit 
            if c.isdigit():
              # 35, multiply * 10, 30 + 5 
                cur = cur * 10 + int(c) 
            # Calculate
            # total first and then + or - sign
            elif c in "+-": 
                total += (cur * sign) 
                cur = 0 
                
                if c == "-":
                    sign = -1
                    
                else: 
                    sign = 1
            # stack Total & Sign 
            # go back to default 
            elif c =="(": 
                stack.append(total)
                stack.append(sign)
                total = 0
                sign = 1 
            # calculate Total
            # Pop Sign and Total
            elif c == ")": 
                total += (cur * sign) 
                total *= stack.pop() 
                total += stack.pop() 
                cur = 0 
               # add remaining 
        return total + (cur * sign) 		

      

