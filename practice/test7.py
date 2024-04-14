def is_palindrome(string):
   
    string = string.lower().replace(" ", "")
    left = 0
    right = len(string) - 1
    
    while left < right:
        
        if string[left] != string[right]:
            return False
        
        left += 1
        right -= 1
    
    return True

def main():

    user_input = input("Enter a string: ")
    if is_palindrome(user_input):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

if __name__ == "__main__":
    main()
