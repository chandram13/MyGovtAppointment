# Marvish Chandra

import re


def __init__(self, numEmployees, numCustomers):
    self.numEmployees = numEmployees
    self.numCustomers = numCustomers


def united_States_Postal_Service(self, fname, lname, email, operationalDays, operationalHours):
    fname = ""
    refName = re.string("[a-Z]{0,15}$/", fname)
    print(refName)
    lname = ""
    relName = re.string("[a-Z]{0,15}$/", lname)
    print(relName)
    email = ""
    clientEmail = re.string("^(a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.(a-zA-Z]{2,10})$")
    print(clientEmail)

    services = ["Receive & Send Packages", "Purchase Delivery Supplies", "Passport & Green Card Services"]

    operationalDays = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 3, "Saturday": 4}
    operationalHours = [9, 10, 11, 12, 1, 2, 3, 4, 5]
    daysKeys = d.keys()
    print(daysKeys)
    for h in operationalHours:
        print(h)
    if operationalDays.splice(4):
        print(range(operationalHours[0, 4]))


def localLibrary(fname, lname, email, operationalDays, operationalHours):
    fname = ""
    llfName = re.string("[a-Z]{0,15}$/", fname)
    print(llfName)
    lname = ""
    lllname = re.string("[a-Z]{0,15}$/", lname)
    email = ""
    llclientEmail = re.string("^[a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,10})$")
    print(llclientEmail)

    services = ["Loan a Book", "Loan a Movie", "Access a Computer", "Print", "Study"]


def foodDistribution(operationalDays, operationalHours):
    services = ["Donate unexpired goods", "Receive unexpired goods", "Volunteer"]
    operationalDays = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5,
                       "Sunday": 6}
    operationalHours = [9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7]


def clothesDrive(operationalDays, operationalHours):
    services = ["Donate new or used clothing", "Receive clothing", "Volunteer"]


def hospitals(fname, lname, operationalDays, operationalHours):
    fname = ""
    hfName = re.string("[a-Z]{0,15}$/", fname)
    lname = ""


    services = ["Childcare", "Nursing","Surgery","Pharmacy","Cancer treatment","Rehabilitation"]


def financialInstitutions(fname, lname, operationalDays, operationalHours):
    services = ["Borrow money","Deposit money","Withdraw weapon","Setup checking account","Setup savings account"]
