def check_if_palindrome(data):
    if data == data[::-1]:
        return True


palindrome_data = input().split()
palindrome_to_check = input()
palindromes = []

for i in range(len(palindrome_data)):
    if check_if_palindrome(palindrome_data[i]):
        palindromes.append(palindrome_data[i])

print(palindromes)
print(f"Found palindrome {palindrome_data.count(palindrome_to_check)} times")
