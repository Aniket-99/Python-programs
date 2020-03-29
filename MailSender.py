import smtplib as s


# On Gmail's less secure app in order to allow this program to send email

ob = s.SMTP("smtp.gmail.com",589)

ob.starttls()
ob.login("YourEmail@gmail.com", "YourPassword")

subject = "Sending email using python"
body = "This is python here"
message = "Subject:{}\n\n{}".format(subject,body)
listOfAddresses = ["email","email"]

ob.sendmail("abc@gmail.com", listOfAddresses, message)
print("Send successfully....")
ob.quit()