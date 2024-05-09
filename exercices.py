import random
# prime numbers
def is_prime(number_to_check):
    if number_to_check <= 1:
        return False
    for i in range(2,int(number_to_check**0.5) + 1):
        if number_to_check%i == 0:
            return False
    
    return True
    
print(is_prime(4))
print(is_prime(1))
print(is_prime(5))
print(is_prime(7))
print(is_prime(17))
print(is_prime(9))

#factorial numbers
def factorial_number(number):
    if number < 0:
        raise ValueError("The number must be positive")
    if (number == 0):
        return 1
    result = 1
    for i in range (1,number+1):
        result *= i
    return result

print(factorial_number(1))
print(factorial_number(4))
print(factorial_number(0))
print(factorial_number(9))
try:
    factorial_number(-1)
except ValueError as ve:
    print(ve)

#fibonacci
def fibonacci(number):
    if number <= 1:
        return number
    
    return fibonacci(number-1) + fibonacci(number-2)


print(fibonacci(4))


#check letters in string
def count_matching_letters(words):
    if not words:
        return 0
    
    matching_letters = 0
    
    min_length = min(len(word) for word in words)
    
    for i in range(min_length):
        if all(word[i] == words[0][i] for word in words):
            matching_letters += 1
    
    return matching_letters

array = ["abc", "abd", "aac"]
result = count_matching_letters(array)
print("Number of matching letters in the same position:", result)

#check longest word
def check_longest_word(words):
    if not words:
        return 0
    
    word_info = {
        "word": "",
        "length":0,
    }
    for word in words:
        if word_info["length"] < len(word):
            word_info["length"] = len(word)
            word_info["word"] = word
    
    return word_info

words = ["apple", "banana", "orange", "kiwi"]
result = check_longest_word(words)
print("Longest word:", result)

#to check if a word is palindrome
def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("reconocer"))

# to check if a number is palindromic
def is_palindromic_number(number):
    number_string = str(number)
    return number_string == number_string[::-1]

print(is_palindromic_number(1234321))

#to get a array sorted by descending order
def sort_descending(numbers):
    numbers.sort(reverse = True)
    return numbers

print(sort_descending([24,89,1,67,23,22,23,7,14,45]))

#find repeated_elements
def find_repeated_elements(arrays):
    counts = {}

    for array in arrays:
        for element in array:
            if element in counts:
                counts[element] += 1
            else:
                counts[element] = 1

    return counts

# Ejemplo de uso:
arrays = [[1, 2, 3,10], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9]]
repeated_elements = find_repeated_elements(arrays)
print("Elementos que se repiten:", repeated_elements)


#find largest number
def find_largest_number(numbers):
    if not numbers:
        return 0
    largest_number = 0

    for number in numbers:
        if largest_number <= number:
            largest_number = number

    return largest_number

print(find_largest_number([1,2,3,5,7,4,9,23,19,3,89,5]))

#counts vowels in a given string
def count_vowels(word):
    lower_word = word.lower()
    vowels = ["a","e","i","o","u"]
    vowels_count = 0

    for letter in lower_word:
        if letter in vowels:
            vowels_count += 1

    return vowels_count

print(count_vowels("AAAAAA"))

#to check if the parenthesis are in the right position
def validate_parentheses(string):
    stack = []

    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()

    return not stack

print(validate_parentheses("()()"))
print(validate_parentheses(")("))
print(validate_parentheses("((()"))
print(validate_parentheses("()("))
print(validate_parentheses("()(()"))

#caesar cipher
def caesar_cipher(word,number):
    if not word:
        return word
    
    if number == 0:
        return word
    
    lower_word = word.lower()
    converted_word = ""
    for letter in lower_word:
        ascii_character = ord(letter)
        reasigned_ascii = ascii_character + number
        if reasigned_ascii >= 122:
            reasigned_ascii -= 26
        reasigned_letter = chr(reasigned_ascii)
        converted_word += reasigned_letter
    return converted_word

print(caesar_cipher("xyz",3))

#delete duplicate elements
def delete_duplicate_elements(data_to_clear):
    return list(set(data_to_clear))

given_numbers = [1, 2, 3, 2, 4, 5, 6, 4]
clear_data = delete_duplicate_elements(given_numbers)
print("Lista original:", given_numbers)
print("Lista sin duplicados:", clear_data)


def clear_text(text):
    return text.lower().replace(',', '').replace('.', '').replace('!', '').replace('?', '').replace(':', '').replace(';', '')
