## Project 3 - Pizza
### Enda McCarthy
#### Web Programming with Python and JavaScript
#### August 2019

This is a food ordering website. Users are required to register and login before they can place an order.

Once logged in the user can select and customize their order and add it to the shopping cart. They can then checkout using the dummy credit card information provided.

The project was created using the Django framework for Python.

Django admin allows a superuser access to the menu content and the user profiles. The superuser can assign certain users as staff and give them limited permissions in the admin page. The staff will only have the ability to modify the menu content and the prices.

This can be seen by logging into the admin page as a staff member using the following login details:</br>
<strong>Username:</strong> staff</br><strong>Password:</strong> Testing1234</strong>


The following services/features were used for the project:
- <strong>Linode:</strong>  website host
- <strong>Apache:</strong>  web server used to run site
- <strong>Namecheap.com:</strong>  used to buy the domain name (endamccarthy.com)
- <strong>Let's Encrypt/Certbot:</strong>  used to run the site on a secure (HTTPS) link
- <strong>Stripe:</strong>  used for the payment functionality (in test mode)

The styling of the page is used using SASS (.scss).</br>
See link to the project requirements [here](https://docs.cs50.net/web/2019/x/projects/3/project3.html).


There are a number of minor issues which could be resolved given enough time, including:
- The CSS file will not reload on the Apache server after it is edited, it just continues to load the previous file. I tried a number of fixes for this including modifying the Apache config files and cleaning the cache but no luck.
- There are a couple of bugs relating to the order form validations. If the number of toppings selected on a pizza differs from the specified amount an error appears, but this does not clear unless the page is refreshed. Also the submit button will stay disabled even if the number of toppings is rectified.
