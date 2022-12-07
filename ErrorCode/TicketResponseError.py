class Main(object):
    L = []
    selection = ""

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
        elif Main.selection == "3":
            #You pass L as argument in the ticketResponse method. 
            Ticket().ticketResponse()
            Main.__init__()
        elif Main.selection == "4":
            Ticket.ticketStats()

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


    def menu():
        Main.selection = input("Select from the following choices:\n"
                               "0: Exit\n"
                               "1: Submit helpdesk ticket\n"
                               "2: Show all tickets\n"
                               "3: Re-open/Respond to ticket by number\n"
                               "4: Display ticket stats\n"
                               "_________________________________________\n"
                               "Enter menu selection 0 - 5: ")
        return Main.selection


class Ticket(object):
    ticket_number = 2000
    tickets_created = 0
    tickets_resolved = 0
    tickets_open = 0

    def __init__(self):
        self.name = ""
        self.id = ""
        self.email = ""
        self.issue = ""
        self.response = ""
        self.status = ""
        Ticket.ticket_number += 1
        self.ticket_number = Ticket.ticket_number
        Ticket.tickets_created += 1

    def ticketData(self):
        self.name = input("Please enter your name: ")
        self.id = input("Please enter your staff ID: ")
        self.email = input("Please enter your email: ")
        self.issue = input("Please describe your issue: ")
        if "password change" in self.issue.lower():
            self.response = Ticket.passwordGenerator(self)
            self.status = "Closed"
            Ticket.tickets_resolved += 1
        else:
            self.response = "Not Yet Provided"
            self.status = "Open"
            Ticket.tickets_open += 1

    def ticketDisplay(self):
        print("Ticket Number: ", self.ticket_number)
        print("Ticket Creator: ", self.name)
        print("Staff ID: ", self.id)
        print("Email Address: ", self.email)
        print("Description of Issue: ", self.issue)
        print("Response: ", self.response)
        print("Ticket Status: ", self.status)

    def passwordGenerator(self):
        string1 = (self.id[0] + self.id[1])
        string2 = (self.name[0] + self.name[1] + self.name[2])
        new_password = ("New password generated: " + "".join([string1, string2]))
        return new_password

    def ticketStats():
        print("Tickets Created: ", Ticket.tickets_created)
        print("Tickets Resolved: ", Ticket.tickets_resolved)
        print("Tickets to Solve: ", Ticket.tickets_open)

    def ticketResponse(self):
        #first ask user to tell ticket number he want to update response of then
        ticket_update = input("Please enter ticket number: ")
        #here in ticket response apply a loop on the L that you will get as parameter. and find ticket with the specified
        for i in range(len(Main.L)):
            if ticket_update == Main.L[i].ticket_number:
                Main.L[i].response = input("Please enter response: ")
        #number and update response by asking user to enter response and update it in the ticket
        if self.status == "Open":
            self.response = input("Please enter response: ")
            Ticket.tickets_open -= 1
            Ticket.tickets_resolved += 1
            self.status = "Closed"
        elif self.status == "Reopened":
            self.response = input("Please enter response: ")
            Ticket.tickets_open -= 1
            Ticket.tickets_resolved += 1
            self.status = "Closed"
        else:
            self.response = input("Please enter response: ")
            Ticket.tickets_resolved -= 1
            Ticket.tickets_open += 1
            self.status = "Reopened"


if __name__ == '__main__':
    Main.__init__()
