class Solution:
    def decodeString(self, s: str) -> str:
        '''
        The last calculated string must be included. 

        Iterate over, add everything, the moment we see a closing bracking, we pop and append while we don't see a "["

        we then reverse the output and hav a number. if there is a number to the left of the "[" we multiple the string by that can append it

        I'm assuming that the number will only appear outside the first opening bracket not anywhere else in the string

        '''
        stack = []
        for c in s: #iterate over the characters
            print(stack)
            if c == "]": #If current char is a closing bracket
                temp = []
                while stack[-1] != "[": #Iterate over all the char in between the closing bracket and the opening brack store them
                    temp.append(stack.pop())
                
                temp = temp[::-1] #Reverse since it comes in backwards
                stack.pop() #Since we know its "["

                if stack and type(stack[-1]) is int: #We need to check if we have a coefficient
                    stack.append(''.join(temp)*stack.pop())  #If we do append the coefificent times the characters
                else:
                    stack.append(''.join(temp)) #Otherwise, just append the final temp

            elif c in set('0123456789'): #If the char is a number
                if not stack or str(stack[-1]) not in set('0123456789'): #Check if its the first
                    stack.append(int(c))
                else:
                    print("Here where prev isnt number: ", stack, c)
                    stack[-1] = stack[-1]*10+int(c) #If its not the first
                
            else:
                stack.append(c) #If the character isnt the end of a bracket, and isnt a number, we just add it since its a normal character
            
        return ''.join(stack)
                
