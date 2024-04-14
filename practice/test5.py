def count_vowels(sentence):
    vowels = 'a,e,i,o,u,A,E,I,O,U'
    vowel_count = 0
    
    for char in sentence:
        if char in vowels:
            vowel_count += 1
    return vowel_count

def main():
    sentence = input("Enter a sentence: ")
    
   
    total_vowels = count_vowels(sentence)
    
   
    print("Total number of vowels:", total_vowels)

if __name__ == "__main__":
    main()