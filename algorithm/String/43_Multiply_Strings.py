class Solution:
    def multiply(self, num1, num2):
        product = [0] * (len(num1) + len(num2)) #placeholder for multiplication ndigit by mdigit result in n+m digits
        position = len(product)-1 # position within the placeholder

        for n1 in num1[::-1]:
            tempPos = position
            for n2 in num2[::-1]:
                product[tempPos] += int(n1) * int(n2) # ading the results of single multiplication
                product[tempPos-1] += product[tempPos]//10 # bring out carry number to the left array
                product[tempPos] %= 10 # remove the carry out from the current array
                tempPos -= 1 # first shifting the multplication to the end of the first integer
            position -= 1 # then once first integer is exhausted shifting the second integer and starting


        # once the second integer is exhausted we want to make sure we are not zero padding
        pointer = 0 # pointer moves through the digit array and locate where the zero padding finishes
        while pointer < len(product)-1 and product[pointer] == 0: # if we have zero before the numbers shift the pointer to the right
            pointer += 1

        return ''.join(map(str, product[pointer:])) # only report the digits to the right side of the pointer