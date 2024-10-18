def AlphaSL():
  key_word = input("key word?")
  site_name = input("site name?")
  
  while len(key_word) <= 10:
    key_word += key_word
  
  while len(site_name) <= len(key_word):
    site_name += site_name
  
  password = ""
  for i in range(0, (len(key_word))):
    password += site_name[i]
    password += key_word[i]
  
  print(password)
