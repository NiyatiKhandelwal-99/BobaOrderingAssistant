import random

user_name = ""
# menu item lists
tea_base = ['honey bush green tea', 'jasmine white tea',
            'irish breakfast black tea', 'darjeeling oolong tea']
milk_base = ['coconut milk', 'hazlenut milk', 'peanut milk', 'rice milk']
toppings = ["grass jelly", "lychee", "chia seeds", "pudding", "boba", "coffee"]
exceptions = ["hold the lychee", "no pudding", "avoid coffee"]

# list for exceptions
exception_words = ["hold", "no", "avoid", "without"]
exception_ingredients = ["lychee", "pudding", "coffee"]

# list of un-needed words
cut_down_words = ["the", "please", "putting", "request", "kindly"]

# list of equivalent terms
equivalent_words = [["coffee", "brew"], ["lychee", "litchi"], [
    "boba", "bubble"], ["green tea", "matcha"]]


# parsing the message to find equivalent terms and remove un-needed words from message
def parse_message(msg):
  msg = msg.lower()
  msg = msg.replace(".", "")
  for x in equivalent_words:
    if x[1] in msg:
      msg = msg.replace(x[1], x[0])
  for x in msg.split():
    if x in cut_down_words:
      msg = msg.replace(x, "")
  return msg

# removing exception items from the toppings list


def consider_exceptions(msg, listoftoppings):

  removed_ele = []
  unchecked_toppings = []
  flag = "false"
  for x in msg.split():
    if flag == "true":
      unwanted_ele = x
      if (unwanted_ele in listoftoppings and unwanted_ele in exception_ingredients):
        removed_ele.append(unwanted_ele)
      elif (unwanted_ele not in listoftoppings):
        print(unwanted_ele+" is not a part of this drink anyway!")
        unchecked_toppings.append(unwanted_ele)
      else:
        print("Sorry, "+unwanted_ele+" cannot be removed.")
      flag = "false"

    if x in exception_words:
      flag = "true"

  return [removed_ele, unchecked_toppings]


drinks_special = {"Sunny Sparkling Irish Breakfast": "A drink with Irish Breakfast Black Tea and Hazlenut Milk topped with pudding and lychee",
                  "Sweet Sixteen Jasmine White Tea": "A drink with Jasmine White Tea and Rice Milk topped with boba and chia seeds",
                  "Nutritionist Green Honey Drive": "Drink with Honey Bush Green Tea and Peanut Milk topped with chia seeds and lychee",
                  "Niyati's Darjeeling Spirit Special": "Drink with Darjeeling Oolong Tea and Coconut Milk topped with grass jelly and chia seads"}


sunny_sparkling_dict = {"name of the drink": "Sunny Sparkling Irish Breakfast",
                        "usual ingredients": "irish black tea, hazlenut milk, pudding, lychee",
                        "tea-type": "irish breakfast black tea",
                        "milk-type": "hazlenut milk",
                        "toppings": ["pudding", "lychee"]
                        }

sweet_sixteen_dict = {"name of the drink": "Sweet Sixteen Jasmine White Tea",
                      "usual ingredients": "jasmine white tea, rice milk, boba, chia seeds",
                      "tea-type": "jasmine white tea",
                      "milk-type": "rice milk",
                      "toppings": ["boba", "chia seeds"]
                      }

nutritionist_green_dict = {"name of the drink": "Nutritionist Green Honey Drive",
                           "usual ingredients": "honey bush green tea, peanut milk, lychee, chia seeds",
                           "tea-type": "honey bush green tea",
                           "milk-type": "peanut milk",
                           "toppings": ["lychee", "chia seeds"]
                           }

niyati_darjeeling_dict = {"name of the drink": "Niyati\'s Darjeeling Spirit Special",
                          "usual ingredients": "darjeeling oolong tea, coconut milk, grass jelly, chia seeds",
                          "tea-type": "darjeeling oolang tea",
                          "milk-type": "coconut milk",
                          "toppings": ["grass jelly", "chia seeds"]
                          }


def format_name(x):
  return x.title


