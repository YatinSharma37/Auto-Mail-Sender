
import smtplib
my_email =input("Enter Sender mail here:")
to_email=input("Enter reciver mail here:")
password=input("Enter Sender mail generated pass:")
subject=input("Enter mail subject:")
body=input("Enter mail body:")
msg = f"Subject: {subject}\n\n{body}"

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
      
        connection.starttls()
       
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=msg)
    print("Email sent successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
