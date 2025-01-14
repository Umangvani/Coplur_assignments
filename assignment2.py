from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, recipient, message):
        pass

class EmailNotification(Notification):
    def send(self, recipient, message):
        print(f"Sending Email to {recipient}: {message}")

class SMSNotification(Notification):
    def send(self, recipient, message):
        print(f"Sending SMS to {recipient}: {message}")

class PushNotification(Notification):
    def send(self, recipient, message):
        print(f"Sending Push Notification to {recipient}: {message}")


def write_Notification(channel,recipient, message):
    if(channel == "email"):
        em = EmailNotification()
        return em.send(recipient, message)
    
    if(channel == "sms"):
        sm = SMSNotification()
        return sm.send(recipient, message)
    
    if(channel == "push"):    
        pm = PushNotification()
        return pm.send(recipient, message)
    
    if not channel:
        print("Invalid notification channel.")
    

    
if __name__ == "__main__":
    print("\nNew Policy Announcement:")
    write_Notification("email", "umangvani777@gmail.com" ,"A new policy has been implemented." )
    
    
    print("\nEvent Reminder:")
    write_Notification("sms", 9154306476 , "Makar Sankranti Event by 5pm")
    
    print("\nSystem Alert:")
    write_Notification("push", "samyak", "Drop server till 6pm")
