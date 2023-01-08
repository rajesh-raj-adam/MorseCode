# Morse code dictionary
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 

def encrypt(message):
  cipher = ''
  for letter in message:
    if letter != ' ':
      # Append the morse code of the letter to the cipher
      cipher += MORSE_CODE_DICT[letter] + ' '
    else:
      # Append a space to the cipher
      cipher += ' '

  return cipher

def decrypt(message):
  message += ' '
  decipher = ''
  citext = ''
  lookup = {v: k for k, v in MORSE_CODE_DICT.items()}
  for letter in message:
    # If the letter is a space
    if letter != ' ':
      # A counter to keep track of space
      i = 0
      # Store the character
      citext += letter
    else:
      # Increase the counter
      i += 1
      # If the counter is even, it means two spaces have been encountered
      if i == 2 :
        # Add a space to the decipher
        decipher += ' '
      else:
        # Look for the morse code in the lookup table
        decipher += lookup[citext]
        citext = ''

  return decipher

def main():
  message = input("Enter a message: ")
  result = encrypt(message.upper())
  print(result)
  result = decrypt(result)
  print(result)

if __name__ == '__main__':
  main()
