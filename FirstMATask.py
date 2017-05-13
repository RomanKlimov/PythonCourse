
print("Enter number of factors:")
entered = 1
n = 0
while entered == 1:
	n = input()
	try:
		n = int(n)
		if n > 0:
			entered = 0
		else:
			print('You entered the negative number')
					
	except ValueError:
		print('Seems like you did\'t write a number')

file = open('index.html', 'w')
file.write('''<!DOCTYPE html>
\n<html>
\n\t<head>
\n\t\t<title>Multiplication table</title>
\n\t</head>
\n\t<body>\n\t\t<h1 align = \'center\'>Multiplication table ''' + str(n) + ''' X ''' + str(n) + '''</h1>\n\t\t<table cellspacing=\"5\" cellpadding=\"10\" align = \'center\'>''')
r = ''
for i in range(1, n+1):
	file.write('\n\t\t<tr>')
	for j in range(1,n+1):
		if (i == 1 or j == 1 or i == j):
			r = ' bgcolor = \'#ffcc00\''
		file.write('\n\t\t<td align = \'center\'' + r + '>' + str(i*j))
		r = ''
	file.write('\n\t\t</tr>')

file.write('\n\t\t</table>\n\t</body>')
file.close()