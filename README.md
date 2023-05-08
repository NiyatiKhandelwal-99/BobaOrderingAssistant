[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=9262959&assignment_repo_type=AssignmentRepo)
# Boba 🧋🫧🥛🍵🍡

You are the owner of the best bubble tea shop in South Lake Union and you want to make it easy for your customers to order by speaking in natural language. Before working up to voice-to-text you decide to start with just text for your boba ordering system.

The system you develop will accept a typed customer order, engage in a dialog with the customer to clarify details, and then print out the complete order. For simplicity we will ignore details about cost and it does not need to actually make the beverage ... yet.

## Background

The goal of this assignment is to create a dialog system that does something useful. And importantly, during this process, to get an idea of the issues involved in understanding natural language. Chatbots are becoming common in such situations. For example:

* [https://www.linkedin.com/pulse/5-ways-grow-revenue-using-chatbots-sales-tool-alexandre-debecker/](https://www.linkedin.com/pulse/5-ways-grow-revenue-using-chatbots-sales-tool-alexandre-debecker/)
* [https://www.salesforce.com/eu/blog/2019/04/what-is-a-chatbot.html](https://www.salesforce.com/eu/blog/2019/04/what-is-a-chatbot.html)

However, our emphasis is not on the highly polished natural language interface you may see with a chatbot. Instead, our goal is to have you concentrate on the logic behind such systems, finding out what information is available in the customer's order and what is not, and ensuring you get all the required information from the customer by asking specific questions. Of course, in theory, you could create a fine chatbot using the information you put together in this assignment.

You may program in either Python or SWI-Prolog.

## Instructions

1. Decide on the menu: the drinks, toppings, and options you offer. Customers can only order the specials you offer. They cannot create a completely new boba tea from scratch. However, they can modify any of the bubble teas by choosing a (different) type of tea or milk. They may also customize with topics or exceptions (examples below) to their boba order.

    * Your menu must include at least 4 types of drink speicals, one of which has your name in it, such as "Grace's Taro Special".
    * You should decide what ingredients usually go into each drink, but you can leave the temperature or sugar level unspecified in some types of drinks. Use this information to make up a description for each drink you offer. For example, you may describe "Grace's Taro Special", as a "Drink with jasmine tea and taro milk topped with pudding, lychee jelly, boba, and foam with normal sweetness."
    * The menu must offer at least 3 options each for tea-base and milk-base with at least 3 additional toppings, and at least 3 exceptions you can leave out.

2. For inspiration, see something like the [Gong cha](https://gongchausa.com/) or [TSAoCAA](https://www.tsaocaatea.com/). Their websites will give you some ideas. Get creative, but don't make things too complicated! Decide on what you offer, including:

    * The kinds of drinks you offer (e.g., Brown Sugar Milk Tea, Honey Lemon Yogurt Green Tea, etc.)
    * The usual ingredients of each drink (e.g., tea, milk, and boba for a Milk Tea)
    * The kinds of base drink options available (e.g., matcha, chai, coffee, etc.)
    * The milk options available (e.g., soy, coconut, latose-free, etc.)
    * Additional options that are possible (e.g., hot or cold, "extra boba", "basil seeds", etc.), and
    * What exceptions are possible ("no foam", "hold the ice", etc.)

    Complete the "My Drinks" section below.

3. Decide on the logic of the system. In this step, you interact with the customer to get complete details of the drink they want. From each initial customer request, you have to figure out what's specified. If some details are not specified by the customer (e.g., they did not specify the drink base they want), you should tell the customer what detais you're looking for, what the options are, and what the default is. You should then ask the customer to specify the details you require. To get these details right, imagine you are using the customer input to fill out a form (or data structure) with something like the following details:

    * Name of Drink:
    * Usual ingredients:
    * Tea-type:
    * Milk-type:
    * Options:
    * Exceptions:

    Of these, the name, tea, and milk are required to be confirmed by the customer.

    Customers may specify additional options or exceptions as optional information; often they may specify neither. The usual ingredients are known to the program from the name of the drink.

4. Your program should:

    * Greet the customer and ask them what they want to have.
    * If the customer asks for the menu with a request like "What are the choices?" , "What's on the menu?" etc., display a menu with the drink choices and a description of each. Ask them what they would like to have.
    * The customer should come up with an (initial) request that looks something similar to one of these (these are only some examples; you can think of so many variations of these):
        * Grace's Taro Special please with no jelly.
        * I want the Brown-Sugar Milk Tea, skim milk, with cheese foam.
        * I'd like the Boba Lover's with green tea please, oreo, hold the sugar.
    * Remember that customers can only order the drinks you offer, but they have a choice of bases, milks, toppings, & exceptions, and they can ask for any of these choices with any drink they order. For example, if a customer just asks for "Grace's Taro with chai please, another boba, and without sweetness", you  can imagine the form or data structure you saw above filled-in with the following details:
        * Name of drink: Grace's Taro Special
        * Usual ingredients: jasmine tea, taro milk, pudding, lychee jelly, boba, foam, and normal sweetness
        * Tea: Chai
        * Milk: Taro
        * Options: boba
        * Exceptions: normal sweetness

        In this case, the customer has completely specified what they want. No other details are required.
    * If some details are not specified in the customer's initial request, you must get them to clarify their choice for each detail that is required. For example, if the customer does not specify any particular milk for a drink, you may say "This drink usually comes with coconut milk. Is that alright or would you like: almond milk, oat milk ..."
    * Take the customer's input and fill in the details provided. Decide also how you will respond if the customer specifies irrelevant options, for example, asking for "No pudding please" even when the drink they order does not have pudding.
5. Complete the My Text Processing section.
6. Demo your program with a TA. Visit office hours or make an appointment.

Programming notes:

* Some terms are equivalent ("bubble" and "boba", "matcha" and "green tea", ...) and you must treat each element in a of these terms the same as the other elements in the set.
* Ignore un-needed words like "please", "thank you", "I'd like a", etc. for simplicity.
* Phrases like "Hold the sugar" and "I don't want the dragonfruit" mean to put sweetness and dragonfruit in the exceptions liks.
* Confirm the drink order once complete.
* Allow the user to see the drinks and descriptions at any time.
* Clarify any missing item.
* Name the main program `boba.py` or `boba.pl` as appropriate. Create addtional files as needed.
* Do *NOT* request numbers from the user (enter 1. for green tea, 2 for sakura tea, etc.) the point is to be as natural language possible.
* Do *NOT* use any chatbot package or a bot framework. You may use any regex package to identify relevant words in the customer's input.
* Do *NOT* create a fancy UI. Simple text input / output only.
* Do *NOT* use any natural language library such as nltk nor spaCy.

## My Drinks

[Drink Bases] : Honey Bush Green Tea, Jasmine White Tea, Irish Breakfast Black Tea, Darjeeling Oolong Tea

[Milk Options] : Coconut Milk, Hazlenut Milk, Peanut Milk, Rice Milk

[Additional Options] : Grass Jelly, Lychee, Chia Seeds, Pudding, Boba, Coffee

[Possible Exceptions] : hold the lychee, no pudding, avoid coffee

[At Least 4 Named Drinks with descriptions] :

1. Sunny Sparkling Irish Breakfast: A drink with Irish Breakfast Black Tea and Hazlenut Milk topped with pudding and lychee

2. Sweet Sixteen Jasmine White Tea: A drink with Jasmine White Tea and Rice Milk topped with boba and chia seeds

3. Nutritionist Green Honey Drive: Drink with Honey Bush Green Tea and Peanut Milk topped with chia seeds and lychee

4. Niyati's Darjeeling Spirit Special: Drink with Darjeeling Oolong Tea and Coconut Milk topped with grass jelly and chia seads

## My Text Processing

[The list of terms you treat as equivalent] : [["coffee", "brew"], ["lychee", "litchi"], [
    "boba", "bubble"], ["green tea", "matcha"]]

[The list of terms like "Please" etc. that you will ignore.] : ["please", "putting", "request", "the", "kindly"]

[The different ways you will allow customers to specify exceptions like "Hold the rose"] : to specify an exception we can make use of the following words - ["hold", "no", "avoid", "without"]. For eg, we can say- "hold the rose", "no rose", "avoid the rose", "without rose".

## Screenshots or Notebook

Include 3 screenshot examples or a jupyter notebook where the boba ordering system takes customer input and creates something for the customer based on incomplete specifications for the boba. At least 2 of  these examples should be incomplete specifications requiring the system to check with the customer to get additional details. Add a 4th example where the boba ordering system takes customer input, and fails to create an order for the customer, because the logic of the system does not support something the customer is requesting.

Example 1:

![image](https://user-images.githubusercontent.com/66090754/201216218-96d98672-5ebf-4f67-bcb0-8fabc80b36d5.png)

![image](https://user-images.githubusercontent.com/66090754/201216237-52b29af7-ed8a-4f4f-9aad-f2d004f3c33f.png)


Example 2:

![image](https://user-images.githubusercontent.com/66090754/201216270-4909d733-594d-4a20-b118-967988b8e796.png)

![image](https://user-images.githubusercontent.com/66090754/201216300-7e5b39f6-c9f5-4adb-ae2e-9146187093bc.png)


Example 3:

![image](https://user-images.githubusercontent.com/66090754/201216333-73c1c86d-37f0-4c91-9acf-ffa3c8ef6163.png)

![image](https://user-images.githubusercontent.com/66090754/201216349-1ee2ebe1-8f07-4042-bf7d-a463c16c526f.png)


Example 4:

![image](https://user-images.githubusercontent.com/66090754/201216396-3a676f5d-dcdc-4736-80d0-d83a954813ae.png)


## Reflection

1. Explain in two scentences what you felt was the easiest part of the assignment and why.

I felt that the easiest part of the assignment was cleaning and removing the extra words from the given input sentence by the user and formatting the sentence. This is because this step required a simple sequence of string manipulation operations in python. It did not have complex logic in it and the result we get after cleaning the input made it much simpler to proceed with the rest of the entire order generation logic. 

2. Explain in two scentences what you felt was the hardest part of the assignment and why.

The hardest part according to me was to build the dialogue system in such a way that it would understand the user's language in a natural format rather than getting and understanding user input in a discrete format. This was difficult because we needed to develop a mechanism where the dialogue system would understand what the user is asking purely on the basis of the logic we put in the code. Especially, the extraction and matching part within this was something that required quite a bit of logic to make sure that the constraints are well taken care of. In the case of toppings, it was a little difficult to segregate the additional toppings and toppings that the user wanted to exclude because both of them came under the same umbrella of toppings.

3. Explain how your last example causes your ordering system to fail.

My last example causes my ordering system to fail because the input choice given by the customer does not match with any of the 4 special drinks nor does it match with the use case where the customer is asking to see the menu. As a result of this, none of the conditions in the logic of the code will pass through and the system will fail stating that the order could not be processed.
The customer 'Siri' when asked to input a choice from the 4 drinks, gave the input of 'halloween magenta' which was clearly not a part of the menu's special drinks. Hence, here, the ordering system failed with message- 'Failed to create order since drink not correctly selected!' 

4. Would it be possible to create a chatbot that pretends to be the customer? Explain why or why not.

It would be possible to create a chatbox that pretends to be a customer. This is because just how we could mimic the ordering system representative by building a system that knows the kind of questions the customer can ask, we can mimic a customer as well. It will not be impossible to create a dialogue system for a customer as the customer chat box can access the menu, scan through its items. Using a predefined format of placing an order, it can select the items from the menu and place a request command. Like humans, we can also design the customer chat box to speak some arbitrary things while placing the order.

5. How easy / difficult would it be to add another drink as well additional teas/milks/toppings to your program?

It would be very easy to add another drink in my program as well as additional teas/milks/toppings. 
The teas, milks and toppings are maintained as separate lists at a single place in the program and hence in the future whenever something needs to be added to them, that item can simply be added to the lists present in the program. 
Similarly, adding a drink is not at all difficult because I have maintainined modularity in my code by separating out tasks (with the help of functions) and the code strongly makes use of re-usability. The entire common functionality for processing each drink is extracted out and kept in a common functon.  Hence, in the future if we need to add a drink, we can simply process this drink with the help of the common function. You can see this in the program. For processing any of the drinks, we are calling the 'common_drink_make' function and we simply pass the original dictionary ingredient of the drink. The rest entire ordering process will be taken care of the 'common_drink_make' function. 
