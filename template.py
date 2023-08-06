letter='''Dear<|Name|>,
you are selected.
Date:<|Date|>
'''
name=input("Enter a name\n")
date=input("Enter a date\n")
letter=letter.replace("<|Name|>",name)
letter=letter.replace("<|Date|>",date)
print(letter)