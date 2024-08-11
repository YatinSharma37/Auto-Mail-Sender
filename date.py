import datetime as dt
import smtplib
my_email =input("Enter Sender mail here:")
to_email=input("Enter reciver mail here:")
password=input("Enter Sender mail generated pass:")
subject=input("Enter mail subject:")
body=input("Enter mail body:")
Hour=int(input("Enter Sending Hour here:"))
Min=int(input("Enter Sending Minute here:"))

# password="xtyv nmqp ylfc hrnf"
# my_email = "abc@gmail.com"
# to_email = "cde@gmail.com"
# subject = "hlo"     
# body = "how are you"
msg = f"Subject: {subject}\n\n{body}"
while True:
            now = dt.datetime.now()
            target_time = dt.time(Hour, Min)
            if now.time().replace(microsecond=0,second=0) == target_time:
                try:
                    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                        connection.starttls()
                            
                        connection.login(user=my_email, password=password)
                        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=msg)
                        print("Email sent successfully!")
                except Exception as e:
                            print(f"An error occurred: {e}")

                break
            else:
                continue
                print("No")
                continue
