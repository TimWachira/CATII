# CATII

# Question 1(b)
The relationship between the Customer
and Order Models is a one-to-many
where a single Customer can have 
multiple Orders associated with them, 
but each unique order belongs to only 
one Customer. 

In the Order Model:

order_date: The date and time the order was placed, using auto_now_add to set this field when the order is created.

total_amount: The total cost of the order, using a DecimalField for accuracy in financial data.

customer: A ForeignKey field that establishes the link to the Customer model. It also includes:

on_delete=models.CASCADE: Deletes all associated orders if the customer is deleted.

related_name='orders': Allows reverse lookup from Customer to its related orders.
