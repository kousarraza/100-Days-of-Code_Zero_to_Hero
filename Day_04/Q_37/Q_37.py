# 37. Write a Python program to convert seconds into hours ,mintues & seconds.

sec=int(input("Enter number of Seconds: "))

hours=sec//3600
mint=(sec % 3600) //60
remaining_sec=sec%60

print("Hours: ",hours)
print("Mintues: ",mint)
print("Seconds ",remaining_sec)
