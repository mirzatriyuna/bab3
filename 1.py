hours = raw_input('Enter Hours : ')
rate = raw_input('Enter Rate : ')

x = float(hours)
y = float(rate)

if x < 40:
   print float(x * y)
else :
   a = 40 * y	 	#menampung perkalian rate sebanyak 40 hours
   b = x - 40	 	#menampung banyaknya hours yang lebih dari 40
   c = (y*3/2) * b
   e = a + c		#hasil akhir
   print ('pay :'), float(e)
