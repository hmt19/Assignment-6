class Parentheses():

    def isValid(self, string):
        stack = []

        #Traverse through the string
        for char in string:
            #If the character is an opening bracket, push it to the stack
            if char in ["(", "{", "["]:
                stack.append(char)

            #If the character is a closing bracket
            else:
                #If the stack is empty, return False
                if len(stack) == 0:
                    return False

                #Pop the topmost element from the stack
                topElement = stack.pop()

                #Check if the popped element matches with the closing bracket
                if (topElement == "(" and char != ")"):
                    return False
                elif (topElement == "{" and char != "}"):
                    return False
                elif (topElement == "[" and char != "]"):
                    return False

        #If the stack is empty, return True
        if len(stack) == 0:
            return True
        else:
            return False
