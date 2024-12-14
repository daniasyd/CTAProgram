#
# objecttier
#
# Original author: Ellen Kidane
#
# Name: Dania Nazimuddin
# NedID: dnazi2
# Class: CS 341
# Date: 10/11/24
# Overview: Builds Lobbyist-related objects from data retrieved through 
# the data tier.
#
import datatier

##################################################################
#
# Lobbyist:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#
# class Lobbyist:
#     def __init__(self, lobbyist_id, first_name, last_name, phone):
#         self._Lobbyist_ID = lobbyist_id
#         self._First_Name = first_name
#         self._Last_Name = last_name
#         self._Phone = phone

class Lobbyist:
   def __init__ (self, lobbyist_id, first_name, last_name, phone):
      self._lobbyist_id = lobbyist_id
      self._first_name = first_name
      self._last_name = last_name
      self._phone = phone


   @property
   def Lobbyist_ID(self):
      return self._lobbyist_id
   
   @property
   def First_Name(self):
      return self._first_name

   @property
   def Last_Name(self):
      return self._last_name

   @property
   def Phone(self):
      return self._phone


##################################################################
#
# LobbyistDetails:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   Salutation: string
#   First_Name: string
#   Middle_Initial: string
#   Last_Name: string
#   Suffix: string
#   Address_1: string
#   Address_2: string
#   City: string
#   State_Initial: string
#   Zip_Code: string
#   Country: string
#   Email: string
#   Phone: string
#   Fax: string
#   Years_Registered: list of years
#   Employers: list of employer names
#   Total_Compensation: float
#
class LobbyistDetails:
    def __init__(self, lobbyist_id, salutation, first_name, middle_initial, last_name, suffix, address_1, address_2, city, state_initial, zip_code, country, email, phone, fax, years_registered, employers, total_compensation):
        self._lobbyist_id = lobbyist_id
        self._salutation = salutation
        self._first_name = first_name
        self._middle_initial = middle_initial
        self._last_name = last_name
        self._suffix = suffix
        self._address_1 = address_1
        self._address_2 = address_2
        self._city = city
        self._state_initial = state_initial
        self._zip_code = zip_code
        self._country = country
        self._email = email
        self._phone = phone
        self._fax = fax
        self._years_registered = years_registered
        self._employers = employers
        self._total_compensation = total_compensation

    @property
    def Lobbyist_ID(self):
        return self._lobbyist_id

    @property
    def Salutation(self):
        return self._salutation

    @property
    def First_Name(self):
        return self._first_name

    @property
    def Middle_Initial(self):
        return self._middle_initial

    @property
    def Last_Name(self):
        return self._last_name

    @property
    def Suffix(self):
        return self._suffix

    @property
    def Address_1(self):
        return self._address_1

    @property
    def Address_2(self):
        return self._address_2

    @property
    def City(self):
        return self._city

    @property
    def State_Initial(self):
        return self._state_initial

    @property
    def Zip_Code(self):
        return self._zip_code

    @property
    def Country(self):
        return self._country

    @property
    def Email(self):
        return self._email

    @property
    def Phone(self):
        return self._phone

    @property
    def Fax(self):
        return self._fax

    @property
    def Years_Registered(self):
        return self._years_registered

    @property
    def Employers(self):
        return self._employers

    @property
    def Total_Compensation(self):
        return self._total_compensation

##################################################################
#
# LobbyistClients:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#   Total_Compensation: float
#   Clients: list of clients
#
class LobbyistClients:
    def __init__(self, lobbyist_id, first_name, last_name, phone, total_compensation, clients):
        self._lobbyist_id = lobbyist_id
        self._first_name = first_name
        self._last_name = last_name
        self._phone = phone
        self._total_compensation = total_compensation
        self._clients = clients
    
    @property
    def Lobbyist_ID(self):
        return self._lobbyist_id

    @property
    def First_Name(self):
        return self._first_name

    @property
    def Last_Name(self):
        return self._last_name

    @property
    def Phone(self):
        return self._phone

    @property
    def Total_Compensation(self):
        return self._total_compensation

    @property
    def Clients(self):
        return self._clients


