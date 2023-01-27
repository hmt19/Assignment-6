
def is_pangram(string): 
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  for char in alphabet: 
    if char not in string.lower(): 
      return False
  
  return True
  
print(is_pangram("The quick brown fox jumps over the lazy dog")) 
# Output: True
