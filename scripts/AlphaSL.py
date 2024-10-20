def AlphaSL():
  key_word = input("key word?")
  site_name = input("site name?")

  while len(key_word) <= 10:
    key_word += key_word

  while len(site_name) <= 4 * (len(key_word)):
    site_name += site_name

  x = 2 if "o" in site_name else 1

  cut_site_name = ""

  while x < len(site_name):
    cut_site_name += site_name[x]
    x += 2

  password = ""
  for i in range(0, (len(key_word))):
    password += cut_site_name[i]
    password += key_word[i]

  print(password)
