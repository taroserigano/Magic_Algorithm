/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var reverseKGroup = function(head, k) {
  if (!head || k < 2) return head;
  
  var count = 0;
  var current = head;
  var prev = head;
  var next = null;
    
  
  
  while (current && count < k) {
    current = current.next;
    count++;
  }

  if (count === k) {
        
    current = reverseKGroup(current, k);
    while (count-- > 0) {
    console.log(" ***************************** ")
        // 1, 2, 3, 4, 5
        // current starts from = 4, with prev and next = 1  
        // and then next moves to 2, prev's next connected to current
        // current becomes prev, 
        // prev moves on -> to the next = 2
      next = prev.next;
            console.log(next.val + " next is prev's next now ")

      prev.next = current;
             console.log(current.val + " prev next connected to current now")
      current = prev;
            console.log(prev.val + " prev itself is still")
             console.log(current.val + " current")

      prev = next;
            console.log(prev.val + " prev now replaced by current")
    }
    prev = current;
              console.log("prev " + prev.val)

  }
  
  return prev;
};



