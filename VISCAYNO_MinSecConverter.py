s = int(input("Enter an integer in seconds: "))

sec = s % 60
min = s // 60

print(s, "seconds is", min, "minutes and", sec, "seconds")
