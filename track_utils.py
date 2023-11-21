import sqlite3
import threading

# Create a thread-local storage for connections
_thread_local = threading.local()

# Function to get a thread-local connection
def get_connection():
    if not hasattr(_thread_local, 'connection'):
        _thread_local.connection = sqlite3.connect('data.db')
    return _thread_local.connection

# Function to create the pageTrackTable
def create_page_visited_table():
    connection = get_connection()
    with connection:
        c = connection.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS pageTrackTable(pagename TEXT, timeOfvisit TIMESTAMP)')

# Function to add page visited details
def add_page_visited_details(pagename, timeOfvisit):
    connection = get_connection()
    with connection:
        c = connection.cursor()
        c.execute('INSERT INTO pageTrackTable(pagename, timeOfvisit) VALUES (?, ?)', (pagename, timeOfvisit))

# Function to view all page visited details
def view_all_page_visited_details():
    connection = get_connection()
    with connection:
        c = connection.cursor()
        c.execute('SELECT * FROM pageTrackTable')
        data = c.fetchall()
        return data

# Function to create emotionclfTable
def create_emotionclf_table():
    connection = get_connection()
    with connection:
        c = connection.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS emotionclfTable(rawtext TEXT, prediction TEXT, probability NUMBER, timeOfvisit TIMESTAMP)')

# Function to add prediction details
def add_prediction_details(rawtext, prediction, probability, timeOfvisit):
    connection = get_connection()
    with connection:
        c = connection.cursor()
        c.execute('INSERT INTO emotionclfTable(rawtext, prediction, probability, timeOfvisit) VALUES (?, ?, ?, ?)',
                  (rawtext, prediction, probability, timeOfvisit))

# Function to view all prediction details
def view_all_prediction_details():
    connection = get_connection()
    with connection:
        c = connection.cursor()
        c.execute('SELECT * FROM emotionclfTable')
        data = c.fetchall()
        return data