#words count
def count_words(text):
    cleaned_text = clear_text(text)
    splited_text = cleaned_text.split()
    words_info = {}

    for word in splited_text:
        words_info[word] = words_info.get(word, 0) + 1

    return words_info
        


print(count_words("mesa! ,silla. mesa,,, silla!! mesa    mesa"))

#multiplication

def max_product(numbers):
    if len(numbers) < 2:
        return 0
    numbers.sort()
    return max(numbers[0]*numbers[1],numbers[-1]*numbers[-2])

numbers = [1, 3, 2, 5, 7, -1, 4, 0]
print("Máximo producto de dos números en la lista:", max_product(numbers))

numbers = [1, 3, 2, -6, -7, 8, -1, 4, 0]
print("Máximo producto de dos números en la lista:", max_product(numbers))



#push, pop y peek y push in stack
class Stack:
    def __init__(self):
        self.items = []
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def push(self,item):
        self.items.append(item)

stack = Stack()
stack.push(5)
stack.push(10)
stack.push(15)
stack.push(20)
stack.push(25)
print(stack.peek())
print(stack.pop()) 
print(stack.peek())

# Queue

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.append(item)

    def is_empty(self):
        return len(self.items) == 0
    
    def dequeue(self):
        if self.is_empty():
            return None
        
        return self.items.pop(0)
    
q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())
print(q.dequeue())

print(q.is_empty())

print(q.dequeue())

print(q.is_empty())


#  exceptions

class OutOfStockError(Exception):
    def __init__(self,quantity):
        self.message = f"There are only {quantity} products they buy couldnt be done"

class ProductNotFoundError(Exception):
    def __init__(self):
        self.message = "This product doesnt exists"

class Shop():
    def __init__(self):
        self.__products = {
            "chair" : random.randint(5,10),
            "table" : random.randint(5,10),
        }
    
    def buy(self,quantity,product):
        if not product in self.__products:
            raise ProductNotFoundError
        if quantity > self.__products[product]:
            raise OutOfStockError(self.__products[product])
        self.__products[product] -= quantity
        return "Buy successful"

my_shop = Shop()
try:
    buy_result = my_shop.buy(41,"chair")
    print(buy_result)
except ProductNotFoundError as exists:
    print(exists.message)
except OutOfStockError as stock:
    print(stock.message)


#inheritance
class Animal:
    def __init__(self, species):
        self.__species = species

    def get_species(self):
        return self.__species

    def speak(self):
        return "GRRR"

class Dog(Animal):
    def __init__(self, species, breed):
        super().__init__(species)
        self.__breed = breed

    def get_breed(self):
        return self.__breed

    def speak(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, species, color):
        super().__init__(species)
        self.__color = color

    def get_color(self):
        return self.__color

    def speak(self):
        return "Meow!"


dog = Dog("Dog", "Labrador")
print(dog.get_species())
print(dog.get_breed())
print(dog.speak())

cat = Cat("Cat", "Black")
print(cat.get_species())
print(cat.get_color())
print(cat.speak())


def is_pachydermism(phrase):
    return len(set(phrase)) == 26

print(is_pachydermism("abcdefghijklmnopqrstuvwxyz"))
print(is_pachydermism("abcdefghijklmnopqrstuvwxyy"))

'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    return []
        
print(two_sum([2,11,7,15],18))

# Can you come up with an algorithm that is less than O(n2) time complexity?

def two_sum_v2(nums,target):
    checker = {}
    for i in range(len(nums)):
        remainder = target - nums[i]
        if remainder in checker:
            return [checker[remainder],i]
        checker[nums[i]] = i
    return []

print(two_sum_v2([2,11,7,15],22))


# Roman to integer
def roman_to_integer(roman):
    roman_to_arabic = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
    }
    common_cases = {
        "IV" : 4,
        "IX" : 9,
        "XL" : 40,
        "XC" : 90,
        "CD" : 400,
        "CM" : 900,
    }
    solution = 0
    i = 0
    while i < len(roman):
        if i + 1 < len(roman) and roman[i] + roman[i + 1] in common_cases:
            solution += common_cases[roman[i] + roman[i + 1]]
            i += 2 
        else:
            solution += roman_to_arabic[roman[i]]
            i += 1
    return solution



print(roman_to_integer("MCMXCIV"))

def all_start_with(words,start):
    return all(word.startswith(start) for word in words)

