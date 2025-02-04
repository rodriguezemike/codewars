#https://www.codewars.com/kata/53d40c1e2f13e331fc000c26/

'''
From The Wizard book SICP

Exercise 1.19.   There is a clever algorithm for computing the Fibonacci numbers in a logarithmic number of steps. Recall the transformation of the state variables a and b in the fib-iter process of section 1.2.2: a  a + b and b  a. Call this transformation T, and observe that applying T over and over again n times, starting with 1 and 0, produces the pair Fib(n + 1) and Fib(n). In other words, the Fibonacci numbers are produced by applying Tn, the nth power of the transformation T, starting with the pair (1,0). Now consider T to be the special case of p = 0 and q = 1 in a family of transformations Tpq, where Tpq transforms the pair (a,b) according to a  bq + aq + ap and b  bp + aq. Show that if we apply such a transformation Tpq twice, the effect is the same as using a single transformation Tp'q' of the same form, and compute p' and q' in terms of p and q. This gives us an explicit way to square these transformations, and thus we can compute Tn using successive squaring, as in the fast-expt procedure. Put this all together to complete the following procedure, which runs in a logarithmic number of steps:41


(define (fib n)
  (fib-iter 1 0 0 1 n))
(define (fib-iter a b p q count)
  (cond ((= count 0) b)
        ((even? count)
         (fib-iter a
                   b
                   <??>      ; compute p'
                   <??>      ; compute q'
                   (/ count 2)))
        (else (fib-iter (+ (* b q) (* a q) (* a p))
                        (+ (* b p) (* a q))
                        p
                        q
                        (- count 1)))))
'''

def fib(n):
	a,b,p,q = 1, 0, 0, 1
	sign = -1 if (n < 0) & (abs(n) % 2 == 0) else 1
	n = abs(n)
	while True:
		if n == 0:
			return b*sign
		elif n % 2 == 0:
			p, q = (p**2 + q**2), (q**2 + 2*p*q)
			n/=2
		else:
			a, b = (b*q + a*q + a*p), (b*p + a*q)
			n -= 1

def fib_mat_style(n):
  if n < 0: return (-1)**(n % 2 + 1) * fib(-n)
  a = b = x = 1
  c = y = 0
  while n:
    if n % 2 == 0:
      (a, b, c) = (a **2 + b **2,
                   a * b + b * c,
                   b **2 + c **2)
      n /= 2
    else:
      (x, y) = (a * x + b * y,
                b * x + c * y)
      n -= 1
  return y

def fib_mat_expo(n):
    def matrix_multiply(a, b):
        first_row = [
            a[0][0] * b[0][0] + a[0][1] * b[1][0],
            a[0][0] * b[0][1] + a[0][1] * b[1][1],
        ]
        second_row = [
            a[1][0] * b[0][0] + a[1][1] * b[0][1],
            a[1][0] * b[0][1] + a[1][1] * b[1][1],
        ]
        return [first_row, second_row]

    def matrix_power(matrix, exponent):
        if exponent == 1:
            return matrix
        else:
            result = matrix_power(matrix, exponent // 2)
            result = matrix_multiply(result, result)
            if exponent % 2 == 1:
                result = matrix_multiply(result, matrix)
            return result

    matrix = [[0, 1], [1, 1]]
    result =  matrix_power(matrix, abs(n) + 1)[0][0]
    sign = -1 if n < 0 and n % 2 == 0 else 1
    return result * sign
