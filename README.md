[![Build Status](https://travis-ci.org/markofsuccess/fullstack-ecommerce.svg?branch=master)](https://travis-ci.org/markofsuccess/fullstack-ecommerce)


# Executive Summary of The Website

The last milestone project for my school [Code Insitute](https://codeinstitute.net/). A Full-Stack Django Frameworks ecommerce site where users can browse for smartphones and make an order if the want with Stripe payment option integrated. You can try and make an order by registering as an user and at the checkout form you can put in the card number 4242424242424242 and 123 as the CVV number. Databases are stored with Postgres and SQlite. Stripe Test API is used for this project as no real products are sold.

## The Goal & Purpose of The Website

### The Goal

* The End Goal of the website is to sell smartphones and make it an easy and simple way for the customer to do so.

 There are many smartphones on the page, the customer can inspect each and one of them by clicking on more details to see specifications and pictures of each smartphone. There the customer can choose to add the product to the cart by pressin add to cart or press continue shopping if he/she wants to continue browsing other smartphones.

 Customers can choose what smartphones they like and put in the quantity they want and its added to the cart. If they like to proceeed with the purchase, they press on the cart icon in the navbar and then the checkout button to come to the checkout form. If the customers like to remove a product from the cart, they press on the cart in the navbar and then press the ammend button and choose quanitity.

### Purpose

* The purpose of the website is to show how with Django frameworks, Python and Stripe API you can create an fully functional e-commerce site where the business owner can host their ecommerce shop with an secure  and well known payment processor as Stripe.

# UX

The website is for visitors who are intrested in smartphones and purchasing smartphones.

* As a user, I want to know more about a specific smartphone and its specifications by pressing on the more   details button. And by pressing on each product image, the image is zoomed in to make it larger.

* As a user, I want to search the site for a specific smartphone that I'm intrested in.

* As a user, I can register an unique profile with a unique profile name by clicking on the register icon     in the navbar.

* As s user, I can choose between logging in with my username or email address by clicking on the login       button in the navbar.

* As a user, I want to make an secure payment with a well known and secure payment provider as Stripe.

* As a user, I want to be able to ammend a product if I regret adding it to the cart, by pressing the         ammend button in the cart page.

* As a user, I can retrieve the password to my profile if I forgot it by pressing on the forgot my            password link in the login page.

* As a user, I can see how much a product costs, all prices of each product are specified in Euro under       each item, and at the checkout you can see the total amount stated in Euro.

* As a user, I can add a product to the cart by choosing the quantity and pressin on the add button.

* As a user, the only way to purchase a product is by logging in/ register a new user.

* As a user, I can watch the carousel images displaying different smartphones in a bigger frame.


## Design

* The design is a simple with all content & products on 1 page. The navbar has register, login and cart icons. The smartphone logo takes you back to the homepage. There is a search bar where users can search for items. Added carousel images of different smartphones making it more interactive for the user. The footer has icons of all the payments details avaiable on the page.

## Mockup

* The mockup was partly inspired by my [third milestone project](https://python-mobilephone-review.herokuapp.com/) and the rest was designed throughout the project.

# Features

## Existing Features

* The user can search any product by using the search bar.
* The user can add any product they like by choosing quantity and clicking the add button.
* The user can press on the more details button on each item to find out more information about the product.
* The user can register and profile by clicking on register icon in the navbar.
* The user can login with their email or username by clicking on the login icon in the navbar.
* The user can inspect the cart by clicking on the cart icon the navbar.
* The user can ammend any product by clicking the ammend button in the cart page.
* The user can checkout by pressin on the checkout button in the cart page.
* The user can log out by pressing the log out button in the navbar.
* The user can make an purchase by clicking on the submit a payment in the checkout page.
* The user can press on each product image to increase the size of it in the product details page.
* The user can retrieve their password by clicking on the forgot my password link in the login page.


## Features Left to Impelemt

* Adding more product categories such as tables and computers
* Creating a contact page for users to get in contact.
* Styling the page more interactive and responsive.

## Techonologies Used

* [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)

* [CSS3](https://developer.mozilla.org/en-US/docs/Archive/CSS3)
- Boostrap was used mainly to make the website responsive on multiple devices using bootstrap grid.   

* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- Stripe JavaScript was used to render the payment processing.

* [Gitpod](https://www.gitpod.io/)
- Gitpod was the platform used to code the whole project with.

* [jQuery](https://jquery.com/)
- The project uses JQuery to simplify DOM manipulation.

* [Github](https://github.com/)
- Github was used to document the project progress.

* [HTML Validator](https://validator.w3.org/)
- This was used to validate the HTML code.

* [HTML Formatter](https://htmlformatter.com/)
- This was used for formatting the HTMl code.

* [Stripe](https://stripe.com/)
- Stripe is used for to make payments securely on any products on the page.

* [Materialize](https://materializecss.com/)
- Materialize was used for the materialize box image class, when pressing on the product details images to    increase the size of it.

* [Postgres](https://www.postgresql.org/)/ [Sqlite3](https://www.sqlite.org/index.html)
- These were used for storing Databases.

* [Heroku](www.heroku.com)
- Heroku was used for hosting the web page.

* [Django](https://www.djangoproject.com/)
- Django frameworks were used for this project.

* [Python3](https://www.python.org/)
- Python3 was used for this project.

* [Font Awesome](https://fontawesome.com/)
- Font Awesome was used to style the fonts/icons of the page.

* [Chrome Devtools](https://developers.google.com/web/tools/chrome-devtools)
- Google Chrome Devtools was used for inspecting webpage for any errors and used for designing the page in a faster way.

* [AWS](aws.amazon.com/)
‎- Amazon Web Services was used to host the media and static files for the project.
‎
# Testing

## Broswers

* The website was tested on the Google Chrome browser, Safari, Firefox Quantum and Brave broswer to make sure that everything loaded smoothly and looked proper across different browsers.

* Google Chrome Version 76.0.3809.132

* Brave Version 0.61.52 Chromium: 73.0.3683.86

* Safari Version 12.1.2 (14607.3.9)

* Firefox Quantum version 69.01

* Samsung Internet Browser on Samsung Galaxy S10, Version 10.1.00.27

* Chrome Broswer on Samsung Galaxy S10, version 77.0.3865.92

* Brave Broswer on Samsung Galaxy S10, Chromium 80.0.3987.119

## Responsivness

* The site was tested on multiple devices using Google chrome developer tools to see the responsivness for different media devices. The devices that were tested were: Samsung S5, Samsung Galaxy s10, iPhone X, iPhone 5/6/7/8, iPhone 6/7/8 Plus, iPad and iPad Pro.

## Tests.py

* The tests.py file was test and test were successful as you can see in the picture below. The Database URL not found, used SQLite instead.

## Registration & Login

* Created multiple accounts and used the Django admin panel to see if users have been registered.
* After Register and logging in there should pop up a green message either "you have succssfully registered" or "you        have successfully logged in". 
* Click on the profile icon to see what email address you are logged in with.
* Once registered and logged in you can proceed to the checkout form.
* If not logged in you can add items to the cart but you can't proceed to the checkout without logging in.
* You can succesfully log in with both username and email.

## Log out

* When clicking log out - a pop message with "You have successfully logged out" appears.
* If trying to checkout from cart logged out - you will be redirected to log in page.

## Reset Password Function

## Products

* If trying to click add on a product without specifying quantity - pop up with this field is required.
* When clicking on more details button - redirected succsfully to that item page.
* In the product details page - you need to specify amount in order to add to cart. 
* When clicked on continue shopping - gets redirected to products page.
* Clicking on product image to see if it image increases.
* In the Django Admin Panel - Check if edit/delete Product and Product images are possible. 


## Submit Payment & Ammend

* At the checout form, if any field is missing and you try to submit payment, pop up messsage with fil in this field is     required.
* Amend a item in the cart by choosing quantity 1 to delete item from cart.
* In the Django Admin Panel - Checkout - Orders to see all succesful orders registered.
* Once filled in the checkout form and clicked submit payment, a pop up message with "You have succesfully paid" shows      up. Also checked my Stripe dashboard for succesful payments. See picture below.

## Travis 

* Travis was used to scan packages and libraries for bugs and anything that might damage travis or the server, to ensure    that that server is safe and free of code that might be dangerous. All tests were passed, see the green build passing     button in top of the README file and see pictures below.

## Bugs

* After doing a search or submit payment it redirects to products page but carousel images not displaying.

## Code Validators

* The CSS and HTML code was validated using validators.

# Deployment

# Credits

## content
* The images on all the smartphones were from [MediaMarkt] (https://www.mediamarkt.se/)
* The Profile Registration & Log in functions was used from the Code Institute course lesson [Authentication & Authorisation](https://courses.codeinstitute.net/courses/course-v1:CodeInstitute+F101+2017_T1/courseware/c237a0c4183442698c6602454dbf011a/5434e9d235c844678d18d4d05bf9f63c/?activate_block_id=block-v1%3ACodeInstitute%2BF101%2B2017_T1%2Btype%40sequential%2Bblock%405434e9d235c844678d18d4d05bf9f63c)
* Parts of the design and wiring of the project was learned from the Code Institute course lesson [Putting It All Together | ECommerce Mini Project](https://courses.codeinstitute.net/courses/course-v1:CodeInstitute+F101+2017_T1/courseware/c95cdb47b7bb40e49bbfb75cb4c29114/01fbdaedba5d4db19ad118cbe07c1ab7/?activate_block_id=block-v1%3ACodeInstitute%2BF101%2B2017_T1%2Btype%40sequential%2Bblock%4001fbdaedba5d4db19ad118cbe07c1ab7)

## Aknowledgements

* Thanks to all the great tutors on Code institute for being a great support through the entire course.
* Thanks to my Mentor Antonia Simic for helping me with the projects.
* Thanks to my school [Code Institute](https://codeinstitute.net/) for creating a great Full-Stack Developer Education.


