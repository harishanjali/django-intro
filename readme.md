#admin page django
#authorization and authentication
#only admin can have rights to do crud operations on product table, not for users.

#to access the admin page
step 1: py manage.py createsuperuser
step2: type base_url/admin then page will open
step3: you can see the page with details
if you wants to give access to tables, you can give like this in admin.py file
admin.site.register(Product)