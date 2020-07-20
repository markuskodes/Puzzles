# Question
'''Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.'''

# Solution Strategy
'''Used a hard ware oriented ripple carry adder scheme. The rippleCarry
function is a module that takes in the two bits and a carry in bit. It 
outputs the bit sum and the carry out bit. Then the addBinary function
goes through the two binary strings base by base to construct the answer.'''

class Solution:
    def rippleCarry(self, bit_a, bit_b, carry_in):
        if bit_a + bit_b + carry_in == 1:
            return 1,0 #bit_sum, carry_out
        elif bit_a + bit_b + carry_in == 0:
            return 0,0
        elif bit_a + bit_b + carry_in >1:
            return (bit_a + bit_b + carry_in) % 2,1

    def addBinary(self, a: str, b: str) -> str:
        #assume a is the shorter string
        len_a = len(a)
        len_b = len(b)
        
        if len_a > len_b:
            return self.addBinary(b,a)
        
        output = []
        carry = 0
        i = 0
        a = a[::-1]
        b = b[::-1]
        
        while i < len_b:
            
            if i < len_a:
                bit_sum, carry = self.rippleCarry(int(a[i]),int(b[i]),carry)
                output = [str(bit_sum)] + output
                i += 1
            else:
                bit_sum, carry = self.rippleCarry(0,int(b[i]),carry)
                output = [str(bit_sum)] + output
                i += 1

        if carry == 1:
            output = ["1"] + output
            
        return "".join(output)