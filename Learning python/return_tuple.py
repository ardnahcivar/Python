def email_split(email_id):
    email, domain = email_id.split('@')
    return (email,domain)


print(email_split('ravbhanage@gmail.com'))
    
