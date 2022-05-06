# recebe um número como arametro e devolve a palavra conforme o numero

def fizzbuzz(n):

	if n%3 == 0 and n%5 != 0:
		return 'Fizz'
	elif n%5 == 0 and n%3 != 0:
		return 'Buzz'
	elif n%3 == 0 and n%5 == 0:
		return 'FizzBuzz'
	else:
		return n



n = int(input('Digite um número: '))
print(fizzbuzz(n))