"""example we want to print square numbers from 1 to 10"""
for  i in range(0,11):
    print (i**2)
    #printing traingle
    for x in range (0,10,2):
        s = 'j'*x
        print (s.center(10))
        
        #comprehension"
        """
        -expression
        -iteration
        -condition
        """
        
    square_numbers = [i**2 for i in range (0,11)]
    print(square_numbers)
    names = ["roger","tonny","edgar","edrine,"peter","jane"]
    listt_of-names_with_letter_o = [name for name in names if "o" in name]
    print (list_of_names_with_letter_o)