##################################################################
# 
# num_lobbyists:
#
# Returns: number of lobbyists in the database
#           If an error occurs, the function returns -1
#
def num_lobbyists(dbConn):
   #count the number of employers in the database
   sql = "SELECT COUNT(*) FROM LobbyistInfo"
   result = datatier.select_one_row(dbConn, sql)
    
   #if there is an error or no result, return -1
   if result is None:
      return -1
   
   return result[0]


##################################################################
# 
# num_employers:
#
# Returns: number of employers in the database
#           If an error occurs, the function returns -1
#
def num_employers(dbConn):
   sql = "SELECT COUNT(*) FROM EmployerInfo"
   result = datatier.select_one_row(dbConn, sql)

   #if there is an error or no result, return -1
   if result is None:
      return -1
    
   return result[0]


##################################################################
# 
# num_clients:
#
# Returns: number of clients in the database
#           If an error occurs, the function returns -1
#
def num_clients(dbConn):
   #count the number of clients in the database
   sql = "SELECT COUNT(*) FROM ClientInfo"
   result = datatier.select_one_row(dbConn, sql)
   
   #if there is an error or no result, return -1
   if result is None:
      return -1
    
   return result[0] #return count of clients


##################################################################
#
# get_lobbyists:
#
# gets and returns all lobbyists whose first or last name are "like"
# the pattern. Patterns are based on SQL, which allow the _ and % 
# wildcards.
#
# Returns: list of lobbyists in ascending order by ID; 
#          an empty list means the query did not retrieve
#          any data (or an internal error occurred, in
#          which case an error msg is already output).
#
def get_lobbyists(dbConn, pattern):
   # query uses SQL wildcards to search by first or last name
   sql = "SELECT Lobbyist_ID, First_Name, Last_Name, Phone FROM LobbyistInfo WHERE First_Name LIKE ? OR Last_Name LIKE ? ORDER BY Lobbyist_ID"

   parameters = [pattern, pattern] #parameters contain the pattern twice for the LIKE conditions in SQL

   #Execute the query and get all matching rows
   rows = datatier.select_n_rows(dbConn, sql, parameters)
    
   #if rows are returned, create Lobbyist objects and add them to list
   lobbyists = []
   if rows is not None:
      for row in rows:
         lobbyists.append(Lobbyist(row[0], row[1], row[2], row[3]))
    
   return lobbyists


##################################################################
#
# get_lobbyist_details:
#
# gets and returns details about the given lobbyist
# the lobbyist id is passed as a parameter
#
# Returns: if the search was successful, a LobbyistDetails object
#          is returned. If the search did not find a matching
#          lobbyist, None is returned; note that None is also 
#          returned if an internal error occurred (in which
#          case an error msg is already output).
#
def get_lobbyist_details(dbConn, lobbyist_id):
   #retireve basic lobbyist information
   sql = """SELECT Lobbyist_ID, Salutation, First_Name, Middle_Initial, Last_Name, Suffix, Address_1, Address_2, 
             City, State_Initial, ZipCode, Country, Email, Phone, Fax 
             FROM LobbyistInfo WHERE Lobbyist_ID = ?
            """
 
   parameters = [lobbyist_id]
    
   row = datatier.select_one_row(dbConn, sql, parameters)
    
   if row is None:
       return None
   
   if len(row) < 15: #ensure all required columns are retrieved
         return None
   
   years_registered = []
   employers = []
   total_compensation = 0.0

   #Fetch the years the lobbyist was registered
   sql_years = "SELECT Year FROM LobbyistYears WHERE Lobbyist_ID = ? ORDER BY Year"
   years_rows = datatier.select_n_rows(dbConn, sql_years, parameters)
   years_registered = [year_row[0] for year_row in years_rows] 
   
   #Get distinct employers of the lobbyist
   sql_employers = """SELECT DISTINCT(e.Employer_Name)
                       FROM LobbyistAndEmployer le
                       JOIN EmployerInfo e ON le.Employer_ID = e.Employer_ID
                       WHERE le.Lobbyist_ID = ?
                       ORDER BY e.Employer_Name"""
   employers_rows = datatier.select_n_rows(dbConn, sql_employers, parameters)
   employers = [emp_row[0] for emp_row in employers_rows]

   #Calculate the total compensation for the lobbyist
   sql_total_compensation = "SELECT SUM(Compensation_Amount) FROM Compensation WHERE Lobbyist_ID = ?"
   total_comp_row = datatier.select_one_row(dbConn, sql_total_compensation, parameters)
   total_compensation = total_comp_row[0] if total_comp_row[0] is not None else 0.0
    
   #return a populated LobbyistDetails object with all retrieved data
   return LobbyistDetails(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], years_registered, employers, total_compensation)
   

