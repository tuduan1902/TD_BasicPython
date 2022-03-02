def emailProcess(email):
    email_usename = email[0:email.index("@")]
    email_domain = email[email.index("@")+1:]
    return [email_usename, email_domain]
def printMsg(email_usename, email_domain):
    print(f"Username is {email_usename}; Email Domain is {email_domain}")

def main():
    email = input("Please enter your email address: ").strip()
    email_usename, email_domain = emailProcess(email)
    printMsg(email_usename, email_domain)   


if __name__ == "__main__":
    main()

