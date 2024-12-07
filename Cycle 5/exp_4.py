import palindrome

def longest_palindromic_substring(s: str) -> str:
    longest = ""

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if palindrome.is_palindrome(substring) and len(substring) > len(longest):
                longest = substring

    return longest

input_string = input("Enter a string: ")

result = longest_palindromic_substring(input_string)

print(f"The longest palindromic substring is: {result}")
