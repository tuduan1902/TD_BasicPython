from moriaty import emailProcess, printMsg

def main():
    emails =['moriaty@gmail.com', 'github@gmail.com', 'tuduan1902@github.dev']
    for email in emails:
        email_username, email_domain = emailProcess(email)
        printMsg(email_username, email_domain)

if __name__ == '__main__':
    main()