# tuple with single element initialization
a = ('a', )
b = ('a')
print('a and its type', a, type(a)) # tuple
print('b and it type', b, type(b)) # str

s = 'gyf940517@gmail.com'
username, mail = s.split('@')
print(username)
print(mail)
print(type(username)) # str
print(type(mail)) # strq		


a = 4
b = 5
a, b = b, a
print(a) # 5
print(b) # 4

s = 'sdwesda'
s = tuple(s)
print(s) # ('s', 'd', 'w', 'e', 's', 'd', 'a')

# divmod(a, b)
# return tuple(a/b, a%b)
t = divmod(7, 3) # tuple of quotient and remainder
print(t) # (2, 1)
# or
quotient, remainder = divmod(7, 3)
print(quotient)
print(remainder)