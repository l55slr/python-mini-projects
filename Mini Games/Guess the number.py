guess = 0
tries = 0
while guess != 6 and tries < 5:
  guess = int(input("guess the number in my mind: "))
  tries = tries +1
if guess != 6:
  print("You hit your limit")
else:
  print("you nailed it")
