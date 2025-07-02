from _datetime import datetime


class Mail():
    def __init__(self, sender_adresse, subject, message, date_time, read_status):
        self.senderAdresse = sender_adresse
        self.subject = subject
        self.message = message
        self.datetime = date_time if date_time else datetime.now()
        self.read_status = read_status

    def mark_read(self):
        self.read_status = True

    def __str__(self):
        return print("Subject", self.subject, "from", self.senderAdresse, "on", self.datetime, ":", self.message,
                     "opened", self.read_status)


class inbox():
    def __init__(self):
        self.inbox = []

    def add(self, mail):
        self.inbox.append(mail)

    def print_mail_headers(self):
        for mail in self.inbox:
            print("Subject", mail.subject, "from", mail.senderAdresse, "on", mail.datetime)

    def open(self, index):
        if index < 0 or index > len(self.inbox):
            print("Index out of range")
            return
        mail = self.inbox[index]
        mail.mark_read()
        print("From", mail.senderAdresse, "on", mail.datetime, ":", mail.message)

    def count_unread(self):
        unread = 0
        for mail in self.inbox:
            if not mail.read_status:
                unread += 1
        return unread



class Main():
    meine_mail = Mail(

    sender_adresse="max@example.com",
    subject="Hallo!",
    message="Das ist eine Testnachricht.", read_status= False, date_time=datetime.now())


    inbox = inbox()
    inbox.add(Mail("Tom@ichkannnichtmehr.end", "Bug fix", "Its full of bugd.", datetime.now(), False))
    inbox.add(Mail("alice@example.com", "Meeting", "The meeting is at 10am.", datetime.now(), False))
    inbox.add(Mail("bob@example.com", "Party", "Don't forget the party on Saturday!", datetime.now(), False))
    inbox.add(Mail("carol@example.com", "Invoice", "Your invoice is attached.", datetime.now(), False))
    inbox.add(meine_mail)


    print("Unread: ", inbox.count_unread())
    meine_mail.mark_read()
    print("Unread: ", inbox.count_unread())

    (inbox.print_mail_headers())
    inbox.open(1)
    inbox.open(3)
