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
    daysKeys = sorted(operationalDays.keys())
    print(daysKeys)
    for h in operationalHours:
        print(h)
    if operationalDays.splice(4):
        print(range(operationalHours[0, 8]))


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

    operationalDays = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5}
    operationalHours = [10, 11, 12, 1, 2, 3, 4, 5, 6, 7]
    libDays = sorted(operationalDays.keys())
    print(libDays)
    for h in operationalHours:
        print(h)
    if operationalDays.splice(5):
        print(range(operationalHours[0,9]))

def foodDistribution(operationalDays, operationalHours):
    services = ["Donate unexpired goods", "Receive unexpired goods", "Volunteer"]
    operationalDays = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5,
                       "Sunday": 6}
    operationalHours = [9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7]
    fooDays = sorted(operationalDays.keys())
    print(fooDays)
    for h in operationalHours:
        print(h)
    if operationalDays.splice(7):
        print(range(operationalHours[0,10]))


def clothesDrive(operationalDays, operationalHours):
    services = ["Donate new or used clothing", "Receive clothing", "Volunteer"]
    operationalDays = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
    operationalHours = [9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7]
    clothesDays = sorted(operationalDays.keys())
    print(clothesDays)
    for h in operationalHours:
        print(h)
    if operationalDays.splice(7):
        print(range(operationalHours[0,10]))

def hospitals(fname, lname, operationalDays, operationalHours):
    fname = ""
    hfName = re.string("[a-Z]{0,15}$/", fname)
    print(hfName)
    lname = ""
    hlName = re.string("[a-Z]{0,15}$/", lname)
    print(hlName)

    services = ["Childcare", "Nursing", "Surgery", "Pharmacy", "Cancer treatment", "Rehabilitation"]
    operationalDays = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
    operationalHours1 = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    operationalHours2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    hospitalDays = sorted(operationalDays.keys())
    print(hospitalDays)
    if operationalDays.splice(7):
        print(range(operationalHours1[0,11]))
        print(range(operationalHours2[0,11]))

def financialInstitutions(fname, lname, operationalDays, operationalHours):
    fname = ""
    ffiName = re.string("[a-Z]{0,15}$/", fname)
    print(ffiName)
    lname = ""
    lfiName = re.string("[a-Z]{0,15}$/", lname)
    print(lfiName)

    services = ["Borrow money", "Deposit money", "Withdraw weapon", "Setup checking account", "Setup savings account"]
    operationalDays = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5}
    operationalHours = [9, 10, 11, 12, 1, 2, 3, 4, 5, 6]
    financialDays = sorted(operationalDays.keys())
    print(financialDays)
    if operationalDays.splice(6):
        print(range(operationalHours[0,10]))


