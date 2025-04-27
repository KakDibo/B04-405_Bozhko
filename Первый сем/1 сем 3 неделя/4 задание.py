def triangle():
	a = input().split()
	n = int(a[0])
	s = a[1]

	for i in range(n):
		if i <= n // 2 - 1:
			print(s*(i+1))
		else:
			print(s*(n-i))