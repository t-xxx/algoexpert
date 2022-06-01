def getNthFib(n):
    last_l = [0, 1]
    counter = 3
    while counter <= n:
	    last_fib = last_l[0] + last_l[1]
        last_l[0] = last_l[1]
        last_l[1] = last_fib
        counter += 1
    return last_l[1] if n > 1 else last_l[0]