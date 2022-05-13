import pytest 
import pyodbc

# Author - Robert Chapin
# Date Created - 5/12/2022
# This test calls a database request to a local database and gets back country information which it validates all regions between 1-4
def test_execute_sql():
    conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=DESKTOP-3HHOLVA;Trusted_Connection=yes;database=Sandbox")
    cursor = conn.cursor()  
    cursor.execute('SELECT TOP (1000) [country_id],[country_name],[region_id] FROM [Sandbox].[dbo].[countries]')  
    row = cursor.fetchone()
    while row:  
        print(str(row[0]) + " " + str(row[1]) + " " + str(row[2]))
        assert int(row[2]) > 0 and int(row[2] < 5)
        row = cursor.fetchone()  
    conn.close()