import re
import math

class Addition:
    def __init__(self, one, two):
        self.one = float(one)
        self.two = float(two)

    def description(self):
        return "Add numbers"

    def calculate(self):
        return self.one + self.two
class Subtraction:
    def __init__(self, one, two):
        self.one = float(one)
        self.two = float(two)

    def description(self):
        return "Subtract numbers"
    def calculate(self):
        return self.one - self.two
class Multiplication:
    def __init__(self, one, two):
        self.one = float(one)
        self.two = float(two)
    def description(self):
        return "Multiply numbers"
    def calculate(self):
        return self.one * self.two
class Division:
    def __init__(self, one, two):
        self.one = float(one)
        self.two = float(two)
    def description(self):
        return "Divide numbers"
    def calculate(self):
        if self.two == 0:
            raise ValueError("Cannot divide by zero")
        return self.one / self.two
class Remainder: #Modulus
    def __init__(self, one, two):
        self.one = float(one)
        self.two = float(two)
    def description(self):
        return "Remainder of division"
    def calculate(self):
        if self.two == 0:
            raise ValueError("Cannot divide by zero")
        return self.one % self.two
class RoundedDivision: #Floor Division
    def __init__(self, one, two):
        self.one = int(one)
        self.two = int(two)
    def description(self):
        return "Rounded Division"
    def calculate(self):
        if self.two == 0:
            raise ValueError("Cannot divide by zero")
        return self.one // self.two
class Exponents:
    def __init__(self, one, two):
        self.one = float(one)
        self.two = float(two)
    def description(self):
        return "Raise number to exponent"
    def calculate(self):
        return self.one ** self.two
class ScaleConverter:
    def __init__(self, units_from, units_to, factor):
        self.units_from = float(units_from)
        self.units_to = float(units_to)
        self.factor = float(factor)
    def description(self):
        return f"Convert {self.units_from} to {self.units_to}"
    def calculate(self, value):
        return value * self.factor
class ScaleAndOffsetConverter(ScaleConverter):
    def __init__(self, units_from, units_to, factor, offset):
        ScaleConverter.__init__(self, units_from, units_to, factor)
        self.offset = offset
    def calculate(self, value):
        return value * self.factor + self.offset
class CelsiusToFahrenheit:
    def __init__(self, celsius):
        self.celsius = float(celsius)
    def description(self):
        return "Convert Celsius to Fahrenheit"
    def calculate(self):
        return (self.celsius * 9/5) + 32
class FahrenheitToCelsius:
    def __init__(self, fahrenheit):
        self.fahrenheit = float(fahrenheit)
    def description(self):
        return "Convert Fahrenheit to Celsius"
    def calculate(self):
        return (self.fahrenheit - 32) * 5/9
class PhoneNumbers:
    def __init__(self):
        self.r = re.compile(r"\d")
    def pretty_format(self, phone_number):
        digits = self.r.findall(str(phone_number))
        if len(digits) < 10:
            raise ValueError("Phone number must contain at least 10 digits")
        area_code = "".join(digits[-10:-7])
        first_3 = "".join(digits[-7:-4])
        last_4 = "".join(digits[-4:])
        return f"({area_code}) {first_3}-{last_4}"
class SquareRoot:
    def __init__(self, one):
        self.one = one
    def description(self):
        return "Square root of a num"
    def calculate(self):
        return math.sqrt(self.one)
class CubeRoot:
    def __init__(self, one):
        self.one = one
    def description(self):
        return "Cube root of a num"
    def calculate(self):
        return math.cbrt(self.one)
class Square:
    def __init__(self, one):
        self.one = one
    def description(self):
        return "Squaring of a num"
    def calculate(self):
        return self.one ** 2
class Cube:
    def __init__(self, one):
        self.one = one
    def description(self):
        return "Cubing of a num"
    def calculate(self):
        return self.one ** 3
class FizzBuzzer: # Book
  def __init__(self):
    self.n = 0
  def foo(self,_):
    self.n += 1
    if (self.n % 3)  == 0:
      x = "buzz"
    else: x = "fizz"
    return x
class HeckerTranslate:
    def __init__(self):
        self.r = re.compile(r'[\u4e00-\u9fff]+')
    def replace_7t(self, s):
        return s.replace('7', 't')
    def replace_3e(self, s):
        return s.replace('3', 'e')
    def replace_6g(self, s):
        return s.replace('6', 'g')
    def replace_4a(self, s):
        return s.replace('4', 'a')
    def sub_chinese(self, s):
        return self.r.sub(" ", s)
class isPalindrome: #From book
    def __init__(self, word):
        self.word = word
    def description(self):
        return "Checks is a word is a palindrome."
    def check(self):
        from collections import deque
        dq = deque(self.word)
        while len(dq) > 1:
            if dq.popleft() != dq.pop():
                return False
        return True


class CaesarCipher:
    def __init__(self, shift=3):
        self.shift = shift % 26

    def description(self):
        return f"Caesar cipher with shift {self.shift}"

    def encrypt(self, text):
        result = ""
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted = (ord(char) - base + self.shift) % 26 + base
                result += chr(shifted)
            else:
                result += char
        return result

    def decrypt(self, text):
        result = ""
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted = (ord(char) - base - self.shift) % 26 + base
                result += chr(shifted)
            else:
                result += char
        return result