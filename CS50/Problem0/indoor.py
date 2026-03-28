def lowercase(text):
  return text.lower()

def main():
  global user_input 
  user_input = str(input('say: '))
  result = lowercase(user_input)
  print(result)

main()
