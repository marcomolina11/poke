from __future__ import unicode_literals
from django.db import models
from re import match, search
from bcrypt import hashpw, gensalt

class UserManager(models.Manager):
    def register(self, email, first_name, last_name, alias, password, confirm_password, csrfmiddlewaretoken):
        messagelist = []
        # Validate email
        email = email[0]
        if not match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', email):
            messagelist.append("Invalid email address")
        elif User.objects.filter(email=email):
            messagelist.append("Email Address already in use")
        # Validate first_name
        first_name = first_name[0]
        if len(first_name) < 2:
            messagelist.append("First Name must be at least 2 characters long")
        elif search(r'[^a-zA-Z]', first_name):
            messagelist.append("First Name must only contain letters")
        # Validate last_name
        last_name = last_name[0]
        if len(last_name) < 2:
            messagelist.append("Last Name must be at least 2 characters long")
        elif search(r'[^a-zA-Z]', last_name):
            messagelist.append("Last Name must only contain letters")
        # Validate alias
        alias = alias[0]
        if len(alias) < 2:
            messagelist.append("Alias must be at least 2 characters long")
        elif search(r'[^a-zA-Z]', alias):
            messagelist.append("Alias must only contain letters")
        # Validate password
        password = password[0]
        if len(password) < 8:
            messagelist.append("Password must be at least 8 characters long")
        # Validate conf_password
        conf_password = confirm_password[0]
        if conf_password != password:
            messagelist.append("Password does not match")
        # Check if all validation checks passed
        if len(messagelist) == 0:
        # If the are no errors, create pw_hash and then create user
            pw_hash = hashpw(password.encode(), gensalt())

            new_user = User.objects.create(email=email, first_name=first_name, last_name=last_name, alias=alias, password=pw_hash)
            return (True, new_user.id)

        else:
            return (False, messagelist)

    def login(self, email, password):
        if User.objects.filter(email=email):
            user = User.objects.get(email=email)
            if hashpw(password.encode(), user.password.encode()) == user.password:
                return (True, user.id)
            else:
                return (False, "Invalid password")
        else:
            return (False, "Invalid email address")

    def editInfo(self, user_id, email, first_name, last_name, csrfmiddlewaretoken):
        messageList = []
        #Validate email
        email = email[0]
        if not match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', email):
            messagelist.append("Invalid email address")
        # Validate first_name
        first_name = first_name[0]
        if len(first_name) < 2:
            messagelist.append("First Name must be at least 2 characters long")
        elif search(r'[^a-zA-Z]', first_name):
            messagelist.append("First Name must only contain letters")
        # Validate last_name
        last_name = last_name[0]
        if len(last_name) < 2:
            messagelist.append("Last Name must be at least 2 characters long")
        elif search(r'[^a-zA-Z]', last_name):
            messagelist.append("Last Name must only contain letters")
        
        #validations
        if len(messageList) > 0:
            return (False, messageList)

        self.filter(id=user_id).update(email=email, first_name=first_name, last_name=last_name)

        return (True, ["User Info updated successfully"])

    def editPassword(self, user_id, password, confirm_password, csrfmiddlewaretoken):
        messagelist = []
        # Validate password
        password = password[0]
        if len(password) < 8:
            messagelist.append("Password must be at least 8 characters long")
        # Validate conf_password
        conf_password = confirm_password[0]
        if conf_password != password:
            messagelist.append("Password does not match")
        # Check if all validation checks passed
        if len(messagelist) > 0:
            return(False, messagelist)

        pw_hash = hashpw(password.encode(), gensalt())

        self.filter(id=user_id).update(password=pw_hash)

        return (True, ["User Info updated successfully"])


class User(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    alias = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    userManager = UserManager()
    objects = models.Manager()

    def __str__(self):
        return self.first_name