def display_order(order):
  print("-------------------------------------------------------------------")
  print("Please confirm your order: ")
  print("\nDrink: "+order["name of the drink"])
  print("Usual Ingredients: "+order["usual ingredients"])
  print("Tea Type: "+order["tea-type"])
  print("Milk Type: "+order["milk-type"])

  my_toppings = order["toppings"]
  my_toppings_print = "Toppings: " + \
      ', '.join(str(item) for item in my_toppings)
  print(my_toppings_print)

  exceptions = order["exceptions"]
  exceptions_print = "Exceptions: " + \
      ', '.join(str(item) for item in exceptions)
  print(exceptions_print)

  print("\n-------------------------------------------------------------------")
  print("Should we confirm this order or do we cancel this one and begin a new one?")


def display_menu():
    print("""
---------------------------------Niya's Boba-mazing Drink's Special MENU--------------------------------
    
    We have 4 special drinks on the menu today : 
    
    1. Sunny Sparkling Irish Breakfast
       """+drinks_special['Sunny Sparkling Irish Breakfast']+"""
    2. Sweet Sixteen Jasmine White Tea
       """+drinks_special['Sweet Sixteen Jasmine White Tea']+"""
    3. Nutritionist Green Honey Drive
       """+drinks_special['Nutritionist Green Honey Drive']+"""
    4. Niyati's Darjeeling Spirit Special
       """+drinks_special['Niyati\'s Darjeeling Spirit Special']+"""
    
    Choices of Drinks:
    """+tea_base[0] + ", " + tea_base[1] + ", " + tea_base[2] + ", " + tea_base[3]+"""
    
    Choices of Milk Base:
    """+milk_base[0] + ", " + milk_base[1] + ", " + milk_base[2] + ", " + milk_base[3]+"""

    Toppings available:
    """+toppings[0] + ", " + toppings[1] + ", " + toppings[2] + ", " + toppings[3]+", " + toppings[4]+", " + toppings[5]+"""

    Exceptions:
    """+exceptions[0] + ", " + exceptions[1] + ", " + exceptions[2]+"""
    -----------------------------------------------------------------------------------------------------""")


responses = {
    "show me the menu": display_menu,
    "": "Hey, are you there?",
    "default": "this is the default message"
}


def display_menu_at_any_level(userchoice):
  if "menu" in userchoice or "choices" in userchoice or "options" in userchoice:
    display_menu()
    return "true"
  return "false"


def print_response(msg):
  if (msg == "show me the menu"):
    display_menu()
    print("What would you like to have?")
    user_input = input()
    print(related(user_input))
  elif(msg == "Invalid choice. Please select a tea from the menu!"):
    print("Failed to create order since drink not correctly selected!")


def related(x_text):
  y_text = ""
  if "menu" in x_text or "choices" in x_text or "options" in x_text:
    y_text = "show me the menu"
  elif "sunny" in x_text or "sparkling" in x_text or "irish" in x_text or "breakfast" in x_text:
    sunny_sparkling_irish_breakfast_check(x_text)
  elif "sweet" in x_text or "sixteen" in x_text or "jasmine" in x_text or "white" in x_text:
    sweet_sixteen_jasmine_check(x_text)
  elif "nutritionist" in x_text or "green" in x_text or "honey" in x_text or "drive" in x_text:
    nutritionist_green_honey_check(x_text)
  elif "niyati" in x_text or "darjeeling" in x_text or "spirit" in x_text or "special" in x_text:
    niyati_darjeeling_spirit_check(x_text)
  else:
    y_text = "Failed to create order since drink not correctly selected!"
  return y_text


def check_tea_type(msg):

  if ("green" in msg):
    return "honey bush green tea"
  elif ("white" in msg):
    return "jasmine white tea"
  elif ("black" in msg):
    return "irish breakfast black tea"
  elif ("oolong" in msg):
    return "darjeeling oolong tea"
  else:
    return "no tea type mentioned"


def check_milk_type(msg):

  if ("coconut" in msg):
    return "coconut milk"
  elif ("hazlenut" in msg):
    return "hazlenut milk"
  elif ("peanut" in msg):
    return "peanut milk"
  elif ("rice" in msg):
    return "rice milk"
  else:
    return "no milk type mentioned"

# extracting all toppings mentioned in the order


def check_toppings(msg):

  toppings_list = []

  for x in toppings:
    if x in msg:
      toppings_list.append(x)

  return toppings_list


order = {"name of the drink": "",
         "usual ingredients": "",
         "tea-type": "",
         "milk-type": "",
         "toppings": [],
         "exceptions": []
         }


