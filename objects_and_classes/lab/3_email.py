class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []

while True:
    command = input()
    if command == "Stop":
        break
    emails.append(command)

sent_mails = list(map(int, input().split(", ")))

for mail in range(len(emails)):
    current_command = emails[mail].split(" ")
    current_mail = Email(current_command[0], current_command[1], current_command[2])

    if mail in sent_mails:
        current_mail.send()

    print(current_mail.get_info())
