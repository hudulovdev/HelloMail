import smtplib

def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)  # Change the server and port based on your email provider
        server.starttls()
        server.login(sender_email, sender_password)

        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(sender_email, recipient_email, message)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("An error occurred while sending the email:", str(e))


def main():
    sender_email = input("Enter your email address: ")
    sender_password = input("Enter your email password: ")
    recipient_email = input("Enter the recipient's email address: ")
    recipient_name = input("Enter the recipient's name: ")

    subject = f"Hello {recipient_name}!"
    body = f"Hello {recipient_name},\n\nThis is a test email sent from Python."

    send_email(sender_email, sender_password, recipient_email, subject, body)


if __name__ == "__main__":
    main()
