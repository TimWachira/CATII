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


# HOW TO SET UP THE ENVIRONMENT #

# 1. Clone the Repository
Using this url, clone the repo to your 
machine using GitClassroom,
https://github.com/TimWachira/CATII.git

Then Navigate to the project directory
 using the following command 'cd 
 Ecommerce'

# 2. Create and Activate a Virtual Env 
Create a virtual env and activate, 
this is to isolate dependencies. 

# 3. Install Django and test server
Make sure Django is installed, and use 
the link, http://127.0.0.1:8000/ to 
verify the installation is working.

# 4. Create a SuperUser Account
This is to limit access to the db, and 
ensure privacy, in your terminal run 
the code, 'python manage.py 
createsuperuser' and follow the 
instructions to set up your account. 

# 5. Run the server
Use the link http://127.0.0.1:8000/
admin/. to access and alter relations 
for customer and orders. 