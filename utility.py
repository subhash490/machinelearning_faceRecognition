#function for sending whatsapp message  
    
def whatsapp():
    import pywhatkit as kitkat
    kitkat.sendwhatmsg_instantly('mobileNo',' face detected  this message is computer generated !!!')
    print("WHATSAPP MESSAGE SENT!!!")
    
  #function for sending Email message  
    
 def email_message():
    
    
    
    import smtplib

    sender_email = "subhashyadav945@gmail.com"
    rec_email = "subhashyadav2816@gmail.com"
    password = pas
    message = "face dedected at"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    print("Login success")
    server.sendmail(sender_email, rec_email, message)
    print("Email has been sent to ", rec_email)
    
    
     #function for aws configuration
     
     
     def aws():
    print("in")
    #LANUNCHING AN INSTANCE
    os.popen("aws ec2 run-instances --image-id ami-0ad704c126371a549 --count 1 --instance-type t2.micro ")
    print("AWS instance launched!!!\n")
    time.sleep(15)
    
    #CREATING A 5GB VEBS VOLUME
    os.popen("aws ec2 create-volume --availability-zone ap-south-1a --volume-type gp2 --size 2 --tag-specifications ResourceType=volume,Tags=[{Key=Name,Value=SI_task}]!!!\n")
    time.sleep(15)
    
    print("TASK 6 DONE!!!")
    
