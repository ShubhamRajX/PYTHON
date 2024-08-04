# Write a program to fill in a letter template given below with name and date. 
# letter = '''  
#         Dear <|Name|>, 
#         You are selected! 
#         <|Date|> 
#         ''' 

letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''

print(letter.replace("<|Name|>", "Raj").replace("<|Date|", "4 August 2024"))