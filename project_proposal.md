# Candidate Number: 260032

## Project Notes

---

### Abstract

- **Novel Nook** is an online platform that provides a comprehensive digital library for students, offering access to a vast collection of academic textbooks and learning resources.
- It aims to revolutionize the way students access and engage with educational materials by providing an affordable, convenient, and environmentally friendly alternative to traditional print textbooks.
- The site's core focus is on making education more accessible and affordable for students worldwide.
- **Novel Nook** offers a subscription-based model that grants students unlimited access to a wide range of textbooks and learning materials at a fraction of the cost of purchasing physical copies. This approach enables students to save money, reduce the burden of carrying heavy textbooks, and access resources conveniently from any device with internet connectivity.
- The resources emphasize user experience and functionality, providing students with intuitive features such as highlighting, note-taking, and search capabilities within the digital texts. These features enhance the learning experience, allowing students to personalize their study materials and easily find relevant information.
- **Novel Nook** aims to disrupt the traditional textbook market by offering a modern, cost-effective, and eco-friendly solution for students. With its extensive library, user-friendly interface, and commitment to accessibility and sustainability, Perlego serves as a valuable resource for students seeking an efficient and affordable way to access educational materials.

### Introduction

The

### Aims & Objectives

The proposed project is an ecommerce web application for students to shop for learning resources.

### Issues/Errors

- Session ID is only generated only when user is in the basket page.
- When the basket subtotal was added to the basket page, it did not show. Resolved by adding the quantity to the delete basket from the summary template, `document.getElementById("basket-qty").innerHTML = json.qty`
- When item was deleted from the basket, the number counter in the basket icon showed `undefined` instead of updating the value.

``` python
Error: ecommerce/basket/views.py", line 30, in basket_delete
    product_id = int(request.POST.get('productid'))
TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'
```

- Edit account detail does not work, shows 200 status code but does not change username

#### Sessions

- Session is temporary and interactive information
- Single user per session - save retrieve arbitrary data on a per-site-visitor basis
- Store the data on the server side
- User recieves a session ID
- Session ID is used to retrieve the associated data

![Sessions](./media/images/sessions.png)

#### Sessions Set up

- Setup
- Create session
- context processor (site-wide access)
- Add to session functionality

### Part 2

#### Sessions development - Delete Session data

- View all items in the basket
- Add a delete button
- Create AJAX request to delete item
- Add new function in Basket class
- JS - remove item from basket

#### Sessions development - Updating the data

- send an update request from Ajax
- Handling the update request (qty)
- Change the front-end data (price and qty)
- Develop the front-end code to update the basket
- Debug issues
- Testing

### Part 3 - Ecommerce store user, payment and other management

- Refactoring - style/UI updates
- User Management - Signup, Login, Logout, Dashboard, Password Reset
- Payment - Template, Payment, Capture
- Order Management
- Testing

### Login Details

```python
email: a@a.com
username: john
password: johnjohn1
```
