class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        
        # Multiply each digit from right to left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                digit1 = int(num1[i])
                digit2 = int(num2[j])
                
                # Current multiplication product
                product = digit1 * digit2
                
                # Positions in the result array
                p1, p2 = i + j, i + j + 1
                
                # Add to existing value (including carry)
                total = product + res[p2]
                
                res[p2] = total % 10          # Store current digit
                res[p1] += total // 10        # Carry over to the left position
                
        # Convert result array to string and strip leading zeros
        result_str = "".join(map(str, res))
        return result_str.lstrip("0")