def longest_common_prefix(words):
    first_word = words[0]
    longest_prefix = ""

    for i, letter in enumerate(first_word):
        prefix_to_check = first_word[:i + 1]
        if all_start_with(words, prefix_to_check):
            longest_prefix = prefix_to_check
        else:
            break

    return longest_prefix
    


strs = ["flower", "flow", "flight","flail"]
print(longest_common_prefix(strs))


def first_occurrence(haystack,needle):
    needle_length = len(needle)
    haystack_length = len(haystack)
    result = -1
    for i in range(0,haystack_length - needle_length + 1):
        haystack_part = haystack[i:i+needle_length]
        if haystack_part == needle:
            return i
    return result

print(first_occurrence("xsadbutsad","sad"))
print(first_occurrence("leetcode","leeto"))


'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''

def search_index(nums, target):
    left = 0
    right = len(nums) - 1
        
    while left <= right:
        mid = left + (right - left) // 2
            
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left
    
print(search_index([1,3,5,6], 5))  
print(search_index([1,3,5,6], 2))  

'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.
'''
def length_last_word(sentence):
    new_sentence = " ".join(sentence.split())
    words = new_sentence.split(" ")
    return len(words[-1])
    

print(length_last_word("   fly me   to   the moon  "))

'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit 
of the integer. The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
'''
def plus_one(numbers):
    if numbers[-1] != 9:
        numbers[-1] += 1
        return numbers
    if len(numbers) == 1 and numbers[0] == 9:
        return [1,0]
    if numbers[-1] == 9:
        numbers[-2] += 1
        numbers[-1] += 1
        return numbers
    numbers[-1] += 1
    return numbers

print(plus_one([1,2,3]))
print(plus_one([4,3,2,2]))
print(plus_one([9]))

def add_binary(a,b):
    longest_len = max(len(a),len(b))
    a = a.zfill(longest_len)
    b = b.zfill(longest_len)
    result = ""
    carry = 0

    for i in range(longest_len -1,-1,-1):
        digit_sum = int(a[i]) + int(b[i]) + carry
        if digit_sum == 0 or digit_sum == 1:
            result = str(digit_sum) + result
            carry = 0
        elif digit_sum == 2:
            result = "0" + result
            carry = 1
        else:
            result = "1" + result
            carry = 1
    if carry == 1:
        result = "1" + result
    return result
print(add_binary("1100101","100101011"))


def climb_stairs( n):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1  
        
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        
    return dp[n]

print(climb_stairs(4))

def pascal_triangle(num_rows):
    triangle = [[1]]
    for i in range(1, num_rows):
        new_row = [0] * (i + 1)
        new_row[0] = 1
        new_row[-1] = 1
        
        for j in range(1, len(new_row) - 1):
            new_row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        
        triangle.append(new_row)
    
    return triangle

print(pascal_triangle(5))  


'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy
 one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

def max_profit(prices):
    profit = 0
    for i in range(len(prices)):
        for j in range(len(prices)):
            if i != j and j > i:
                if prices[j] - prices[i] > profit:
                    profit = prices[j] - prices[i]
    return profit

print(max_profit([7,1,5,3,6,4]))

# Do this in less than O(n2)

def max_profit_2(prices):
    min_price = prices[0]
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    
    return max_profit

print(max_profit_2([7,1,5,3,6,4]))

'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
'''

def single_number(numbers):
    result = 0
    for number in numbers:
        result ^= number
    return result
    
print(single_number([2,2,1,3,3]))

'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
'''

def majority_element(nums):
    nums.sort()
    nums_len = len(nums)
    return nums[nums_len//2]



print("El numero que mas se repite es " + str(majority_element([2,2,1,1,1,2,2])))

#Could you solve the problem in linear time and in O(1) space?
# Moore Voting solution

def majority_element_2(nums):
    candidate = 0
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    return candidate

print("El numero que mas se repite es " + str(majority_element_2([3,2,3])))
print("El numero que mas se repite es " + str(majority_element_2([2,2,1,1,1,2,2])))

'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
'''

def happy_number(number):
    string_number = str(number)
    next_number = 0
    visited = set()
    while True:
        for digit in string_number:
            current_digit = int(digit)
            next_number = next_number + current_digit**2
        
        if next_number == 1:
            return True
        
        if next_number in visited:
            return False
        
        string_number = str(next_number)
        visited.add(next_number)
        next_number = 0
    

print(happy_number(19))
print(happy_number(2))