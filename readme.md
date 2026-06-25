#admin page django
#authorization and authentication
#only admin can have rights to do crud operations on product table, not for users.

#to access the admin page
step 1: py manage.py createsuperuser
step2: type base_url/admin then page will open
step3: you can see the page with details
if you wants to give access to tables, you can give like this in admin.py file
admin.site.register(Product)

#common questions rises in our mind
1. Store Employee Details
Simple Definition: A Django model is a Python class that represents a database table. Each attribute in the class represents a column in the table.

how to write
from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_name=100)
    last_name = models.CharField(max_name=100)
    hire_date = models.DateField()

2. Add a New Field Without Losing Data
Simple Definition: To add a field safely, you must provide a default value or allow it to be empty (null=True). Then, you run migrations to update the database schema without wiping existing rows.

write
class Employee(models.Model):
    # ... existing fields ...
    department = models.CharField(max_length=100, default="Unassigned")

python manage.py makemigrations
python manage.py migrate

3. Implement Soft Delete
Simple Definition: Instead of permanently erasing a database row, "soft deleting" marks a row as inactive (usually with a boolean flag like is_deleted), keeping the data intact for records.

from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)

    def soft_delete(self):
        self.is_deleted = True
        self.save()

4. Enforce Unique Email Addresses
Simple Definition: You use the unique=True constraint on a model field. This tells the database to reject any new entry that tries to reuse an email address already in that column.

class Employee(models.Model):
    email = models.EmailField(unique=True)

5. Store Uploaded Profile Pictures
Simple Definition: You use an ImageField, which stores the file path string in the database while uploading the actual file to your server's media storage directory.

class Employee(models.Model):
    # Requires the 'Pillow' library installed via pip
    profile_picture = models.ImageField(upload_to='profile_pics/')

Views & Templates
6. Display Data from a Model in a Template
Simple Definition: Fetch the records using Django's ORM in your view, pass them to the template, and use a Jinja-like {% for %} loop to display them.

How to write it:

View (views.py):
from django.shortcuts import render
from .models import Employee

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees.html', {'employees': employees})


7. Show Only Active Users
Simple Definition: Use the .filter() method in your Django ORM query to select only the records where the active status is set to True.
from django.contrib.auth.models import User
from django.shortcuts import render

def active_users_view(request):
    active_users = User.objects.filter(is_active=True)
    return render(request, 'active_users.html', {'users': active_users})

8. Pass Data from a View to a Template
Simple Definition: Data is passed via a Python dictionary called the context. The keys in this dictionary become variables you can use inside your HTML template.

def my_view(request):
    # The dictionary {'app_name': 'Employee Portal'} is the context
    return render(request, 'home.html', {'app_name': 'Employee Portal'})

<h1>Welcome to {{ app_name }}</h1>

9. Implement Search Functionality in a List View
Simple Definition: Grab the search term from the URL query parameters using request.GET and use __icontains (case-insensitive search) to filter your database records.

def employee_search(request):
    query = request.GET.get('q', '') # Looks for ?q=search_term in URL
    if query:
        results = Employee.objects.filter(first_name__icontains=query)
    else:
        results = Employee.objects.all()
        
    return render(request, 'search.html', {'results': results, 'query': query})

10. Handle a 404 Page (Not Found)
Simple Definition: Use Django's built-in get_object_or_404() shortcut in your view. If the record isn't found, Django automatically stops execution and serves a 404 error page.

from django.shortcuts import render, get_object_or_404
from .models import Employee

def employee_detail(request, emp_id):
    # If employee with id doesn't exist, throws a 404 instantly
    employee = get_object_or_404(Employee, id=emp_id)
    return render(request, 'detail.html', {'employee': employee})



#authentication and autherization

To use authentication mixins like LoginRequiredMixin, Django needs to know how to log users in and out.

The simplest way to implement this is by using Django’s built-in, production-ready auth views (LoginView and LogoutView). 
You don't have to write any backend logic—Django handles the authentication; you just supply the HTML template.

Here is the step-by-step setup to get it working effortlessly.

#apis concept
-first pip install django-rest-framework
-then create apis using this framework
-status code is very important in api call
-200 ok
-404 not found
-400 bad request etc.
#for testing api you can use rest web page given by rest framework(browsable api)
# go and type http://127.0.0.1:8000/api/products/
    -list of product objects will come in array in JSON


    {
    "id": 2,
    "pname": "Fridge",
    "pprice": 54000.0,
    "c_gst":100,
    "s_gst":100
}

# simple jwt token
    --after successful login it will return refersh token and access token
    --{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc4MjI4MTkwMSwiaWF0IjoxNzgyMTk1NTAxLCJqdGkiOiJmMjczNDY2YzIxMWQ0MGFkOTNmZGU1MTY3ZTgwZDAzMyIsInVzZXJfaWQiOiI1In0.qbLdmuogqGckBM2yoRuSlUIbleUVU1GxDN2sAL5uC5Y",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzgyMTk1ODAxLCJpYXQiOjE3ODIxOTU1MDEsImp0aSI6IjZhNzhhYzQxMDhiNjRjMzI4NmRjNThlNTc1MjQ5ZDI0IiwidXNlcl9pZCI6IjUifQ.lb9ZIeXGx4v3aaJ64yjWATMRxjy_RBazEH8dNjaJBS8"
}

# how to access the secured api
    --you have to include jwt access token in headers
    url = 'api/login'
    user_data={"username":"vcube","password":"vcube@123"}
    resp = requests.post(url,user_data)
    token = resp.json()['access']

    get_url = 'products/'
    resp = requests.get(get_url,headers={
        "Authorization":f"Bearer {token}"
    })
    print(resp)
    print(resp.json())

## cors headers
    --added cors headers to give access to other origins
    --attaching the backend to front end by this cors headers.