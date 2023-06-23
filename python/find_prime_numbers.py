def get_number_from_user(msg):
    while True:
      num = input(msg).strip()
      if not num.isnumeric():
         print("Oops! This is an invalid response. Try again and insert a number:  ")
         