##################################################################
#
# get_top_N_lobbyists:
#
# gets and returns the top N lobbyists based on their total 
# compensation, given a particular year
#
# Returns: returns a list of 0 or more LobbyistClients objects;
#          the list could be empty if the year is invalid. 
#          An empty list is also returned if an internal error 
#          occurs (in which case an error msg is already output).
#
def get_top_N_lobbyists(dbConn, N, year):
   # SQL query to retrieve the top N lobbyists based on total compensation for a given year
   sql = """SELECT l.Lobbyist_ID, l.First_Name, l.Last_Name, l.Phone, SUM(c.Compensation_Amount) as Total_Compensation
             FROM LobbyistInfo l 
             JOIN Compensation c ON l.Lobbyist_ID = c.Lobbyist_ID
             WHERE strftime('%Y', c.Period_Start) = ?
             GROUP BY l.Lobbyist_ID
             ORDER BY Total_Compensation DESC
             LIMIT ?"""
    
   parameters = [str(year), N] #make sure year is passed as a string
   rows = datatier.select_n_rows(dbConn, sql, parameters)
    
   lobbyists = []
   if rows is not None:
      for row in rows:
         #get clients for this lobbyist from the Compensation table
         sql_clients = """SELECT ci.Client_Name
                             FROM Compensation co
                             JOIN ClientInfo ci ON co.Client_ID = ci.Client_ID
                             WHERE co.Lobbyist_ID = ? AND strftime('%Y', co.Period_Start) = ?
                             GROUP BY ci.Client_ID, ci.Client_Name
                             ORDER BY ci.Client_Name"""
         client_parameters = [row[0], str(year)]
         client_rows = datatier.select_n_rows(dbConn, sql_clients, client_parameters)
         
         # Extract the client names and append to the clients list
         clients = [client_row[0] for client_row in client_rows]

         #appemd a LobbyistClients object with the details and the clients list
         lobbyists.append(LobbyistClients(row[0], row[1], row[2], row[3], row[4], clients))
    
   return lobbyists #return list of objects


##################################################################
#
# add_lobbyist_year:
#
# Inserts the given year into the database for the given lobbyist.
# It is considered an error if the lobbyist does not exist (see below), 
# and the year is not inserted.
#
# Returns: 1 if the year was successfully added,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def add_lobbyist_year(dbConn, lobbyist_id, year):
   #check if the lobbyist exists in the LobbyistInfo table
   sql_check = """
                  SELECT Lobbyist_ID
                  FROM LobbyistYears 
                  WHERE LobbyistYears.Lobbyist_ID = ?;
                  """
   
   lobbyist_exists = datatier.select_one_row(dbConn, sql_check, [lobbyist_id])

   #no lobbyist with this ID, return 0
   if lobbyist_exists == ():
         return 0 

   #Insert the year into the LobbyistYears table
   sql_insert = """INSERT INTO LobbyistYears(Lobbyist_ID, Year) 
                     VALUES (?, ?);"""

   result = datatier.perform_action(dbConn, sql_insert, [lobbyist_id, year])
   
   return 1 if result == 1 else 0 #return 1 if successfully inserted, else 0
 

##################################################################
#
# set_salutation:
#
# Sets the salutation for the given lobbyist.
# If the lobbyist already has a salutation, it will be replaced by
# this new value. Passing a salutation of "" effectively 
# deletes the existing salutation. It is considered an error
# if the lobbyist does not exist (see below), and the salutation
# is not set.
#
# Returns: 1 if the salutation was successfully set,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def set_salutation(dbConn, lobbyist_id, salutation):
   sql_check = "SELECT Lobbyist_ID FROM LobbyistInfo WHERE Lobbyist_ID = ?"
   if datatier.select_one_row(dbConn, sql_check, [lobbyist_id]) is None:
      return 0
    
   sql_update = "UPDATE LobbyistInfo SET Salutation = ? WHERE Lobbyist_ID = ?"
   result = datatier.perform_action(dbConn, sql_update, [salutation, lobbyist_id])
    
   return 1 if result == 1 else 0