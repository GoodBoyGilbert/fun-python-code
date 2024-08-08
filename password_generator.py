import random
import string

N = 18

def generate_pass():
  res = ''.join(random.choices(string.ascii_lowercase + string.digits, k=N))
  print("Your long password : " + str(res))

generate_pass()