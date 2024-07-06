'''This module file is created to practice Python String Slicing
    and Created by Chandan on 28/06/2024'''

email = 'ichandanvp@gmail.com'

username = email.split("@")[0]
print("username is:",username)

domain = email.split("@")[1]
mail_domain = domain.split(".")[0]
print(mail_domain)
