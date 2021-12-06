# Part I ­ Implement the Fibonnaci Sequence
def fib(n) :
	if n <= 1 :
		return n
	return fib(n -1) + fib(n -2)

# Part II ­ Implement Euclid’s GCD Algorithm
def gcd2(a, b):
	if a == 0:
		return b
	elif b == 0:
		return a
    
	return gcd2(b, a % b)

# Part III ­ String Comparison
def compareTo(s1, s2):
    if s1 == '' and s2 == '':
        return 0
    elif ord(s1[0]) > ord(s2[0]):
        return 0 + ord(s1[0])
    elif ord(s1[0]) < ord(s2[0]):
        return 0 - ord(s2[0])
    elif s1[1:2] == '' and not s2[1:2] == '':
        return 0 - ord(s2[0])
    elif s2[1:2] == '' and not s1[1:2] == '':
        return 0 + ord(s1[0])
    elif s1[1:2] == '' and s2[1:2] == '':
        return 0
    else:
        return compareTo(s1[1:], s2[1:])
if __name__ == "__main__":
    fibo = input("Enter value of N for fibonacci series: ")
    
    print(fibo+'th value of the fibonacci series is: ',fib(int(fibo)))

    print('GCD is:',gcd2(int(input('Enter first Number: ')), int(input('Enter second Number: '))))
    
    print('Value returned after comparison is: ',compareTo(input("Enter first string: "), input('Enter Second string: ')))
    
