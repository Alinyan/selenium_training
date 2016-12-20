# -*- coding: utf-8 -*-

class Account:
    def __init__(self, firstname=None, lastname=None, address1=None, city=None, postcode=None,
                 email=None, phone=None, password=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address1 = address1
        self.city = city
        self.postcode = postcode
        self.email = email
        self.phone = phone
        self.password = password

    def __repr__(self):
        return "%s" \
               % (self.id, self.name)

    def __eq__(self, other):
        return (self.name is None or other.name is None or self.name == other.name)



