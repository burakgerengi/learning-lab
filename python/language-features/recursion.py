def countdown(n):
    if n == 0:  # base case: stop
        return

    print(n)
    countdown(n - 1)  # recursive call


countdown(10)  # run