def common_drink_make(msg, drink_dict):
  msg = parse_message(msg)

  order["name of the drink"] = drink_dict["name of the drink"]
  order["usual ingredients"] = drink_dict["usual ingredients"]

  #setting tea type
  tea_type = drink_dict["tea-type"]
  if ("tea" in msg):
    tea_type = check_tea_type(msg)
  else:
    print("The drink is best served with " +
          drink_dict["tea-type"]+". Do you want continue with this or you can select any tea type from the below tea bases: ")
    print(', '.join(tea_base))
    input_ans = input()
    menu_needed = display_menu_at_any_level(input_ans)
    if (menu_needed == "true"):
      print("The drink is best served with " +
            drink_dict["tea-type"]+". Do you want continue with this or you can select any tea type from the below tea bases: ")
      print(', '.join(tea_base))
      input_ans = input()
    if ("default" in input_ans or "this" in input_ans or "yes" in input_ans or "continue" in input_ans):
      tea_type = drink_dict["tea-type"]
    else:
      tea_type = check_tea_type(input_ans)

  if (tea_type == "no tea type mentioned"):
    tea_type = drink_dict["tea-type"]
  order["tea-type"] = tea_type

  #setting milk type
  milk_type = drink_dict["milk-type"]
  if ("milk" in msg):
    milk_type = check_milk_type(msg)
  else:
    print("This drink is usually served with " +
          drink_dict["milk-type"]+". Do you want to continue with it or you can select any milk type from the below milk bases: ")
    print(', '.join(milk_base))
    input_ans = input()
    menu_needed = display_menu_at_any_level(input_ans)
    if (menu_needed == "true"):
      print("This drink is usually served with " +
            drink_dict["milk-type"]+". Do you want to continue with it or you can select any milk type from the below milk bases: ")
      print(', '.join(milk_base))
      input_ans = input()
    if ("default" in input_ans or "this" in input_ans or "yes" in input_ans or "continue" in input_ans):
      milk_type = drink_dict["milk-type"]
    else:
      milk_type = check_milk_type(input_ans)
  if (milk_type == "no_milk_type_mentioned"):
    milk_type = drink_dict["milk-type"]
  order["milk-type"] = milk_type

  #setting toppings
  drink_toppings = drink_dict["toppings"]
  additional_toppings = check_toppings(msg)
  topping_result = consider_exceptions(msg, drink_toppings)
  removed_toppings = topping_result[0]
  unchecked_toppings = topping_result[1]

  # removing exceptions from additional toppings
  for x in additional_toppings:
    if x in removed_toppings:
      additional_toppings.remove(x)

  # setting the exceptions to removed toppings
  order["exceptions"] = removed_toppings

  # removing exception toppings from original toppings list
  for x in removed_toppings:
    if x in drink_toppings:
      drink_toppings.remove(x)

  # preparing the final toppings list taking into account the original additional toppings
  final_toppings_list = []
  for x in drink_toppings:
    final_toppings_list.append(x)
  for y in additional_toppings:
    final_toppings_list.append(y)
  final_list = [*set(final_toppings_list)]
  order["toppings"] = final_list

  for x in final_toppings_list:
    if x in unchecked_toppings:
      final_toppings_list.remove(x)

  display_order(order)
  user_ch = input()
  if ("begin" in user_ch or "new" in user_ch or "start" in user_ch or "cancel" in user_ch):
    start_order()
  else:
    print("Thank you! Your order is confirmed.")


def niyati_darjeeling_spirit_check(msg):
  common_drink_make(msg, niyati_darjeeling_dict)

def nutritionist_green_honey_check(msg):
  common_drink_make(msg, nutritionist_green_dict)

def sweet_sixteen_jasmine_check(msg):
  common_drink_make(msg, sweet_sixteen_dict)

def sunny_sparkling_irish_breakfast_check(msg):
  common_drink_make(msg, sunny_sparkling_dict)


def send_message(message):
  print_response(message)


def respond(message):
    if message in responses:
        bot_message = random.choice(responses[message])
    else:
        bot_message = random.choice(responses["default"])
    return bot_message


def start_order():
  print("Hi " + user_name +
        ", hope you are having a good day! What would you like to have?")
  user_input = input()
  user_input = user_input.lower()
  related_text = related(user_input)
  send_message(related_text)


def main():
  print("Hello! What do you want me to call you?")
  global user_name
  user_name = input()

  start_order()


main()