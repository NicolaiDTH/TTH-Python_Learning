shopping_list = []

def show_help():
 print("What else should I pick up at the store?")
 print("Enter DONE to stop.")

def add_to_list(item):
 shopping_list.append(item)
 print("Added: List has {} items.").format(len(shopping_list))

def show_list():
 print("Here's your list:")
 for item in shopping_list:
  print(item)

 show_help()

 while True:
  new_input = input("> ")
  if new_item == 'DONE'
  show_list()
  break
  add_to_list(new_item)
  continue

  show_list()