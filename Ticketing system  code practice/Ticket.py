class Ticket():
    # Represents a ticket for assistance request in the ticketing system.

    # Constructor method to initialize a new Ticket object with provided attributes.
    def __init__(self, ticket_id, name, staff_id, email, issue):
        """
        Initializes a new Ticket object with provided attributes.

        Args:
            ticket_id (int): Unique identifier for the ticket.
            name (str): Name of the staff member submitting the ticket.
            staff_id (str): Staff ID of the staff member submitting the ticket.
            email (str): Email address of the staff member submitting the ticket.
            issue (str): Description of the issue or assistance request.

        Returns:
            None
        """
        # Initialize ticket attributes
        self.ticket_id = ticket_id
        self.name = name
        self.staff_id = staff_id
        self.email = email
        self.issue = issue
        # Default response and status
        self.response = "Not Provided"
        self.status = "Open"

        # Check if the issue involves changing password
        if "change" in self.issue and "password" in self.issue:
            # Generate new password
            password = staff_id[:2] + name[:3]
            # Update response with new password
            self.response = "Your new password is ->" + password
            # Change ticket status to closed
            self.status = "Closed"
