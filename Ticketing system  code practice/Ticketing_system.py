from Ticket import Ticket  # Importing the Ticket class from Ticket module


class Ticketing_system:

    def __init__(self):
        # Initializing instance variables
        self.tickets = []  # List to store ticket objects
        self.counter = 2000  # Counter to assign unique ticket IDs
        self.open_tickets = 0  # Counter to keep track of open tickets
        self.total_tickets = 0  # Counter to keep track of total tickets

    def Submit_ticket(self):
        # Method to submit a new ticket
        Ticket_id = self.counter
        staff_id = input("Enter Your Staff ID:")
        name = input("Enter Your name :")
        email = input("Enter Your E-mail ID:")
        issue = input("What is the issue:")

        # Creating a new Ticket object
        ticket = Ticket(Ticket_id, name, staff_id, email, issue)
        self.tickets.append(ticket)  # Adding the ticket to the list
        self.counter += 1
        self.open_tickets += 1  # Incrementing open ticket count
        self.total_tickets += 1  # Incrementing total ticket count

        print("Your ticket is submitted successfully")

    def Display_tickets(self):
        # Method to display all tickets
        for ticket in self.tickets:
            print()
            print("*****TICKET*****")
            print("Ticket ID : ", ticket.ticket_id)
            print("Name : ", ticket.name)
            print("Staff ID : ", ticket.staff_id)
            print("e-mail : ", ticket.email)
            print("Issue : ", ticket.issue)
            print("Response : ", ticket.response)
            print("Status : ", ticket.status)

    def Generate_new_Password(self, Ticket):
        # Method to generate a new password based on the issue
        if "Change password" in Ticket.issue:
            return Ticket.staff_id[:2] + Ticket.name[:3]

    def Response_ticket(self):
        # Method to respond to a ticket
        TID = int(input("Ticket id :"))
        for t in self.tickets:
            if TID == t.ticket_id:
                resp = input("Enter Response: ")
                t.response = resp
                t.status = "Closed"
                self.open_tickets -= 1  # Decrementing open ticket count
                t.response = "The issue has been resolved"
                break

    def Reopen_ticket(self):
        # Method to reopen a closed ticket
        TID = int(input('Ticket Id: '))
        for t in self.tickets:
            if TID == t.ticket_id:
                t.status = "Reopened"
                self.open_tickets += 1  # Incrementing open ticket count
                break
    # def Resolve_ticket(self):
    #     if self.status == "Open":
    #         self.status = "Closed"

    # def Reopen_ticket(self):
    #     if self.status == "Closed":
    #         self.status = "Reopened"

    # def Show_response(self, response):
    #     self.response = response

        # loop through the list of tickets
        # if ticketID == t.ticket_id
        # input respose
        # change the status

    def Status(self):
        # Method to display total and open ticket counts
        print("Total Tickets : ", self.total_tickets)
        print("Open Tickets : ", self.open_tickets)


def main_manu(self):
    # Method to display the main menu and handle user choices
    while True:
        print("")
        print("1. SUBMIT A TICKET")
        print("2. DISPLAY TICKET")
        print("3. RESPOND TO A TICKET")
        print("4. REOPEN A TICKET")
        print("5. SHOW STATUS")
        print("6. EXIT")
        print("PLEASE CHOOSE A NUMBER FROM 1 TO 6")
        print("")
        choice = input("YOUR CHOICE : ")

        if choice == "1":
            self.Submit_ticket()
        elif choice == "2":
            self.Display_tickets()
        elif choice == "3":
            self.Response_ticket()
        elif choice == "4":
            self.Reopen_ticket()
        elif choice == "5":
            self.Status()
        elif choice == "6":
            print("Exiting the Ticketing system. BYE !!")
            break
        else:
            print("Invalid input, Please choose number between 1 to 6 !!!")


ts = Ticketing_system()  # Creating an instance of Ticketing_system class
