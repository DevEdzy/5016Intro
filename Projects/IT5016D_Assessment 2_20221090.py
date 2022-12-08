# IT5016D_Assessment 2_20221090.py
#
# author: Michael Edwards
# date: 2/12/2022


class Main(object):
    L = []
    selection = ""

    #prompts menu and asks user to make a selection
    #invokes function depending on users input
           
    def __init__():
        Main.menu()
        if Main.selection == "1":
            a = Ticket()
            a.ticketData()
            Main.L.append(a)
            Main.prompt()
        elif Main.selection == "2":
            for i in range(len(Main.L)):
                print("----------------------------")
                Main.L[i].ticketDisplay()
            Main.__init__()
        elif Main.selection == "3":
            Ticket().ticketResponse()
            Main.__init__()
        elif Main.selection == "4":
            Ticket.ticketStats()
            Main.__init__()
        else:
            print("Please enter a valid selection")
            Main.__init__()
    
    def prompt():
        prompt = input("Do you have another problem to submit? (Y/N)")
        while prompt.lower() == "y":
            a = Ticket()
            a.ticketData()
            Main.L.append(a)
            prompt = input("Do you have another problem to submit? (Y/N)")
        else:
            print("\n")
            Main.__init__()

    #Main menu display

    def menu():
        Main.selection = input("\nSelect from the following choices:\n"
                               "0: Exit\n"
                               "1: Submit helpdesk ticket\n"
                               "2: Show all tickets\n"
                               "3: Re-open/Respond to ticket by number\n"
                               "4: Display ticket stats\n"
                               "_________________________________________\n"
                               "Enter menu selection 0 - 4: ")
        print("\n")
        return Main.selection


class Ticket(object):
    ticket_number = 2000
    tickets_created = 0
    tickets_resolved = 0
    tickets_open = 0

    #empty variables to be assigned
    
    def __init__(self):
        self.name = ""
        self.id = ""
        self.email = ""
        self.issue = ""
        self.response = ""
        self.status = ""
        self.ticket_number = Ticket.ticket_number

    #asks user for input and assigns to variables in __init__ function
    
    def ticketData(self):
        self.name = input("Please enter your name: ")
        self.id = input("Please enter your staff ID: ")
        self.email = input("Please enter your email: ")
        self.issue = input("Please describe your issue: ")
        Ticket.ticket_number += 1
        Ticket.tickets_created += 1
        if "password change" in self.issue.lower():
            self.response = Ticket.passwordGenerator(self)
            self.status = "Closed"
            Ticket.tickets_resolved += 1
        else:
            self.response = "Not Yet Provided"
            self.status = "Open"
            Ticket.tickets_open += 1

    #displays ticket information

    def ticketDisplay(self):
        print("Ticket Number: ", self.ticket_number)
        print("Ticket Creator: ", self.name)
        print("Staff ID: ", self.id)
        print("Email Address: ", self.email)
        print("Description of Issue: ", self.issue)
        print("Response: ", self.response)
        print("Ticket Status: ", self.status)

    #generates new password

    def passwordGenerator(self):
        string1 = (self.id[0] + self.id[1])
        string2 = (self.name[0] + self.name[1] + self.name[2])
        new_password = ("New password generated: " + "".join([string1, string2]))
        return new_password

    #display ticket statistics

    def ticketStats():
        print("Tickets Created: ", Ticket.tickets_created)
        print("Tickets Resolved: ", Ticket.tickets_resolved)
        print("Tickets to Solve: ", Ticket.tickets_open)

    #allows helpdesk staff to respond and re-open tickets

    def ticketResponse(self):
        ticket_update = int(input("Please enter ticket number: "))
        for i in range(len(Main.L)):
            if ticket_update == Main.L[i].ticket_number:
                Main.L[i].response = input("Please enter response: ")
                if Main.L[i].status == "Open":
                    Ticket.tickets_open -= 1
                    Ticket.tickets_resolved += 1
                    Main.L[i].status = "Closed"
                elif Main.L[i].status == "Reopened":
                    Ticket.tickets_open -= 1
                    Ticket.tickets_resolved += 1
                    Main.L[i].status = "Closed"
                else:
                    Ticket.tickets_resolved -= 1
                    Ticket.tickets_open += 1
                    Main.L[i].status = "Reopened"
                    

if __name__ == '__main__':
    Main.__init__()

    
