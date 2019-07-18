import random

def play_hat_game():
  hat_number = [1,2,3] 
  hat_choice = random.choice(hat_number) # hat you choose
  winner_hat = random.choice(hat_number) # hat with prize
  stay___result = (hat_choice == winner_hat)
  switch_result = not stay___result
  return random.choice([('stayed',stay___result),('switch',switch_result)])

n = 100000
stay_wins = switch_wins = 0

for i in range(0,n):

  outcome = play_hat_game()
  if outcome[0] == 'switch':
    switch_wins += outcome[1]
  else:
    stay_wins += outcome[1]

print('trials:',n)
print('Probability to win if you switch:',switch_wins/n)
print('Probability to win if you stay  :',stay_wins/n)
