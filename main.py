#
# # Name: Dania Nazimuddin
# NedID: dnazi2
# Class: CS 341
# Date: 10/16/24
# Overview: This program interacts with a SQLite database to manage
# and retrieve information about lobbyists, employers, and clients
# in Chicago. The application allows the user to execute various
# commands such as querying lobbyist details, top lobbyists, adding
# registration years, and updating salutation information
#
import sqlite3
import objecttier
##################################################################  


##################################################################  
# print_stats
# Prints out general statistics about the database, including
# the number of lobbyists, employers, and clients
# 
def print_stats(dbConn):
 
    num_lobbyists = objecttier.num_lobbyists(dbConn)

    num_employers = objecttier.num_employers(dbConn)

    num_clients = objecttier.num_clients(dbConn)

    #Print the general statistics with formatted values
    print("General Statistics:")
    print(f"  Number of Lobbyists: {num_lobbyists:,}")  # formatted with commas
    print(f"  Number of Employers: {num_employers:,}")  # formatted with commas
    print(f"  Number of Clients: {num_clients:,}")      # formatted with commas


#################################################################
# command_1
#
#  Executes the command to find and display lobbyists whose first or 
# last name matches the user input. The input can include SQL 
# wildcards _ and % for pattern matching.
#
def command_1(dbConn):

    print()
    #prompt the user to input a lobbyist's first or last name
    lobbyist_name = input("Enter lobbyist name (first or last, wildcards _ and % supported): ").strip()

    #get lobbyists that match the name pattern
    lobbyists = objecttier.get_lobbyists(dbConn, lobbyist_name)

    num_lobbyist = (len(lobbyists))
    print()
    print("Number of lobbyists found:", f"{num_lobbyist}")

    # if the number of lobbyists exceeds 100  request to narrow down search
    if(num_lobbyist>100):
        print("There are too many lobbyists to display, please narrow your search and try again...")
        return

    #display lobbyist detials
    for l in lobbyists:
        print(l.Lobbyist_ID, " : ",
        l.First_Name, " ", l.Last_Name, 
        " Phone: ", l.Phone)


#################################################################
# command_2
#Executes the command to retrieve and display detailed information 
# about a lobbyist 
#
def command_2(dbConn):
    print()

    id = input("Enter Lobbyist ID: ").strip()

    #fetch the lobbyist's detailed information
    details = objecttier.get_lobbyist_details(dbConn, id)
    print()

    #if no lobbyist exists
    if details is None:
        print("No lobbyist with that ID was found.")
        return

    #Display the lobbyist's full details
    print(id, ":")
    print(f"  Full Name: {details.Salutation} {details.First_Name} {details.Middle_Initial} {details.Last_Name} {details.Suffix}")
    print(f"  Address: {details.Address_1} {details.Address_2} , {details.City} , {details.State_Initial} {details.Zip_Code} {details.Country}")
    print(f"  Email: {details.Email}")
    print(f"  Phone: {details.Phone}")
    print(f"  Fax: {details.Fax}")

    #print years the lobbyist was registered
    print("  Years Registered: ", end= "")
    if details.Years_Registered:
        print(", ".join(map(str, details.Years_Registered)) + ", ")
    
    #print employers
    print("  Employers: ", end = "")
    if details.Employers:
        print(", ".join(map(str, details.Employers)) + ", ")

    #print total compensation
    print(f"  Total Compensation: ${details.Total_Compensation:,.2f}")


#################################################################
# command_3
#
# Executes the command to find and display the top N lobbyists based
# on total compensation for a specific year. The user is prompted to
# enter the number N and the year.#  
#
def command_3(dbConn):
    print()

    #get number of lobbyisys to retrieve
    n = int(input("Enter the value of N: ").strip())
    
    #Ensure that N is positive 
    if n  <= 0:
        print("Please enter a positive value for N...")
        return

    year = input("Enter the year: ").strip()

    #fetch the top N lobbyists by total compensation for the given year
    lobbyists = objecttier.get_top_N_lobbyists(dbConn, n, year)
    print()

    #display the top N lobbyists info
    i = 1
    for l in lobbyists:
        print(f"{i} . {l.First_Name} {l.Last_Name}")
        print(f"  Phone: {l.Phone}")
        print(f"  Total Compensation: ${l.Total_Compensation:,.2f}")

        #print the clients associated with the lobbyist
        print(f"  Clients: ", end ="")
        if l.Clients:
            print(", ".join(map(str, l.Clients)) + ", ")
        i+=1


#################################################################
# command_4
#
#Executes the command to add a registration year for a lobbyist.
# The user is prompted to enter a year and the lobbyist's ID.#  
#
def command_4(dbConn):
    print()

    #prompt the user to input the year and lobbyist I
    year = input("Enter year: ").strip()
    id = input("Enter the lobbyist ID: ").strip()

    # add the registration year to database
    add = objecttier.add_lobbyist_year(dbConn, id, year)
    print()

    if add is None:
        print("No lobbyist with that ID was found.")
        return

    #check if the lobbyist was found and registered successfully
    if add == 1:
        print("Lobbyist successfully registered.")
    else:
        print("No lobbyist with that ID was found.")


#################################################################
# command_5
#Executes the command to update the salutation of a lobbyist.
# The user is prompted to enter the lobbyist's ID and new salutation.
#  
#
def command_5(dbConn):
    print()

    #user inputs the lobbyist ID and salutation
    id = input("Enter the lobbyist ID: ").strip()
    salutation = input("Enter the salutation: ").strip()

    #Update the lobbyists salutation in  database
    result = objecttier.set_salutation(dbConn, id, salutation)
    print()

    #Check if the salutation set successfully
    if result == 0:
        print("No lobbyist with that ID was found.")
    else:
        print("Salutation successfully set.")


##################################################################  
#
# main
#
def main():
    print('** Welcome to the Chicago Lobbyist Database Application **')
    print()
    dbConn = sqlite3.connect('Chicago_Lobbyists.db')
    print_stats(dbConn)
    
    while True:
        print()
        command = input("Please enter a command (1-5, x to exit): ")

        if command == 'x':
           break
        elif command == '1':
            command_1(dbConn)
        elif command == '2':
            command_2(dbConn)
        elif command =='3':
            command_3(dbConn)
        elif command =='4':
            command_4(dbConn)
        elif command =='5':
            command_5(dbConn)
        else:
            print("**Error, unknown command, try again...")

    dbConn.close()

main()


#
# done
#
