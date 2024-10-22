# Write a Python program to compute following operations on String:
# a) To display word with the longest length
# b) To determines the frequency of occurrence of particular character in the string
# c) To check whether given string is palindrome or not 
# d) To display index of first appearance of the substring
# e) To count the occurrences of each word in a given string

def word_with_longest_length(s):
    max_len = 0
    longest_word = ""
    current_word = ""
    
    for char in s + ' ':
        if char != ' ':
            current_word += char
        else:
            if len(current_word) > max_len:
                max_len = len(current_word)
                longest_word = current_word
            current_word = ""
    
    return longest_word

def frequency_of_character(s, char):
    count = 0
    for c in s:
        if c == char:
            count += 1
    return count

def is_palindrome(s):
    cleaned_s = ""
    for char in s:
        if char != ' ':
            cleaned_s += char.lower()
    
    left, right = 0, len(cleaned_s) - 1
    while left < right:
        if cleaned_s[left] != cleaned_s[right]:
            return False
        left += 1
        right -= 1
    
    return True

def index_of_first_substring(s, substring):
    n = len(s)
    m = len(substring)
    
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if s[i + j] != substring[j]:
                match = False
                break
        if match:
            return i
    
    return -1

def count_word_occurrences(s):
    word_count = {}
    current_word = ""
    
    for char in s + ' ':
        if char != ' ':
            current_word += char.lower()
        else:
            if current_word in word_count:
                word_count[current_word] += 1
            else:
                word_count[current_word] = 1
            current_word = ""
    
    return word_count

# Example usage:
string = input("Enter Your String : ")

flag=1
while flag==1:
    print("1. To display word with the longest length")
    print("2. To determines the frequency of occurrence of particular character in the string")
    print("3. To check whether given string is palindrome or not ")
    print("4. To display index of first appearance of the substring")
    print("5. To count the occurrences of each word in a given string")
    print("6. EXIT")
    ch=int(input("enter your choice: "))
    if ch==1:
        print("Word with the longest length:", word_with_longest_length(string))
        m=input(" Do you want to continue:(YES/NO): ")
        if m=='yes':
            flag=1
        else:
            flag=0
    
    elif ch==2:
        s= input("enter Charactor to find frequency : ")
        print("Frequency of :",s,frequency_of_character(string, s))
        m=input(" Do you want to continue:(YES/NO): ")
        if m=='yes':
            flag=1
        else:
            flag=0
    elif ch==3:
        print("Is the string a palindrome?", is_palindrome(string))
        m=input(" Do you want to continue:(YES/NO): ")
        if m=='yes':
            flag=1
        else:
            flag=0
    elif ch==4:
        substring=input("enter substring ")
        print("Index of first appearance of substring: ", index_of_first_substring(string,substring ))
        m=input(" Do you want to continue:(YES/NO): ")
        if m=='yes':
            flag=1
        else:
            flag=0
    elif ch==5:
        print("Word occurrences: ", count_word_occurrences(string))
        m=input(" Do you want to continue:(YES/NO): ")
        if m=='yes':
            flag=1
        else:
            flag=0
            
    elif ch==6:
        print("exit")
        flag=0
    else:
        print("invalid choice")
    
    





