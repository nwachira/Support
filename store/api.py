import frappe


@frappe.whitelist()
def newticket(data):
    """
    Creates a new Support Ticket.

    Args:
      data (dict): A dictionary containing the ticket data.

    Returns:
      dict: The newly created ticket document.
    """
  
    newticket = frappe.new_doc('Support Ticket')
    newticket.update(data)
    newticket.insert(ignore_permissions=True)
    newticket.save()
    return newticket
