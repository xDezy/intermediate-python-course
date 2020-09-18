import random
def main():
  dice_rolls = int(input('How many dice would you like to roll?\n'))
  dice_size = int(input('How many sides'))
  dice_sum = 0
  for i in range(0,dice_rolls):
    roll = random.randint(1,dice_size)
    dice_sum += roll
    if roll == 1:
      print(f'You rolled a fucking {roll} how sad')
    elif roll == dice_size:
      print(f"You rolled a {roll}! The highest number available")
    else:
      print(f'You rolled a {roll}')
  print(f"Your total is {dice_sum}")

if __name__== "__main__":
 main()