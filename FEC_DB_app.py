from tkinter import *
from tkinter import ttk, messagebox
from tkinter.ttk import Scrollbar, Treeview
import mysql.connector
from mysql.connector import Error

# ======================================== SQL Database Connection ========================================

# Replace with your database connection details
host = "localhost"
user = "root"
password = "password"   # Replace with your users MySQL password
database = "database"     # Replace with your database name

try:
    # Connect to the MySQL server
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
)
    
    if connection.is_connected():
        print("The connection to the MySQL database was successful.")
except Error as e:
        print(f"The error '{e}' occurred")

# ======================================== Table Windows ========================================

cursor = connection.cursor()
# ==================== Election Window ====================
def open_election_window():
    # function to show everything in the table
    def fetch_data():
        cursor.execute("SELECT * FROM election")
        rows = cursor.fetchall()
        if len(rows) != 0:
            election_table.delete(*election_table.get_children())
            for row in rows:
                election_table.insert("", END, values=row)
            connection.commit()

    #function to highlight a row that you click on
    def get_cursor():
        cursor_row = election_table.focus()

    # ==================== Button Windows ====================
    def election_insert_window():
        def submit_query():
            insert_query = "INSERT INTO Election (ElectionID, ElectionName, Date, State) VALUES (%s, %s, %s, %s)"
            election_data = (election_ID_entry.get(), election_name_entry.get(),
                             election_date_entry.get(), election_state_entry.get())
            cursor.execute(insert_query, election_data)
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Inserted Successfully")

        insert_window = Toplevel(window)
        insert_window.title("Election Insert")
        insert_window.geometry("500x400")
        Label(insert_window, font=("", 15, "bold"), text="Insert Election").pack()

        InfoFrame = Frame(insert_window)
        InfoFrame.place(x=0, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Enter Info")
        infoFrame.grid(row=0, column=0)

        election_ID_label = Label(infoFrame, font=("", 15), text="Enter Election ID", height=1)
        election_ID_label.grid(row=1, column=0)
        election_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        election_ID_entry.grid(row=1, column=1)

        election_name_label = Label(infoFrame, font=("", 15), text="Enter Election name", height=1)
        election_name_label.grid(row=2, column=0)
        election_name_entry = Entry(infoFrame, font=("", 15), width=18)
        election_name_entry.grid(row=2, column=1)

        election_date_label = Label(infoFrame, font=("", 15), text="Enter Election date", height=1)
        election_date_label.grid(row=3, column=0)
        election_date_entry = Entry(infoFrame, font=("", 15), width=18)
        election_date_entry.grid(row=3, column=1)

        election_state_label = Label(infoFrame, font=("", 15), text="Enter Election state", height=1)
        election_state_label.grid(row=4, column=0)
        election_state_entry = Entry(infoFrame, font=("", 15), width=18)
        election_state_entry.grid(row=4, column=1)

        SubmitFrame = Frame(insert_window)
        SubmitFrame.place(x=0, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        insert_window.grab_set()

    def election_update_window():
        def submit_query():
            update_query = "UPDATE Election SET ElectionName=%s, Date=%s, State=%s WHERE ElectionID=%s"
            cursor.execute(update_query, (election_name_entry.get(), election_date_entry.get(),
                                          election_state_entry.get(), election_ID_entry.get()))
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Updated Successfully")

        update_window = Toplevel(window)
        update_window.title("Election Update")
        update_window.geometry("500x400")
        Label(update_window, font=("", 15, "bold"), text="Update Election").pack()

        InfoFrame = Frame(update_window)
        InfoFrame.place(x=0, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Enter Info")
        infoFrame.grid(row=0, column=0)

        election_ID_label = Label(infoFrame, font=("", 15), text="Enter Election ID", height=1)
        election_ID_label.grid(row=1, column=0)
        election_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        election_ID_entry.grid(row=1, column=1)

        election_name_label = Label(infoFrame, font=("", 15), text="Enter Election name", height=1)
        election_name_label.grid(row=2, column=0)
        election_name_entry = Entry(infoFrame, font=("", 15), width=18)
        election_name_entry.grid(row=2, column=1)

        election_date_label = Label(infoFrame, font=("", 15), text="Enter Election date", height=1)
        election_date_label.grid(row=3, column=0)
        election_date_entry = Entry(infoFrame, font=("", 15), width=18)
        election_date_entry.grid(row=3, column=1)

        election_state_label = Label(infoFrame, font=("", 15), text="Enter Election state", height=1)
        election_state_label.grid(row=4, column=0)
        election_state_entry = Entry(infoFrame, font=("", 15), width=18)
        election_state_entry.grid(row=4, column=1)

        SubmitFrame = Frame(update_window)
        SubmitFrame.place(x=0, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        update_window.grab_set()

    def election_delete_window():
        def submit_query():
            electionID = election_ID_entry.get()
            delete_dependent_rows(electionID)
            delete_query = "DELETE FROM Election WHERE ElectionID=%s"

            cursor.execute(delete_query, (electionID,))
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Deleted Successfully")

        def delete_dependent_rows(electionID):
            delete_query = "DELETE FROM candidate WHERE ElectionID=%s"
            cursor.execute(delete_query, (electionID,))
            connection.commit()

        delete_window = Toplevel(window)
        delete_window.title("Election Delete")
        delete_window.geometry("400x300")
        Label(delete_window, font=("", 15, "bold"), text="Delete Election").pack()

        InfoFrame = Frame(delete_window)
        InfoFrame.place(x=0, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Enter Info")
        infoFrame.grid(row=0, column=0)

        election_ID_label = Label(infoFrame, font=("", 15), text="Enter Election ID", height=1)
        election_ID_label.grid(row=1, column=0)
        election_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        election_ID_entry.grid(row=1, column=1)

        SubmitFrame = Frame(delete_window)
        SubmitFrame.place(x=0, y=150, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        delete_window.grab_set()
        
    # ==================== (Election) Set Operations: UNION ====================
    def setOpElec():
        def submit_query():
            insert_query = """
                            SELECT DISTINCT State FROM Election WHERE ElectionName = %s
                            UNION
                            SELECT DISTINCT State FROM Election WHERE ElectionName = %s;
                            """
            opElection_data = (opElection_X_entry.get(), opElection_Y_entry.get())
            cursor.execute(insert_query, opElection_data)
            rows = cursor.fetchall()
            if len(rows) != 0:
                opElection_table.delete(*opElection_table.get_children())
                for row in rows:
                    opElection_table.insert("", END, values=row)

        
        # ==================== Main setOp Election Window ====================
        opElection_window = Toplevel(window)
        opElection_window.title("(Election Table) Set Operations: UNION")
        opElection_window.geometry("900x500")
        Label(opElection_window, font=("", 20, "bold"), text="Set Operations Election Table (UNION)").pack()
        opElection_window.grab_set()
        
        # UNION text label
        #label1 = Label(opElection_window, font=("", 9), text="UNION of states involved in x and y elections")
        #label1.place(x=150, y=50)  # Positioning the label widget

        # Insert UNION info frame 
        InfoFrame = Frame(opElection_window)
        InfoFrame.place(x=175, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Insert info")
        infoFrame.grid(row=0, column=0)

        opElection_X_label = Label(infoFrame, font=("", 15), text="Enter ElectionName X: ", height=1)
        opElection_X_label.grid(row=1, column=0)
        opElection_X_entry = Entry(infoFrame, font=("", 15), width=18)
        opElection_X_entry.grid(row=1, column=1)

        opElection_Y_label = Label(infoFrame, font=("", 15), text="Enter ElectionName Y: ", height=1)
        opElection_Y_label.grid(row=2, column=0)
        opElection_Y_entry = Entry(infoFrame, font=("", 15), width=18)
        opElection_Y_entry.grid(row=2, column=1)

        # Query info
        label1 = Label(opElection_window, font=("", 9), text= """ Query Info: 
Finds UNION of states involved in X and Y elections""")
        label1.place(x=175, y=150)  # Positioning the label widget
        # Example input info
        label1 = Label(opElection_window, font=("", 9), text= """ Example input: 
X = Senate Election, Y = Governor Election""")
        label1.place(x=175, y=175)  # Positioning the label widget

        # Submit button
        SubmitFrame = Frame(opElection_window)
        SubmitFrame.place(x=175, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        # ==================== Table Result Info Frame ====================
        InfoFrame = Frame(opElection_window)
        InfoFrame.place(x=10, y=50, height=700, width=150)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Result")
        infoFrame.grid(row=0, column=0)

        scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
        opElection_table = ttk.Treeview(infoFrame, columns=("state"),
                                    yscrollcommand=scroll_y.set, height=18)

        opElection_table.column("#0", width=100)
        opElection_table.column("state", anchor=CENTER, width=100)

        opElection_table.heading("state", text="State")

        opElection_table["show"] = "headings"

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y = ttk.Scrollbar(command=opElection_table.yview)

        opElection_table.pack(fill=BOTH, expand=1)
    
    # ==================== (Election) Set Membership: IN ====================  
    def setMemElec():
        def submit_query():
            insert_query = """
                            SELECT ElectionID, ElectionName, Date, State
                            FROM Election
                            WHERE (Date, State) IN (
                            SELECT Date, State
                            FROM Election
                            WHERE ElectionName = %s AND State = %s
                            );
                            """
            memElection_data = (memElection_X_entry.get(), memElection_Y_entry.get())
            cursor.execute(insert_query, memElection_data)
            rows = cursor.fetchall()
            if len(rows) != 0:
                memElection_table.delete(*memElection_table.get_children())
                for row in rows:
                    memElection_table.insert("", END, values=row)

        
        # ==================== Main setMem Election Window ====================
        memElection_window = Toplevel(window)
        memElection_window.title("(Election Table) Set Membership: IN")
        memElection_window.geometry("900x500")
        Label(memElection_window, font=("", 20, "bold"), text="Set Membership Election Table (IN)").pack()
        memElection_window.grab_set()

        # Insert IN info frame 
        InfoFrame = Frame(memElection_window)
        InfoFrame.place(x=525, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Insert info")
        infoFrame.grid(row=0, column=0)

        memElection_X_label = Label(infoFrame, font=("", 15), text="Enter Election name X: ", height=1)
        memElection_X_label.grid(row=1, column=0)
        memElection_X_entry = Entry(infoFrame, font=("", 15), width=18)
        memElection_X_entry.grid(row=1, column=1)

        memElection_Y_label = Label(infoFrame, font=("", 15), text="Enter State Y: ", height=1)
        memElection_Y_label.grid(row=2, column=0)
        memElection_Y_entry = Entry(infoFrame, font=("", 15), width=18)
        memElection_Y_entry.grid(row=2, column=1)

        # Query info
        label1 = Label(memElection_window, font=("", 9), text= """ Query Info: 
Finds details on elections with election name X and state Y.""")
        label1.place(x=515, y=150)  # Positioning the label widget
        # Example input info
        label1 = Label(memElection_window, font=("", 9), text= """ Example input: 
X = Governor Election, Y = IL""")
        label1.place(x=635, y=175)  # Positioning the label widget

        # Submit button
        SubmitFrame = Frame(memElection_window)
        SubmitFrame.place(x=525, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        # ==================== Table Result Info Frame ====================
        InfoFrame = Frame(memElection_window)
        InfoFrame.place(x=10, y=50, height=700, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Result")
        infoFrame.grid(row=0, column=0)

        scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
        memElection_table = ttk.Treeview(infoFrame, columns=("electionID", "electionName", "date", "state"),
                                    yscrollcommand=scroll_y.set, height=18)

        memElection_table.column("#0", width=100)
        memElection_table.column("electionID", anchor=CENTER, width=100)
        memElection_table.column("electionName", anchor=W, width=200)
        memElection_table.column("date", anchor=CENTER, width=100)
        memElection_table.column("state", anchor=CENTER, width=60)

        memElection_table.heading("electionID", text="Election ID")
        memElection_table.heading("electionName", text="Election Name")
        memElection_table.heading("date", text="Date")
        memElection_table.heading("state", text="State")

        memElection_table["show"] = "headings"

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y = ttk.Scrollbar(command=memElection_table.yview)

        memElection_table.pack(fill=BOTH, expand=1)


    # ==================== (Election) Set Comparison: ANY ====================  
    def setCompElec():
        def submit_query():
            insert_query = """
                            SELECT ElectionID, ElectionName, Date, state
                            FROM Election
                            WHERE Date = ANY (SELECT Date FROM Election WHERE ElectionName = %s AND YEAR(Date) = %s);
                            """
            comElection_data = (comElection_X_entry.get(), comElection_Y_entry.get())
            cursor.execute(insert_query, comElection_data)
            rows = cursor.fetchall()
            if len(rows) != 0:
                comElection_table.delete(*comElection_table.get_children())
                for row in rows:
                    comElection_table.insert("", END, values=row)

        
        # ==================== Main setCom Election Window ====================
        comElection_window = Toplevel(window)
        comElection_window.title("(Election Table) Set Comparison: ANY")
        comElection_window.geometry("900x500")
        Label(comElection_window, font=("", 20, "bold"), text="Set Comparison Election Table (ANY)").pack()
        comElection_window.grab_set()

        # Insert ANY info frame 
        InfoFrame = Frame(comElection_window)
        InfoFrame.place(x=525, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Insert info")
        infoFrame.grid(row=0, column=0)

        comElection_X_label = Label(infoFrame, font=("", 15), text="Enter Election name X: ", height=1)
        comElection_X_label.grid(row=1, column=0)
        comElection_X_entry = Entry(infoFrame, font=("", 15), width=18)
        comElection_X_entry.grid(row=1, column=1)

        comElection_Y_label = Label(infoFrame, font=("", 15), text="Enter Year Y: ", height=1)
        comElection_Y_label.grid(row=2, column=0)
        comElection_Y_entry = Entry(infoFrame, font=("", 15), width=18)
        comElection_Y_entry.grid(row=2, column=1)

        # Query info
        label1 = Label(comElection_window, font=("", 9), text= """ Query Info: 
Finds elections held on the same date at any election name X in year Y.""")
        label1.place(x=550, y=150)  # Positioning the label widget
        # Example input info
        label1 = Label(comElection_window, font=("", 9), text= """ Example input: 
X = Governor Election, Y = 2023""")
        label1.place(x=635, y=175)  # Positioning the label widget

        # Submit button
        SubmitFrame = Frame(comElection_window)
        SubmitFrame.place(x=525, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        # ==================== Table Result Info Frame ====================
        InfoFrame = Frame(comElection_window)
        InfoFrame.place(x=10, y=50, height=700, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Result")
        infoFrame.grid(row=0, column=0)

        scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
        comElection_table = ttk.Treeview(infoFrame, columns=("electionID", "electionName", "date", "state"),
                                    yscrollcommand=scroll_y.set, height=18)

        comElection_table.column("#0", width=100)
        comElection_table.column("electionID", anchor=CENTER, width=100)
        comElection_table.column("electionName", anchor=W, width=200)
        comElection_table.column("date", anchor=CENTER, width=100)
        comElection_table.column("state", anchor=CENTER, width=60)

        comElection_table.heading("electionID", text="Election ID")
        comElection_table.heading("electionName", text="Election Name")
        comElection_table.heading("date", text="Date")
        comElection_table.heading("state", text="State")

        comElection_table["show"] = "headings"

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y = ttk.Scrollbar(command=comElection_table.yview)

        comElection_table.pack(fill=BOTH, expand=1)

    # ==================== (Election) Calculate the Cumulative Elections ====================  
    def calcCumElec():
        def fetch_data():
            insert_query = """
                            SELECT State, Date,
                            COUNT(*) OVER (PARTITION BY State ORDER BY Date) AS CumulativeElections
                            FROM Election
                            ORDER BY State, Date;
                            """
            cursor.execute(insert_query)
            rows = cursor.fetchall()
            if len(rows) != 0:
                calcCumElection_table.delete(*calcCumElection_table.get_children())
                for row in rows:
                    calcCumElection_table.insert("", END, values=row)

        
        # ==================== Main calCum Election Window ====================
        calcCumElection_window = Toplevel(window)
        calcCumElection_window.title("(Election Table) Advanced Aggregate Functions: WINDOW Functions")
        calcCumElection_window.geometry("900x500")
        Label(calcCumElection_window, font=("", 20, "bold"), text="Calculate Cumulative Election Table (COUNT)").pack()
        calcCumElection_window.grab_set()

        # ==================== Table Result Info Frame ====================
        InfoFrame = Frame(calcCumElection_window)
        InfoFrame.place(x=300, y=50, height=700, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Result")
        infoFrame.grid(row=0, column=0)

        # Query info
        label1 = Label(calcCumElection_window, font=("", 9), text= """ Query Info: 
Calculates running total of elections by state over time.""")
        label1.place(x=550, y=150)  # Positioning the label widget

        scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
        calcCumElection_table = ttk.Treeview(infoFrame, columns=("state", "date", "CumulativeElections"),
                                    yscrollcommand=scroll_y.set, height=18)

        calcCumElection_table.column("#0", width=100)
        calcCumElection_table.column("state", anchor=CENTER, width=60)
        calcCumElection_table.column("date", anchor=CENTER, width=100)
        calcCumElection_table.column("CumulativeElections", anchor=CENTER, width=60)


        calcCumElection_table.heading("state", text="State")
        calcCumElection_table.heading("date", text="Date")
        calcCumElection_table.heading("CumulativeElections", text="Cumulative Elections")
        

        calcCumElection_table["show"] = "headings"

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y = ttk.Scrollbar(command=calcCumElection_table.yview)

        calcCumElection_table.pack(fill=BOTH, expand=1)
        fetch_data()
    
    # ==================== (Election) Subqueries using the WITH Clause ====================  
    def withClauseElec():
        def submit_query():
            insert_query = """
                            WITH RecentElections AS (
                            SELECT * FROM Election WHERE Date >= %s
                            )
                            SELECT * FROM RecentElections WHERE State = %s;
                            """
            withClauseElection_data = (withClauseElection_X_entry.get(), withClauseElection_Y_entry.get())
            cursor.execute(insert_query, withClauseElection_data)
            rows = cursor.fetchall()
            if len(rows) != 0:
                withClauseElection_table.delete(*withClauseElection_table.get_children())
                for row in rows:
                    withClauseElection_table.insert("", END, values=row)

        
        # ==================== Main withClause Election Window ====================
        withClauseElection_window = Toplevel(window)
        withClauseElection_window.title("(Election Table) Subqueries using the WITH Clause")
        withClauseElection_window.geometry("900x500")
        Label(withClauseElection_window, font=("", 20, "bold"), text="Subqueries using the WITH Clause").pack()
        withClauseElection_window.grab_set()

        # Insert ANY info frame 
        InfoFrame = Frame(withClauseElection_window)
        InfoFrame.place(x=525, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 10, "bold"), text="Insert Info")
        infoFrame.grid(row=0, column=0)

        withClauseElection_X_label = Label(infoFrame, font=("", 15), text="Enter Date X: ", height=1)
        withClauseElection_X_label.grid(row=1, column=0)
        withClauseElection_X_entry = Entry(infoFrame, font=("", 15), width=18)
        withClauseElection_X_entry.grid(row=1, column=1)

        withClauseElection_Y_label = Label(infoFrame, font=("", 15), text="Enter State Y: ", height=1)
        withClauseElection_Y_label.grid(row=2, column=0)
        withClauseElection_Y_entry = Entry(infoFrame, font=("", 15), width=18)
        withClauseElection_Y_entry.grid(row=2, column=1)

        # Query info
        label1 = Label(withClauseElection_window, font=("", 9), text= """ Query Info: 
This query uses a Common Table Expression (CTE) named RecentElections 
to temporarily hold data of elections that occurred from 2022 onwards. 
It then selects all such recent elections in California, allowing 
focused analysis on recent state-specific elections. """)
        label1.place(x=525, y=150)  # Positioning the label widget

        # Example input info
        label1 = Label(withClauseElection_window, font=("", 9), text= """ Example input: 
X = 2022-01-01, Y = CA""")
        label1.place(x=635, y=215)  # Positioning the label widget

        # Submit button
        SubmitFrame = Frame(withClauseElection_window)
        SubmitFrame.place(x=525, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        # ==================== Table Result Info Frame ====================
        InfoFrame = Frame(withClauseElection_window)
        InfoFrame.place(x=10, y=50, height=700, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Result")
        infoFrame.grid(row=0, column=0)

        scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
        withClauseElection_table = ttk.Treeview(infoFrame, columns=("electionID", "electionName", "date", "state"),
                                    yscrollcommand=scroll_y.set, height=18)

        withClauseElection_table.column("#0", width=100)
        withClauseElection_table.column("electionID", anchor=CENTER, width=100)
        withClauseElection_table.column("electionName", anchor=W, width=200)
        withClauseElection_table.column("date", anchor=CENTER, width=100)
        withClauseElection_table.column("state", anchor=CENTER, width=60)

        withClauseElection_table.heading("electionID", text="Election ID")
        withClauseElection_table.heading("electionName", text="Election Name")
        withClauseElection_table.heading("date", text="Date")
        withClauseElection_table.heading("state", text="State")

        withClauseElection_table["show"] = "headings"

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y = ttk.Scrollbar(command=withClauseElection_table.yview)

        withClauseElection_table.pack(fill=BOTH, expand=1)

    
    # ==================== Main Election Table Window ====================
    election_window = Toplevel(window)
    election_window.title("Election Table")
    election_window.geometry("900x500")
    Label(election_window, font=("", 20, "bold"), text="Election").pack()
    election_window.grab_set()


    # ==================== Actions Frame ====================
    ActionFrame = Frame(election_window)
    ActionFrame.place(x=550, y=50, height=300, width=285)
    actionFrame = LabelFrame(ActionFrame, font=("", 15, "bold"), text="Select an action")
    actionFrame.grid(row=0, column=0)

    insert_button = Button(actionFrame, text="Insert Data", font=("", 15), width=10, height=1
                           ,command=election_insert_window)
    insert_button.grid(row=1, column=0)

    update_button = Button(actionFrame, text="Update Data", font=("", 15), width=10, height=1,
                           command=election_update_window)
    update_button.grid(row=2, column=0)

    delete_button = Button(actionFrame, text="Delete Data", font=("", 15), width=10, height=1,
                           command=election_delete_window)
    delete_button.grid(row=3, column=0)

    setOP_button = Button(actionFrame, text="Set Operations", font=("", 15), width=10, height=1,
                           command= setOpElec)
    setOP_button.grid(row=4, column=0)

    setMem_button = Button(actionFrame, text="Set Membership", font=("", 15), width=10, height=1,
                           command= setMemElec)
    setMem_button.grid(row=5, column=0)

    setCom_button = Button(actionFrame, text="Set Comparison", font=("", 15), width=10, height=1,
                           command= setCompElec)
    setCom_button.grid(row=6, column=0)

    calCum_button = Button(actionFrame, text="Calculate Cumulative", font=("", 15), width=15, height=1,
                           command= calcCumElec)
    calCum_button.grid(row=7, column=0)

    withClause_button = Button(actionFrame, text="Subqueries using the WITH Clause", font=("", 15), width=23, height=1,
                           command= withClauseElec)
    withClause_button.grid(row=8, column=0)


    # ==================== Table Info Frame ====================
    InfoFrame = Frame(election_window)
    InfoFrame.place(x=10, y=50, height=700, width=500)
    infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Election Info")
    infoFrame.grid(row=0, column=0)


    scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
    election_table = ttk.Treeview(infoFrame, columns=("electionID", "electionName", "date", "state"),
                                  yscrollcommand=scroll_y.set, height=18)

    election_table.column("#0", width=100)
    election_table.column("electionID", anchor=CENTER, width=100)
    election_table.column("electionName", anchor=W, width=200)
    election_table.column("date", anchor=CENTER, width=100)
    election_table.column("state", anchor=CENTER, width=60)


    election_table.heading("electionID", text="Election ID")
    election_table.heading("electionName", text="Election Name")
    election_table.heading("date", text="Date")
    election_table.heading("state", text="State")

    election_table["show"] = "headings"

    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_y = ttk.Scrollbar(command=election_table.yview)

    election_table.pack(fill=BOTH, expand=1)

    fetch_data()


# ==================== Committee Window ====================
def open_committee_window():
    # function to show everything in the table
    def fetch_data():
        cursor.execute("SELECT * FROM committee")
        rows = cursor.fetchall()
        if len(rows) != 0 :
            committee_table.delete(*committee_table.get_children())
            for row in rows:
                committee_table.insert("", END, values=row)
            connection.commit()

    #function to highlight a row that you click on
    def get_cursor():
        cursor_row = committee_table.focus()

    # ==================== Button Windows ====================
    def committee_insert_window():
        def submit_query():
            insert_query = "INSERT INTO Committee (CommitteeID, CommitteeName, Treasurer, CommitteeType, State) VALUES (%s, %s, %s, %s, %s)"
            committee_data = (committee_ID_entry.get(), committee_name_entry.get(),
                              treasurer_entry.get(), committee_type_entry.get(), state_entry.get())
            cursor.execute(insert_query, committee_data)
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Inserted Successfully")

        insert_window = Toplevel(window)
        insert_window.title("Committee Insert")
        insert_window.geometry("500x400")
        Label(insert_window, font=("", 15, "bold"), text="Insert Committee").pack()

        InfoFrame = Frame(insert_window)
        InfoFrame.place(x=0, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Enter Info")
        infoFrame.grid(row=0, column=0)

        committee_ID_label = Label(infoFrame, font=("", 15), text="Enter Committee ID", height=1)
        committee_ID_label.grid(row=1, column=0)
        committee_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        committee_ID_entry.grid(row=1, column=1)

        committee_name_label = Label(infoFrame, font=("", 15), text="Enter Committee name", height=1)
        committee_name_label.grid(row=2, column=0)
        committee_name_entry = Entry(infoFrame, font=("", 15), width=18)
        committee_name_entry.grid(row=2, column=1)

        treasurer_label = Label(infoFrame, font=("", 15), text="Enter Treasurer", height=1)
        treasurer_label.grid(row=3, column=0)
        treasurer_entry = Entry(infoFrame, font=("", 15), width=18)
        treasurer_entry.grid(row=3, column=1)

        committee_type_label = Label(infoFrame, font=("", 15), text="Enter Committee type", height=1)
        committee_type_label.grid(row=4, column=0)
        committee_type_entry = Entry(infoFrame, font=("", 15), width=18)
        committee_type_entry.grid(row=4, column=1)

        state_label = Label(infoFrame, font=("", 15), text="Enter State", height=1)
        state_label.grid(row=5, column=0)
        state_entry = Entry(infoFrame, font=("", 15), width=18)
        state_entry.grid(row=5, column=1)

        SubmitFrame = Frame(insert_window)
        SubmitFrame.place(x=0, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        insert_window.grab_set()

    def committee_update_window():
        def submit_query():
            update_query = """
            UPDATE Committee
            SET CommitteeName = %s, 
                Treasurer = %s, 
                CommitteeType = %s,
                State = %s
            WHERE CommitteeID = %s;
            """
            cursor.execute(update_query, (committee_name_entry.get(), treasurer_entry.get(),
                                          committee_type_entry.get(), state_entry.get(), committee_ID_entry.get()))
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Updated Successfully")

        update_window = Toplevel(window)
        update_window.title("Committee Update")
        update_window.geometry("500x400")
        Label(update_window, font=("", 15, "bold"), text="Update Committee").pack()

        InfoFrame = Frame(update_window)
        InfoFrame.place(x=0, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Enter Info")
        infoFrame.grid(row=0, column=0)

        committee_ID_label = Label(infoFrame, font=("", 15), text="Enter Committee ID", height=1)
        committee_ID_label.grid(row=1, column=0)
        committee_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        committee_ID_entry.grid(row=1, column=1)

        committee_name_label = Label(infoFrame, font=("", 15), text="Enter Committee name", height=1)
        committee_name_label.grid(row=2, column=0)
        committee_name_entry = Entry(infoFrame, font=("", 15), width=18)
        committee_name_entry.grid(row=2, column=1)

        treasurer_label = Label(infoFrame, font=("", 15), text="Enter Treasurer", height=1)
        treasurer_label.grid(row=3, column=0)
        treasurer_entry = Entry(infoFrame, font=("", 15), width=18)
        treasurer_entry.grid(row=3, column=1)

        committee_type_label = Label(infoFrame, font=("", 15), text="Enter Committee type", height=1)
        committee_type_label.grid(row=4, column=0)
        committee_type_entry = Entry(infoFrame, font=("", 15), width=18)
        committee_type_entry.grid(row=4, column=1)

        state_label = Label(infoFrame, font=("", 15), text="Enter State", height=1)
        state_label.grid(row=5, column=0)
        state_entry = Entry(infoFrame, font=("", 15), width=18)
        state_entry.grid(row=5, column=1)

        SubmitFrame = Frame(update_window)
        SubmitFrame.place(x=0, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        update_window.grab_set()

    def committee_delete_window():
        def submit_query():
            committeeID = committee_ID_entry.get()
            delete_query = "DELETE FROM Committee WHERE CommitteeID = %s;"

            cursor.execute(delete_query, (committeeID,))
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Deleted Successfully")

        delete_window = Toplevel(window)
        delete_window.title("Committee Delete")
        delete_window.geometry("400x300")
        Label(delete_window, font=("", 15, "bold"), text="Delete Committee").pack()

        InfoFrame = Frame(delete_window)
        InfoFrame.place(x=0, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Enter Info")
        infoFrame.grid(row=0, column=0)

        committee_ID_label = Label(infoFrame, font=("", 15), text="Enter Committee ID", height=1)
        committee_ID_label.grid(row=1, column=0)
        committee_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        committee_ID_entry.grid(row=1, column=1)

        SubmitFrame = Frame(delete_window)
        SubmitFrame.place(x=0, y=150, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        delete_window.grab_set()

        # ==================== (Election) Set Operations: UNION ====================
    def setOpCom():
        def submit_query():
            insert_query = """
                            SELECT DISTINCT CommitteeName FROM Committee WHERE State = %s
                            UNION
                            SELECT DISTINCT CommitteeName FROM Committee WHERE State = %s;
                            """
            opElection_data = (opElection_X_entry.get(), opElection_Y_entry.get())
            cursor.execute(insert_query, opElection_data)
            rows = cursor.fetchall()
            if len(rows) != 0:
                opElection_table.delete(*opElection_table.get_children())
                for row in rows:
                    opElection_table.insert("", END, values=row)

        
        # ==================== Main setOp Committee Window ====================
        opElection_window = Toplevel(window)
        opElection_window.title("(Committee Table) Set Operations: UNION")
        opElection_window.geometry("900x500")
        Label(opElection_window, font=("", 20, "bold"), text="Set Operations CommitteeTable (UNION)").pack()
        opElection_window.grab_set()
        
        # UNION text label
        #label1 = Label(opElection_window, font=("", 9), text="UNION of states involved in x and y elections")
        #label1.place(x=150, y=50)  # Positioning the label widget

        # Insert UNION info frame 
        InfoFrame = Frame(opElection_window)
        InfoFrame.place(x=200, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Insert info")
        infoFrame.grid(row=0, column=0)

        opElection_X_label = Label(infoFrame, font=("", 15), text="Enter State X: ", height=1)
        opElection_X_label.grid(row=1, column=0)
        opElection_X_entry = Entry(infoFrame, font=("", 15), width=18)
        opElection_X_entry.grid(row=1, column=1)

        opElection_Y_label = Label(infoFrame, font=("", 15), text="Enter State Y: ", height=1)
        opElection_Y_label.grid(row=2, column=0)
        opElection_Y_entry = Entry(infoFrame, font=("", 15), width=18)
        opElection_Y_entry.grid(row=2, column=1)

        # Query info
        label1 = Label(opElection_window, font=("", 9), text= """ Query Info: 
Finds UNION of Committee's involved in X and Y states.""")
        label1.place(x=200, y=150)  # Positioning the label widget
        # Example input info
        label1 = Label(opElection_window, font=("", 9), text= """ Example input: 
X = NY, Y = IL""")
        label1.place(x=200, y=175)  # Positioning the label widget

        # Submit button
        SubmitFrame = Frame(opElection_window)
        SubmitFrame.place(x=200, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        # ==================== Table Result Info Frame ====================
        InfoFrame = Frame(opElection_window)
        InfoFrame.place(x=10, y=50, height=700, width=175)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Result")
        infoFrame.grid(row=0, column=0)

        scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
        opElection_table = ttk.Treeview(infoFrame, columns=("state"),
                                    yscrollcommand=scroll_y.set, height=18)

        opElection_table.column("#0", width=150)
        opElection_table.column("state", anchor=CENTER, width=150)

        opElection_table.heading("state", text="State")

        opElection_table["show"] = "headings"

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y = ttk.Scrollbar(command=opElection_table.yview)

        opElection_table.pack(fill=BOTH, expand=1)
    
    # ==================== (Committee) Set Comparison: EXISTS ====================  
    def setCompCom():
        def submit_query():
            insert_query = """
                            SELECT CASE 
                                WHEN EXISTS (
                                    SELECT 1
                                    FROM Committee
                                    WHERE CommitteeType = 'Campaign'
                                    AND CommitteeName LIKE '%' %s
                                    AND State = %s
                                ) THEN 'Exists'
                                ELSE NULL
                            END AS Result;
                            """
            memElection_data = (memElection_X_entry.get(), memElection_Y_entry.get())
            cursor.execute(insert_query, memElection_data)
            rows = cursor.fetchall()
            if len(rows) != 0:
                memElection_table.delete(*memElection_table.get_children())
                for row in rows:
                    memElection_table.insert("", END, values=row)

        
        # ==================== Main setMem Committee Window ====================
        memElection_window = Toplevel(window)
        memElection_window.title("(Committee Table) Set Comparison: EXISTS")
        memElection_window.geometry("900x500")
        Label(memElection_window, font=("", 20, "bold"), text="Set Comparison Committee Table (Exists)").pack()
        memElection_window.grab_set()

        # Insert info frame 
        InfoFrame = Frame(memElection_window)
        InfoFrame.place(x=250, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Insert info")
        infoFrame.grid(row=0, column=0)

        memElection_X_label = Label(infoFrame, font=("", 15), text="Enter Committee name X: ", height=1)
        memElection_X_label.grid(row=1, column=0)
        memElection_X_entry = Entry(infoFrame, font=("", 15), width=18)
        memElection_X_entry.grid(row=1, column=1)

        memElection_Y_label = Label(infoFrame, font=("", 15), text="Enter State Y: ", height=1)
        memElection_Y_label.grid(row=2, column=0)
        memElection_Y_entry = Entry(infoFrame, font=("", 15), width=18)
        memElection_Y_entry.grid(row=2, column=1)

        # Query info
        label1 = Label(memElection_window, font=("", 9), text= """ Query Info: 
Checks if there are any committees X in State Y and returns NULL if none exist""")
        label1.place(x=250, y=150)  # Positioning the label widget
        # Example input info
        label1 = Label(memElection_window, font=("", 9), text= """ Example input: 
X = Governor, Y = IL""")
        label1.place(x=380, y=175)  # Positioning the label widget

        # Submit button
        SubmitFrame = Frame(memElection_window)
        SubmitFrame.place(x=250, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        # ==================== Table Result Info Frame ====================
        InfoFrame = Frame(memElection_window)
        InfoFrame.place(x=10, y=50, height=700, width=175)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Result")
        infoFrame.grid(row=0, column=0)

        scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
        memElection_table = ttk.Treeview(infoFrame, columns=("Result"),
                                    yscrollcommand=scroll_y.set, height=18)

        memElection_table.column("#0", width=100)
        memElection_table.column("Result", anchor=CENTER, width=100)


        memElection_table.heading("Result", text="Result")


        memElection_table["show"] = "headings"

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y = ttk.Scrollbar(command=memElection_table.yview)

        memElection_table.pack(fill=BOTH, expand=1)


    # ==================== (Committee) Set Membership: IN ====================  
    def setMemCom():
        def submit_query():
            insert_query = """
                            SELECT CommitteeID, CommitteeName, Treasurer, CommitteeType, State
                            FROM Committee
                            WHERE (CommitteeType, State) IN (
                                SELECT CommitteeType, State
                                FROM Committee
                                WHERE CommitteeName LIKE '%' %s
                                AND State = %s
                            );
                            """
            comElection_data = (comElection_X_entry.get(), comElection_Y_entry.get())
            cursor.execute(insert_query, comElection_data)
            rows = cursor.fetchall()
            if len(rows) != 0:
                comElection_table.delete(*comElection_table.get_children())
                for row in rows:
                    comElection_table.insert("", END, values=row)

        
        # ==================== Main setMem Election Window ====================
        comElection_window = Toplevel(window)
        comElection_window.title("(Committee Table) Set Membership: IN")
        comElection_window.geometry("1100x500")
        Label(comElection_window, font=("", 20, "bold"), text="Set Membership Committee Table (IN)").pack()
        comElection_window.grab_set()

        # Insert info frame 
        InfoFrame = Frame(comElection_window)
        InfoFrame.place(x=650, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Insert info")
        infoFrame.grid(row=0, column=0)

        comElection_X_label = Label(infoFrame, font=("", 15), text="Enter Committee name X: ", height=1)
        comElection_X_label.grid(row=1, column=0)
        comElection_X_entry = Entry(infoFrame, font=("", 15), width=18)
        comElection_X_entry.grid(row=1, column=1)

        comElection_Y_label = Label(infoFrame, font=("", 15), text="Enter State Y: ", height=1)
        comElection_Y_label.grid(row=2, column=0)
        comElection_Y_entry = Entry(infoFrame, font=("", 15), width=18)
        comElection_Y_entry.grid(row=2, column=1)

        # Query info
        label1 = Label(comElection_window, font=("", 9), text= """ Query Info: 
Select all committee details that match the type and state of any committee X in State Y.""")
        label1.place(x=650, y=150)  # Positioning the label widget
        # Example input info
        label1 = Label(comElection_window, font=("", 9), text= """ Example input: 
X = Senate, Y = NY""")
        label1.place(x=815, y=175)  # Positioning the label widget

        # Submit button
        SubmitFrame = Frame(comElection_window)
        SubmitFrame.place(x=650, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        # ==================== Table Result Info Frame ====================
        InfoFrame = Frame(comElection_window)
        InfoFrame.place(x=10, y=50, height=700, width=600)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Result")
        infoFrame.grid(row=0, column=0)

        scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
        comElection_table = ttk.Treeview(infoFrame, columns=("CommitteeID", "CommitteeName", "Treasurer", "CommitteeType", "state"),
                                    yscrollcommand=scroll_y.set, height=18)

        comElection_table.column("#0", width=100)
        comElection_table.column("CommitteeID", anchor=CENTER, width=100)
        comElection_table.column("CommitteeName", anchor=W, width=200)
        comElection_table.column("Treasurer", anchor=CENTER, width=100)
        comElection_table.column("CommitteeType", anchor=CENTER, width=100)
        comElection_table.column("state", anchor=CENTER, width=60)

        comElection_table.heading("CommitteeID", text="Committee ID")
        comElection_table.heading("CommitteeName", text="Committee Name")
        comElection_table.heading("Treasurer", text="Treasurer")
        comElection_table.heading("CommitteeType", text="Committee Type")
        comElection_table.heading("state", text="state")

        comElection_table["show"] = "headings"

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y = ttk.Scrollbar(command=comElection_table.yview)

        comElection_table.pack(fill=BOTH, expand=1)

    # ==================== (Committee) Calculate the Cumulative Committees ====================  
    def calcCumCom():
        def fetch_data():
            insert_query = """
                            SELECT CommitteeID, CommitteeName, State,
                            COUNT(*) OVER (PARTITION BY State ORDER BY CommitteeID) AS RunningTotalCommittees
                            FROM Committee
                            ORDER BY CommitteeID;
                            """
            cursor.execute(insert_query)
            rows = cursor.fetchall()
            if len(rows) != 0:
                calcCumElection_table.delete(*calcCumElection_table.get_children())
                for row in rows:
                    calcCumElection_table.insert("", END, values=row)

        
        # ==================== Main calCum Committee Window ====================
        calcCumElection_window = Toplevel(window)
        calcCumElection_window.title("(Committee Table) Advanced Aggregate Functions: WINDOW Functions")
        calcCumElection_window.geometry("900x500")
        Label(calcCumElection_window, font=("", 20, "bold"), text="Calculate Cumulative Committee Table (COUNT)").pack()
        calcCumElection_window.grab_set()

        # ==================== Table Result Info Frame ====================
        InfoFrame = Frame(calcCumElection_window)
        InfoFrame.place(x=200, y=50, height=700, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Result")
        infoFrame.grid(row=0, column=0)

        # Query info
        label1 = Label(calcCumElection_window, font=("", 9), text= """ Query Info: 
Calculates running total of Committees by state, ordered by CommitteeID.""")
        label1.place(x=280, y=450)  # Positioning the label widget

        scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
        calcCumElection_table = ttk.Treeview(infoFrame, columns=("CommitteeID", "CommitteeName", "state", "CumulativeCommittees"),
                                    yscrollcommand=scroll_y.set, height=18)

        calcCumElection_table.column("#0", width=100)
        calcCumElection_table.column("CommitteeID", anchor=CENTER, width=100)
        calcCumElection_table.column("CommitteeName", anchor=W, width=150)
        calcCumElection_table.column("state", anchor=CENTER, width=60)
        calcCumElection_table.column("CumulativeCommittees", anchor=CENTER, width=150)

        calcCumElection_table.heading("CommitteeID", text="Committee ID")
        calcCumElection_table.heading("CommitteeName", text="Committee Name")
        calcCumElection_table.heading("state", text="State")
        calcCumElection_table.heading("CumulativeCommittees", text="Cumulative Committees")
        

        calcCumElection_table["show"] = "headings"

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y = ttk.Scrollbar(command=calcCumElection_table.yview)

        calcCumElection_table.pack(fill=BOTH, expand=1)
        fetch_data()
    
    # ==================== (Committee) Subqueries using the WITH Clause ====================  
    def withClauseCom():
        def submit_query():
            insert_query = """
                            WITH CampaignCommittees AS (
                                SELECT *
                                FROM Committee
                                WHERE CommitteeType = 'Campaign'
                            )
                            SELECT CommitteeID, CommitteeName, Treasurer, CommitteeType, State
                            FROM CampaignCommittees
                            WHERE State = %s;
                            """
            withClauseElection_data = (withClauseElection_X_entry.get(),)
            cursor.execute(insert_query, withClauseElection_data)
            rows = cursor.fetchall()
            if len(rows) != 0:
                withClauseElection_table.delete(*withClauseElection_table.get_children())
                for row in rows:
                    withClauseElection_table.insert("", END, values=row)

        
        # ==================== Main withClause Committee Window ====================
        withClauseElection_window = Toplevel(window)
        withClauseElection_window.title("(Committee Table) Subqueries using the WITH Clause")
        withClauseElection_window.geometry("1000x500")
        Label(withClauseElection_window, font=("", 20, "bold"), text="Subqueries using the WITH Clause").pack()
        withClauseElection_window.grab_set()

        # Insert info frame 
        InfoFrame = Frame(withClauseElection_window)
        InfoFrame.place(x=625, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 10, "bold"), text="Insert Info")
        infoFrame.grid(row=0, column=0)

        withClauseElection_X_label = Label(infoFrame, font=("", 15), text="Enter State Type X: ", height=1)
        withClauseElection_X_label.grid(row=1, column=0)
        withClauseElection_X_entry = Entry(infoFrame, font=("", 15), width=18)
        withClauseElection_X_entry.grid(row=1, column=1)


        # Query info
        label1 = Label(withClauseElection_window, font=("", 9), text= """ Query Info: 
                        This query uses the CTE CampaignCommittees to temporarily hold
                        all committees of the 'Campaign' type. 
                        It then selects committees from the CTE that are based in state Y.
                        Example input: X = NY""")
        label1.place(x=575, y=150)  # Positioning the label widget


        # Submit button
        SubmitFrame = Frame(withClauseElection_window)
        SubmitFrame.place(x=650, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        # ==================== Table Result Info Frame ====================
        InfoFrame = Frame(withClauseElection_window)
        InfoFrame.place(x=10, y=50, height=700, width=600)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Result")
        infoFrame.grid(row=0, column=0)

        scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
        withClauseElection_table = ttk.Treeview(infoFrame, columns=("CommitteeID", "CommitteeName", "Treasurer", "CommitteeType","state"),
                                    yscrollcommand=scroll_y.set, height=18)

        withClauseElection_table.column("#0", width=100)
        withClauseElection_table.column("CommitteeID", anchor=CENTER, width=100)
        withClauseElection_table.column("CommitteeName", anchor=W, width=200)
        withClauseElection_table.column("Treasurer", anchor=CENTER, width=100)
        withClauseElection_table.column("CommitteeType", anchor=CENTER, width=100)
        withClauseElection_table.column("state", anchor=CENTER, width=60)

        withClauseElection_table.heading("CommitteeID", text="Committee ID")
        withClauseElection_table.heading("CommitteeName", text="Committee Name")
        withClauseElection_table.heading("Treasurer", text="Treasurer")
        withClauseElection_table.heading("CommitteeType", text="Committee Type")
        withClauseElection_table.heading("state", text="State")

        withClauseElection_table["show"] = "headings"

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y = ttk.Scrollbar(command=withClauseElection_table.yview)

        withClauseElection_table.pack(fill=BOTH, expand=1)


    # ==================== Main Committee Window ====================
    committee_window = Toplevel(window)
    committee_window.title("Committee Table")
    committee_window.geometry("1000x500")
    Label(committee_window, font=("", 20, "bold"), text="Committee").pack()
    committee_window.grab_set()


    # ==================== Actions Frame ====================
    ActionFrame = Frame(committee_window)
    ActionFrame.place(x=700, y=50, height=500, width=500)
    actionFrame = LabelFrame(ActionFrame, font=("", 15, "bold"), text="Select an action")
    actionFrame.grid(row=0, column=0)

    insert_button = Button(actionFrame, text="Insert Data", font=("", 15), width=10, height=1,
                           command=committee_insert_window)
    insert_button.grid(row=1, column=0)

    update_button = Button(actionFrame, text="Update Data", font=("", 15), width=10, height=1,
                           command=committee_update_window)
    update_button.grid(row=2, column=0)

    delete_button = Button(actionFrame, text="Delete Data", font=("", 15), width=10, height=1,
                           command=committee_delete_window)
    delete_button.grid(row=3, column=0)

    setOP_button = Button(actionFrame, text="Set Operations", font=("", 15), width=10, height=1,
                           command= setOpCom)
    setOP_button.grid(row=4, column=0)

    setMem_button = Button(actionFrame, text="Set Membership", font=("", 15), width=10, height=1,
                           command= setMemCom)
    setMem_button.grid(row=5, column=0)

    setCom_button = Button(actionFrame, text="Set Comparison", font=("", 15), width=10, height=1,
                           command= setCompCom)
    setCom_button.grid(row=6, column=0)

    calCum_button = Button(actionFrame, text="Calculate Cumulative", font=("", 15), width=15, height=1,
                           command= calcCumCom)
    calCum_button.grid(row=7, column=0)

    withClause_button = Button(actionFrame, text="Subqueries using the WITH Clause", font=("", 15), width=23, height=1,
                           command= withClauseCom)
    withClause_button.grid(row=8, column=0)


    # ==================== Table Info Frame ====================
    InfoFrame = Frame(committee_window)
    InfoFrame.place(x=10, y=50, height=700, width=600)
    infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Committee Info")
    infoFrame.grid(row=0, column=0)

    scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
    committee_table = ttk.Treeview(infoFrame, columns=("committeeID", "committeeName", "treasurer", "committeeType", "state"),
                                   yscrollcommand=scroll_y.set, height=18)

    committee_table.column("#0", width=100)
    committee_table.column("committeeID", anchor=CENTER, width=100)
    committee_table.column("committeeName", anchor=W, width=200)
    committee_table.column("treasurer", anchor=W, width=100)
    committee_table.column("committeeType", anchor=W, width=100)
    committee_table.column("state", anchor=CENTER, width=60)

    committee_table.heading("committeeID", text="Committee ID")
    committee_table.heading("committeeName", text="Committee Name")
    committee_table.heading("treasurer", text="Treasurer")
    committee_table.heading("committeeType", text="Committee Type")
    committee_table.heading("state", text="State")

    committee_table["show"] = "headings"

    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_y = ttk.Scrollbar(command=committee_table.yview)

    committee_table.pack(fill=BOTH, expand=1)

    fetch_data()


# ==================== Candidate Window ====================
def open_candidate_window():
    #function to show everything in the table
    def fetch_data():
        cursor.execute("SELECT * FROM candidate")
        rows = cursor.fetchall()
        if len(rows) != 0:
            candidate_table.delete(*candidate_table.get_children())
            for row in rows:
                candidate_table.insert("", END, values=row)
            connection.commit()

    #function to highlight a row that you click in
    def get_cursor():
        cursor_row = candidate_table.focus()

    # ==================== Button Windows ====================
    def candidate_insert_window():
        def submit_query():
            insert_query = "INSERT INTO Candidate (CandidateID, CandidateName, PartyAffiliation, Office, State, CommitteeID, ElectionID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            candidate_data = (candidate_ID_entry.get(), candidate_name_entry.get(), party_affiliation_entry.get(),
                              office_entry.get(), state_entry.get(), committee_ID_entry.get(), election_ID_entry.get())
            cursor.execute(insert_query, candidate_data)
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Inserted Successfully")

        insert_window = Toplevel(window)
        insert_window.title("Candidate Insert")
        insert_window.geometry("500x400")
        Label(insert_window, font=("", 20, "bold"), text="Insert Candidate").pack()

        InfoFrame = Frame(insert_window)
        InfoFrame.place(x=0, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Enter Info")
        infoFrame.grid(row=0, column=0)

        candidate_ID_label = Label(infoFrame, font=("", 15), text="Enter Candidate ID", height=1)
        candidate_ID_label.grid(row=1, column=0)
        candidate_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        candidate_ID_entry.grid(row=1, column=1)

        candidate_name_label = Label(infoFrame, font=("", 15), text="Enter Candidate Name", height=1)
        candidate_name_label.grid(row=2, column=0)
        candidate_name_entry = Entry(infoFrame, font=("", 15), width=18)
        candidate_name_entry.grid(row=2, column=1)

        party_affiliation_label = Label(infoFrame, font=("", 15), text="Enter Party Affiliation", height=1)
        party_affiliation_label.grid(row=3, column=0)
        party_affiliation_entry = Entry(infoFrame, font=("", 15), width=18)
        party_affiliation_entry.grid(row=3, column=1)

        office_label = Label(infoFrame, font=("", 15), text="Enter Office", height=1)
        office_label.grid(row=4, column=0)
        office_entry = Entry(infoFrame, font=("", 15), width=18)
        office_entry.grid(row=4, column=1)

        state_label = Label(infoFrame, font=("", 15), text="Enter State", height=1)
        state_label.grid(row=5, column=0)
        state_entry = Entry(infoFrame, font=("", 15), width=18)
        state_entry.grid(row=5, column=1)

        committee_ID_label = Label(infoFrame, font=("", 15), text="Enter Committee ID", height=1)
        committee_ID_label.grid(row=6, column=0)
        committee_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        committee_ID_entry.grid(row=6, column=1)

        election_ID_label = Label(infoFrame, font=("", 15), text="Enter Election ID", height=1)
        election_ID_label.grid(row=7, column=0)
        election_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        election_ID_entry.grid(row=7, column=1)

        SubmitFrame = Frame(insert_window)
        SubmitFrame.place(x=0, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        insert_window.grab_set()

    def candidate_update_window():
        def submit_query():
            update_query = """
            UPDATE Candidate
            SET CandidateName = %s, 
                PartyAffiliation = %s, 
                Office = %s,
                State = %s,
                CommitteeID = %s,
                ElectionID = %s
            WHERE CandidateID = %s;
        """
            cursor.execute(update_query, (candidate_name_entry.get(), party_affiliation_entry.get(), office_entry.get(),
                                          state_entry.get(), committee_ID_entry.get(), election_ID_entry.get(),
                                          candidate_ID_entry.get()))
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Updated Successfully")

        update_window = Toplevel(window)
        update_window.title("Candidate Update")
        update_window.geometry("500x400")
        Label(update_window, font=("", 20, "bold"), text="Update Candidate").pack()

        InfoFrame = Frame(update_window)
        InfoFrame.place(x=0, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Enter Info")
        infoFrame.grid(row=0, column=0)

        candidate_ID_label = Label(infoFrame, font=("", 15), text="Enter Candidate ID", height=1)
        candidate_ID_label.grid(row=1, column=0)
        candidate_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        candidate_ID_entry.grid(row=1, column=1)

        candidate_name_label = Label(infoFrame, font=("", 15), text="Enter Candidate Name", height=1)
        candidate_name_label.grid(row=2, column=0)
        candidate_name_entry = Entry(infoFrame, font=("", 15), width=18)
        candidate_name_entry.grid(row=2, column=1)

        party_affiliation_label = Label(infoFrame, font=("", 15), text="Enter Party Affiliation", height=1)
        party_affiliation_label.grid(row=3, column=0)
        party_affiliation_entry = Entry(infoFrame, font=("", 15), width=18)
        party_affiliation_entry.grid(row=3, column=1)

        office_label = Label(infoFrame, font=("", 15), text="Enter Office", height=1)
        office_label.grid(row=4, column=0)
        office_entry = Entry(infoFrame, font=("", 15), width=18)
        office_entry.grid(row=4, column=1)

        state_label = Label(infoFrame, font=("", 15), text="Enter State", height=1)
        state_label.grid(row=5, column=0)
        state_entry = Entry(infoFrame, font=("", 15), width=18)
        state_entry.grid(row=5, column=1)

        committee_ID_label = Label(infoFrame, font=("", 15), text="Enter Committee ID", height=1)
        committee_ID_label.grid(row=6, column=0)
        committee_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        committee_ID_entry.grid(row=6, column=1)

        election_ID_label = Label(infoFrame, font=("", 15), text="Enter Election ID", height=1)
        election_ID_label.grid(row=7, column=0)
        election_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        election_ID_entry.grid(row=7, column=1)

        SubmitFrame = Frame(update_window)
        SubmitFrame.place(x=0, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        update_window.grab_set()

    def candidate_delete_window():
        def submit_query():
            candidateID = candidate_ID_entry.get()
            delete_query = "DELETE FROM Candidate WHERE CandidateID=%s;"

            cursor.execute(delete_query, (candidateID,))
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Deleted Successfully")

        delete_window = Toplevel(window)
        delete_window.title("Candidate Delete")
        delete_window.geometry("400x300")
        Label(delete_window, font=("", 20, "bold"), text="Delete Candidate").pack()

        InfoFrame = Frame(delete_window)
        InfoFrame.place(x=0, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Enter Info")
        infoFrame.grid(row=0, column=0)

        candidate_ID_label = Label(infoFrame, font=("", 15), text="Enter Candidate ID", height=1)
        candidate_ID_label.grid(row=1, column=0)
        candidate_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        candidate_ID_entry.grid(row=1, column=1)

        SubmitFrame = Frame(delete_window)
        SubmitFrame.place(x=0, y=150, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        delete_window.grab_set()

        # ==================== (Candidate) Set Operations: UNION ====================
    def setOpCan():
        def submit_query():
            insert_query = """
                            SELECT DISTINCT CandidateName FROM Candidate WHERE PartyAffiliation = %s
                            UNION
                            SELECT DISTINCT CandidateName FROM Candidate WHERE PartyAffiliation = %s;
                            """
            opElection_data = (opElection_X_entry.get(), opElection_Y_entry.get())
            cursor.execute(insert_query, opElection_data)
            rows = cursor.fetchall()
            if len(rows) != 0:
                opElection_table.delete(*opElection_table.get_children())
                for row in rows:
                    opElection_table.insert("", END, values=row)

        
        # ==================== Main setOp Candidate Window ====================
        opElection_window = Toplevel(window)
        opElection_window.title("(Candidate Table) Set Operations: UNION")
        opElection_window.geometry("900x500")
        Label(opElection_window, font=("", 20, "bold"), text="Set Operations Candidate Table (UNION)").pack()
        opElection_window.grab_set()
        
        # UNION text label
        #label1 = Label(opElection_window, font=("", 9), text="UNION of states involved in x and y elections")
        #label1.place(x=150, y=50)  # Positioning the label widget

        # Insert UNION info frame 
        InfoFrame = Frame(opElection_window)
        InfoFrame.place(x=250, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Insert info")
        infoFrame.grid(row=0, column=0)

        opElection_X_label = Label(infoFrame, font=("", 15), text="Enter Candidate Name X: ", height=1)
        opElection_X_label.grid(row=1, column=0)
        opElection_X_entry = Entry(infoFrame, font=("", 15), width=18)
        opElection_X_entry.grid(row=1, column=1)

        opElection_Y_label = Label(infoFrame, font=("", 15), text="Enter Candidate Name Y: ", height=1)
        opElection_Y_label.grid(row=2, column=0)
        opElection_Y_entry = Entry(infoFrame, font=("", 15), width=18)
        opElection_Y_entry.grid(row=2, column=1)

        # Query info
        label1 = Label(opElection_window, font=("", 9), text= """ Query Info: 
Finds UNION of Candidate Names involved in X and Y Party Affiliation.
Example input: X = Democratic Party, Y = Republican Party""")
        label1.place(x=250, y=150)  # Positioning the label widget


        # Submit button
        SubmitFrame = Frame(opElection_window)
        SubmitFrame.place(x=250, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        # ==================== Table Result Info Frame ====================
        InfoFrame = Frame(opElection_window)
        InfoFrame.place(x=10, y=50, height=700, width=225)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Result")
        infoFrame.grid(row=0, column=0)

        scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
        opElection_table = ttk.Treeview(infoFrame, columns=("CandidateName"),
                                    yscrollcommand=scroll_y.set, height=18)

        opElection_table.column("#0", width=100)
        opElection_table.column("CandidateName", anchor=CENTER, width=200)

        opElection_table.heading("CandidateName", text="Candidate Name")

        opElection_table["show"] = "headings"

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y = ttk.Scrollbar(command=opElection_table.yview)

        opElection_table.pack(fill=BOTH, expand=1)
    
    # ==================== (Candidate) Set Membership: IN ====================  
    def setMemCan():
        def submit_query():
            insert_query = """
                            SELECT CandidateID, CandidateName, PartyAffiliation, Office, State
                            FROM Candidate
                            WHERE (PartyAffiliation, Office) IN (
                                SELECT PartyAffiliation, Office
                                FROM Candidate
                                WHERE PartyAffiliation = %s AND Office = %s
                            );
                            """
            memElection_data = (memElection_X_entry.get(), memElection_Y_entry.get())
            cursor.execute(insert_query, memElection_data)
            rows = cursor.fetchall()
            if len(rows) != 0:
                memElection_table.delete(*memElection_table.get_children())
                for row in rows:
                    memElection_table.insert("", END, values=row)

        
        # ==================== Main setMem Candidate Window ====================
        memElection_window = Toplevel(window)
        memElection_window.title("(Candidate Table) Set Membership: IN")
        memElection_window.geometry("1000x500")
        Label(memElection_window, font=("", 20, "bold"), text="Set Membership Candidate Table (IN)").pack()
        memElection_window.grab_set()

        # Insert IN info frame 
        InfoFrame = Frame(memElection_window)
        InfoFrame.place(x=575, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Insert info")
        infoFrame.grid(row=0, column=0)

        memElection_X_label = Label(infoFrame, font=("", 15), text="Enter Party Affiliation X: ", height=1)
        memElection_X_label.grid(row=1, column=0)
        memElection_X_entry = Entry(infoFrame, font=("", 15), width=18)
        memElection_X_entry.grid(row=1, column=1)

        memElection_Y_label = Label(infoFrame, font=("", 15), text="Enter Office Y: ", height=1)
        memElection_Y_label.grid(row=2, column=0)
        memElection_Y_entry = Entry(infoFrame, font=("", 15), width=18)
        memElection_Y_entry.grid(row=2, column=1)

        # Query info
        label1 = Label(memElection_window, font=("", 9), text= """ Query Info: 
Finds details on candidates with Party Affiliation X and office Y.
Example input: X = Democratic Party, Y = Senator""")
        label1.place(x=565, y=150)  # Positioning the label widget

        # Submit button
        SubmitFrame = Frame(memElection_window)
        SubmitFrame.place(x=575, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        # ==================== Table Result Info Frame ====================
        InfoFrame = Frame(memElection_window)
        InfoFrame.place(x=10, y=50, height=700, width=550)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Result")
        infoFrame.grid(row=0, column=0)

        scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
        memElection_table = ttk.Treeview(infoFrame, columns=("CandidateID", "CandidateName", "PartyAffiliation", "Office", "State"),
                                    yscrollcommand=scroll_y.set, height=18)

        memElection_table.column("#0", width=100)
        memElection_table.column("CandidateID", anchor=CENTER, width=100)
        memElection_table.column("CandidateName", anchor=W, width=125)
        memElection_table.column("PartyAffiliation", anchor=CENTER, width=125)
        memElection_table.column("Office", anchor=CENTER, width=60)
        memElection_table.column("State", anchor=CENTER, width=60)

        memElection_table.heading("CandidateID", text="Candidate ID")
        memElection_table.heading("CandidateName", text="Candidate Name")
        memElection_table.heading("PartyAffiliation", text="Party Affiliation")
        memElection_table.heading("Office", text="Office")
        memElection_table.heading("State", text="State")

        memElection_table["show"] = "headings"

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y = ttk.Scrollbar(command=memElection_table.yview)

        memElection_table.pack(fill=BOTH, expand=1)


    # ==================== (Candidate) Set Comparison: EXISTS ====================  
    def setCompCan():
        def submit_query():
            insert_query = """
                            SELECT CASE 
                                WHEN EXISTS (
                                    SELECT 1
                                    FROM Candidate
                                    WHERE CandidateName LIKE %s '%' 
                                    AND Office = %s
                                ) THEN 'Exists'
                                ELSE NULL
                            END AS Result;
                            """
            comElection_data = (comElection_X_entry.get(), comElection_Y_entry.get())
            cursor.execute(insert_query, comElection_data)
            rows = cursor.fetchall()
            if len(rows) != 0:
                comElection_table.delete(*comElection_table.get_children())
                for row in rows:
                    comElection_table.insert("", END, values=row)

        
        # ==================== Main setComp Candidate Window ====================
        comElection_window = Toplevel(window)
        comElection_window.title("(Candidate Table) Set Comparison: EXISTS")
        comElection_window.geometry("900x500")
        Label(comElection_window, font=("", 20, "bold"), text="Set Comparison Candidate Table (EXISTS)").pack()
        comElection_window.grab_set()

        # Insert ANY info frame 
        InfoFrame = Frame(comElection_window)
        InfoFrame.place(x=225, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Insert info")
        infoFrame.grid(row=0, column=0)

        comElection_X_label = Label(infoFrame, font=("", 15), text="Enter Candidate First Name X: ", height=1)
        comElection_X_label.grid(row=1, column=0)
        comElection_X_entry = Entry(infoFrame, font=("", 15), width=18)
        comElection_X_entry.grid(row=1, column=1)

        comElection_Y_label = Label(infoFrame, font=("", 15), text="Enter Office Y: ", height=1)
        comElection_Y_label.grid(row=2, column=0)
        comElection_Y_entry = Entry(infoFrame, font=("", 15), width=18)
        comElection_Y_entry.grid(row=2, column=1)

        # Query info
        label1 = Label(comElection_window, font=("", 9), text= """ Query Info: 
Checks whether a candidate with First name X is running for office Y.
Example input: X = John, Y = Senator""")
        label1.place(x=225, y=150)  # Positioning the label widget


        # Submit button
        SubmitFrame = Frame(comElection_window)
        SubmitFrame.place(x=225, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        # ==================== Table Result Info Frame ====================
        InfoFrame = Frame(comElection_window)
        InfoFrame.place(x=10, y=50, height=700, width=150)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Result")
        infoFrame.grid(row=0, column=0)

        scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
        comElection_table = ttk.Treeview(infoFrame, columns=("Result"),
                                    yscrollcommand=scroll_y.set, height=18)

        comElection_table.column("#0", width=100)
        comElection_table.column("Result", anchor=CENTER, width=80)


        comElection_table.heading("Result", text="Result")

        comElection_table["show"] = "headings"

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y = ttk.Scrollbar(command=comElection_table.yview)

        comElection_table.pack(fill=BOTH, expand=1)

    # ==================== (Candidate) Calculate the Cumulative Partys ====================  
    def calcCumCan():
        def fetch_data():
            insert_query = """
                            SELECT CandidateName, PartyAffiliation, State,
                            COUNT(*) OVER (PARTITION BY PartyAffiliation ORDER BY State) AS CumulativePartys
                            FROM Candidate
                            ORDER BY PartyAffiliation, State;
                            """
            cursor.execute(insert_query)
            rows = cursor.fetchall()
            if len(rows) != 0:
                calcCumElection_table.delete(*calcCumElection_table.get_children())
                for row in rows:
                    calcCumElection_table.insert("", END, values=row)

        
        # ==================== Main calCum Candidate Window ====================
        calcCumElection_window = Toplevel(window)
        calcCumElection_window.title("(Candidate Table) Advanced Aggregate Functions: WINDOW Functions")
        calcCumElection_window.geometry("900x500")
        Label(calcCumElection_window, font=("", 20, "bold"), text="Calculate Cumulative Candidate Table (COUNT)").pack()
        calcCumElection_window.grab_set()

        # ==================== Table Result Info Frame ====================
        InfoFrame = Frame(calcCumElection_window)
        InfoFrame.place(x=150, y=50, height=700, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Result")
        infoFrame.grid(row=0, column=0)

        # Query info
        label1 = Label(calcCumElection_window, font=("", 9), text= """ Query Info: 
Calculates running total of candidates per party affiliation in each state.""")
        label1.place(x=550, y=150)  # Positioning the label widget

        scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
        calcCumElection_table = ttk.Treeview(infoFrame, columns=("CandidateName", "PartyAffiliation", "State", "CumulativePartys"),
                                    yscrollcommand=scroll_y.set, height=18)

        calcCumElection_table.column("#0", width=100)
        calcCumElection_table.column("CandidateName", anchor=CENTER, width=115)
        calcCumElection_table.column("PartyAffiliation", anchor=CENTER, width=125)
        calcCumElection_table.column("State", anchor=CENTER, width=60)
        calcCumElection_table.column("CumulativePartys", anchor=CENTER, width=60)


        calcCumElection_table.heading("CandidateName", text="CandidateName")
        calcCumElection_table.heading("PartyAffiliation", text="PartyAffiliation")
        calcCumElection_table.heading("State", text="State")
        calcCumElection_table.heading("CumulativePartys", text="Cumulative Partys")
        

        calcCumElection_table["show"] = "headings"

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y = ttk.Scrollbar(command=calcCumElection_table.yview)

        calcCumElection_table.pack(fill=BOTH, expand=1)
        fetch_data()
    
    # ==================== (Candidate) Subqueries using the WITH Clause ====================  
    def withClauseCan():
        def submit_query():
            insert_query = """
                            WITH SenatorCandidates AS (
                                SELECT c.CandidateID, c.CandidateName, c.PartyAffiliation, c.Office, c.State, com.CommitteeName
                                FROM Candidate c
                                JOIN Committee com ON c.CommitteeID = com.CommitteeID
                                WHERE c.Office = %s
                            )
                            SELECT *
                            FROM SenatorCandidates;
                            """
            withClauseElection_data = (withClauseElection_X_entry.get(),)
            cursor.execute(insert_query, withClauseElection_data)
            rows = cursor.fetchall()
            if len(rows) != 0:
                withClauseElection_table.delete(*withClauseElection_table.get_children())
                for row in rows:
                    withClauseElection_table.insert("", END, values=row)

        
        # ==================== Main withClause Election Window ====================
        withClauseElection_window = Toplevel(window)
        withClauseElection_window.title("(Candidate Table) Subqueries using the WITH Clause")
        withClauseElection_window.geometry("1150x500")
        Label(withClauseElection_window, font=("", 20, "bold"), text="Subqueries using the WITH Clause").pack()
        withClauseElection_window.grab_set()

        # Insert ANY info frame 
        InfoFrame = Frame(withClauseElection_window)
        InfoFrame.place(x=700, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 10, "bold"), text="Insert Info")
        infoFrame.grid(row=0, column=0)

        withClauseElection_X_label = Label(infoFrame, font=("", 15), text="Enter Office X: ", height=1)
        withClauseElection_X_label.grid(row=1, column=0)
        withClauseElection_X_entry = Entry(infoFrame, font=("", 15), width=18)
        withClauseElection_X_entry.grid(row=1, column=1)

        # Query info
        label1 = Label(withClauseElection_window, font=("", 9), text= """ Query Info: 
This CTE named SenatorCandidates isolates all candidates running for the office of Senator 
and includes a JOIN to the Committee table to bring in the CommitteeName based on the CommitteeID.
After defining the CTE, the main query selects all the information from this temporary set.
Example input: X = Senator""")
        label1.place(x=675, y=150)  # Positioning the label widget

        # Submit button
        SubmitFrame = Frame(withClauseElection_window)
        SubmitFrame.place(x=700, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        # ==================== Table Result Info Frame ====================
        InfoFrame = Frame(withClauseElection_window)
        InfoFrame.place(x=10, y=50, height=700, width=650)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Result")
        infoFrame.grid(row=0, column=0)

        scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
        withClauseElection_table = ttk.Treeview(infoFrame, columns=("CandidateID", "CandidateName", "PartyAffiliation", "Office", "State", "CommitteeName"),
                                    yscrollcommand=scroll_y.set, height=18)

        withClauseElection_table.column("#0", width=100)
        withClauseElection_table.column("CandidateID", anchor=CENTER, width=80)
        withClauseElection_table.column("CandidateName", anchor=W, width=125)
        withClauseElection_table.column("PartyAffiliation", anchor=CENTER, width=125)
        withClauseElection_table.column("Office", anchor=CENTER, width=60)
        withClauseElection_table.column("State", anchor=CENTER, width=60)
        withClauseElection_table.column("CommitteeName", anchor=W, width=175)

        withClauseElection_table.heading("CandidateID", text="Candidate ID")
        withClauseElection_table.heading("CandidateName", text="Candidate Name")
        withClauseElection_table.heading("PartyAffiliation", text="Party Affiliation")
        withClauseElection_table.heading("Office", text="Office")
        withClauseElection_table.heading("State", text="State")
        withClauseElection_table.heading("CommitteeName", text="Committee Name")

        withClauseElection_table["show"] = "headings"

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y = ttk.Scrollbar(command=withClauseElection_table.yview)

        withClauseElection_table.pack(fill=BOTH, expand=1)


    # ==================== Main Candidate Window ====================
    candidate_window = Toplevel(window)
    candidate_window.title("Candidate Table")
    candidate_window.geometry("1000x500")
    Label(candidate_window, font=("", 20, "bold"), text="Candidate").pack()
    candidate_window.grab_set()

    # ==================== Actions Frame ====================
    ActionFrame = Frame(candidate_window)
    ActionFrame.place(x=725, y=50, height=500, width=500)
    actionFrame = LabelFrame(ActionFrame, font=("", 15, "bold"), text="Select an action")
    actionFrame.grid(row=0, column=0)

    insert_button = Button(actionFrame, text="Insert Data", font=("", 15), width=10, height=1,
                           command=candidate_insert_window)
    insert_button.grid(row=1, column=0)

    update_button = Button(actionFrame, text="Update Data", font=("", 15), width=10, height=1,
                           command=candidate_update_window)
    update_button.grid(row=2, column=0)

    delete_button = Button(actionFrame, text="Delete Data", font=("", 15), width=10, height=1,
                           command=candidate_delete_window)
    delete_button.grid(row=3, column=0)

    setOP_button = Button(actionFrame, text="Set Operations", font=("", 15), width=10, height=1,
                           command= setOpCan)
    setOP_button.grid(row=4, column=0)

    setMem_button = Button(actionFrame, text="Set Membership", font=("", 15), width=10, height=1,
                           command= setMemCan)
    setMem_button.grid(row=5, column=0)

    setCom_button = Button(actionFrame, text="Set Comparison", font=("", 15), width=10, height=1,
                           command= setCompCan)
    setCom_button.grid(row=6, column=0)

    calCum_button = Button(actionFrame, text="Calculate Cumulative", font=("", 15), width=15, height=1,
                           command= calcCumCan)
    calCum_button.grid(row=7, column=0)

    withClause_button = Button(actionFrame, text="Subqueries using the WITH Clause", font=("", 15), width=23, height=1,
                           command= withClauseCan)
    withClause_button.grid(row=8, column=0)

    # ==================== Table Info Frame ====================
    InfoFrame = Frame(candidate_window)
    InfoFrame.place(x=10, y=50, height=700, width=700)
    infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Candidate Info")
    infoFrame.grid(row=0, column=0)

    scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
    candidate_table = ttk.Treeview(infoFrame, columns=("candidateID", "candidateName", "partyAffiliation", "office",
                                                       "state", "committeeID", "electionID"),
                                   yscrollcommand=scroll_y.set, height=18)

    candidate_table.column("#0", width=100)
    candidate_table.column("candidateID", anchor=W, width=100)
    candidate_table.column("candidateName", anchor=W, width=100)
    candidate_table.column("partyAffiliation", anchor=W, width=100)
    candidate_table.column("office", anchor=W, width=100)
    candidate_table.column("state", anchor=CENTER, width=60)
    candidate_table.column("committeeID", anchor=W, width=100)
    candidate_table.column("electionID", anchor=W, width=100)

    candidate_table.heading("candidateID", text="Candidate ID")
    candidate_table.heading("candidateName", text="Candidate Name")
    candidate_table.heading("partyAffiliation", text="Party Affiliation")
    candidate_table.heading("office", text="Office")
    candidate_table.heading("state", text="State")
    candidate_table.heading("committeeID", text="Committee ID")
    candidate_table.heading("electionID", text="Election ID")

    candidate_table["show"] = "headings"

    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_y = ttk.Scrollbar(command=candidate_table.yview)

    candidate_table.pack(fill=BOTH, expand=1)

    fetch_data()


# ==================== Contribution Window ====================
def open_contribution_window():
    #function to show everything in the table
    def fetch_data():
        cursor.execute("SELECT * FROM contribution")
        rows = cursor.fetchall()
        if len(rows) != 0:
            contribution_table.delete(*contribution_table.get_children())
            for row in rows:
                contribution_table.insert("", END, values=row)
            connection.commit()

    #function to highlight a row that you click on
    def get_cursor():
        cursor_row = contribution_table.focus()

    # ==================== Button Windows ====================
    def contribution_insert_window():
        def submit_query():
            insert_query = "INSERT INTO Contribution (ContributionID, DonorName, CommitteeID, Amount, Date) VALUES (%s, %s, %s, %s, %s)"
            contribution_data = (contribution_ID_entry.get(), donor_name_entry.get(), committee_ID_entry.get(),
                                 amount_entry.get(), date_entry.get())
            cursor.execute(insert_query, contribution_data)
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Inserted Successfully")

        insert_window = Toplevel(window)
        insert_window.title("Contribution Insert")
        insert_window.geometry("500x400")
        Label(insert_window, font=("", 20, "bold"), text="Insert Contribution").pack()

        InfoFrame = Frame(insert_window)
        InfoFrame.place(x=0, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Enter Info")
        infoFrame.grid(row=0, column=0)

        contribution_ID_label = Label(infoFrame, font=("", 15), text="Enter Contribution ID", height=1)
        contribution_ID_label.grid(row=1, column=0)
        contribution_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        contribution_ID_entry.grid(row=1, column=1)

        donor_name_label = Label(infoFrame, font=("", 15), text="Enter Donor Name", height=1)
        donor_name_label.grid(row=2, column=0)
        donor_name_entry = Entry(infoFrame, font=("", 15), width=18)
        donor_name_entry.grid(row=2, column=1)

        committee_ID_label = Label(infoFrame, font=("", 15), text="Enter Committee ID", height=1)
        committee_ID_label.grid(row=3, column=0)
        committee_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        committee_ID_entry.grid(row=3, column=1)

        amount_label = Label(infoFrame, font=("", 15), text="Enter Amount", height=1)
        amount_label.grid(row=4, column=0)
        amount_entry = Entry(infoFrame, font=("", 15), width=18)
        amount_entry.grid(row=4, column=1)

        date_label = Label(infoFrame, font=("", 15), text="Enter Date", height=1)
        date_label.grid(row=5, column=0)
        date_entry = Entry(infoFrame, font=("", 15), width=18)
        date_entry.grid(row=5, column=1)

        SubmitFrame = Frame(insert_window)
        SubmitFrame.place(x=0, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        insert_window.grab_set()

    def contribution_update_window():
        def submit_query():
            update_query = """
            UPDATE Contribution
            SET DonorName = %s, 
                CommitteeID = %s, 
                Amount = %s,
                Date = %s
            WHERE ContributionID = %s;
        """
            cursor.execute(update_query, (donor_name_entry.get(), committee_ID_entry.get(), amount_entry.get(),
                                          date_entry.get(), contribution_ID_entry.get()))
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Updated Successfully")

        update_window = Toplevel(window)
        update_window.title("Contribution Update")
        update_window.geometry("500x400")
        Label(update_window, font=("", 20, "bold"), text="Update Contribution").pack()

        InfoFrame = Frame(update_window)
        InfoFrame.place(x=0, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"))
        infoFrame.grid(row=0, column=0)

        contribution_ID_label = Label(infoFrame, font=("", 15), text="Enter Contribution ID", height=1)
        contribution_ID_label.grid(row=1, column=0)
        contribution_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        contribution_ID_entry.grid(row=1, column=1)

        donor_name_label = Label(infoFrame, font=("", 15), text="Enter Donor Name", height=1)
        donor_name_label.grid(row=2, column=0)
        donor_name_entry = Entry(infoFrame, font=("", 15), width=18)
        donor_name_entry.grid(row=2, column=1)

        committee_ID_label = Label(infoFrame, font=("", 15), text="Enter Committee ID", height=1)
        committee_ID_label.grid(row=3, column=0)
        committee_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        committee_ID_entry.grid(row=3, column=1)

        amount_label = Label(infoFrame, font=("", 15), text="Enter Amount", height=1)
        amount_label.grid(row=4, column=0)
        amount_entry = Entry(infoFrame, font=("", 15), width=18)
        amount_entry.grid(row=4, column=1)

        date_label = Label(infoFrame, font=("", 15), text="Enter Date", height=1)
        date_label.grid(row=5, column=0)
        date_entry = Entry(infoFrame, font=("", 15), width=18)
        date_entry.grid(row=5, column=1)

        SubmitFrame = Frame(update_window)
        SubmitFrame.place(x=0, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        update_window.grab_set()

    def contribution_delete_window():
        def submit_query():
            contributionID = contribution_ID_entry.get()
            delete_query = "DELETE FROM Contribution WHERE ContributionID = %s;"
            cursor.execute(delete_query, (contributionID,))
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Deleted Successfully")

        delete_window = Toplevel(window)
        delete_window.title("Contribution Delete")
        delete_window.geometry("400x300")
        Label(delete_window, font=("", 20, "bold"), text="Delete Contribution").pack()

        InfoFrame = Frame(delete_window)
        InfoFrame.place(x=0, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Enter Info")
        infoFrame.grid(row=0, column=0)

        contribution_ID_label = Label(infoFrame, font=("", 15), text="Enter Contribution ID", height=1)
        contribution_ID_label.grid(row=1, column=0)
        contribution_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        contribution_ID_entry.grid(row=1, column=1)

        SubmitFrame = Frame(delete_window)
        SubmitFrame.place(x=0, y=150, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        delete_window.grab_set()


        # ==================== (Contribution) Set Operations: UNION ====================
    def setOpCon():
        def submit_query():
            insert_query = """
                            SELECT DonorName FROM Contribution WHERE CommitteeID = %s
                            UNION
                            SELECT DonorName FROM Contribution WHERE CommitteeID = %s;
                            """
            opElection_data = (opElection_X_entry.get(), opElection_Y_entry.get())
            cursor.execute(insert_query, opElection_data)
            rows = cursor.fetchall()
            if len(rows) != 0:
                opElection_table.delete(*opElection_table.get_children())
                for row in rows:
                    opElection_table.insert("", END, values=row)

        
        # ==================== Main setOp Contribution Window ====================
        opElection_window = Toplevel(window)
        opElection_window.title("(Contribution Table) Set Operations: UNION")
        opElection_window.geometry("900x500")
        Label(opElection_window, font=("", 20, "bold"), text="Set Operations Contribution Table (UNION)").pack()
        opElection_window.grab_set()
        
        # UNION text label
        #label1 = Label(opElection_window, font=("", 9), text="UNION of states involved in x and y elections")
        #label1.place(x=150, y=50)  # Positioning the label widget

        # Insert UNION info frame 
        InfoFrame = Frame(opElection_window)
        InfoFrame.place(x=175, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Insert info")
        infoFrame.grid(row=0, column=0)

        opElection_X_label = Label(infoFrame, font=("", 15), text="Enter Committee ID X: ", height=1)
        opElection_X_label.grid(row=1, column=0)
        opElection_X_entry = Entry(infoFrame, font=("", 15), width=18)
        opElection_X_entry.grid(row=1, column=1)

        opElection_Y_label = Label(infoFrame, font=("", 15), text="Enter Committee ID Y: ", height=1)
        opElection_Y_label.grid(row=2, column=0)
        opElection_Y_entry = Entry(infoFrame, font=("", 15), width=18)
        opElection_Y_entry.grid(row=2, column=1)

        # Query info
        label1 = Label(opElection_window, font=("", 9), text= """ Query Info: 
Finds UNION of donor names from committee ID's X and Y
Example input: X = 1, Y = 2""")
        label1.place(x=175, y=150)  # Positioning the label widget


        # Submit button
        SubmitFrame = Frame(opElection_window)
        SubmitFrame.place(x=175, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        # ==================== Table Result Info Frame ====================
        InfoFrame = Frame(opElection_window)
        InfoFrame.place(x=10, y=50, height=700, width=150)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Result")
        infoFrame.grid(row=0, column=0)

        scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
        opElection_table = ttk.Treeview(infoFrame, columns=("DonorName"),
                                    yscrollcommand=scroll_y.set, height=18)

        opElection_table.column("#0", width=100)
        opElection_table.column("DonorName", anchor=CENTER, width=100)

        opElection_table.heading("DonorName", text="Donor Name")

        opElection_table["show"] = "headings"

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y = ttk.Scrollbar(command=opElection_table.yview)

        opElection_table.pack(fill=BOTH, expand=1)
    
    # ==================== (Contribution) Set Membership: IN ====================  
    def setMemCon():
        def submit_query():
            insert_query = """
                            SELECT CASE 
                            WHEN EXISTS (
                                SELECT 1
                                FROM Contribution
                                WHERE DonorName LIKE %s '%'
                                AND CommitteeID = %s
                                ) THEN 'Exists'
                            ELSE NULL
                            END AS Result;
                            """
            memElection_data = (memElection_X_entry.get(), memElection_Y_entry.get())
            cursor.execute(insert_query, memElection_data)
            rows = cursor.fetchall()
            if len(rows) != 0:
                memElection_table.delete(*memElection_table.get_children())
                for row in rows:
                    memElection_table.insert("", END, values=row)

        
        # ==================== Main setMem Contribution Window ====================
        memElection_window = Toplevel(window)
        memElection_window.title("(Contribution Table) Set Membership: EXISTS")
        memElection_window.geometry("900x500")
        Label(memElection_window, font=("", 20, "bold"), text="Set Membership Contribution Table (EXISTS)").pack()
        memElection_window.grab_set()

        # Insert info frame 
        InfoFrame = Frame(memElection_window)
        InfoFrame.place(x=225, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Insert info")
        infoFrame.grid(row=0, column=0)

        memElection_X_label = Label(infoFrame, font=("", 15), text="Enter Donor name X: ", height=1)
        memElection_X_label.grid(row=1, column=0)
        memElection_X_entry = Entry(infoFrame, font=("", 15), width=18)
        memElection_X_entry.grid(row=1, column=1)

        memElection_Y_label = Label(infoFrame, font=("", 15), text="Enter Committee ID Y: ", height=1)
        memElection_Y_label.grid(row=2, column=0)
        memElection_Y_entry = Entry(infoFrame, font=("", 15), width=18)
        memElection_Y_entry.grid(row=2, column=1)

        # Query info
        label1 = Label(memElection_window, font=("", 9), text= """ Query Info: 
checks if a specific donor has made contributions to a particular committee.
Example input: X = John Smith, Y = 1""")
        label1.place(x=215, y=150)  # Positioning the label widget

        # Submit button
        SubmitFrame = Frame(memElection_window)
        SubmitFrame.place(x=225, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        # ==================== Table Result Info Frame ====================
        InfoFrame = Frame(memElection_window)
        InfoFrame.place(x=10, y=50, height=700, width=150)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Result")
        infoFrame.grid(row=0, column=0)

        scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
        memElection_table = ttk.Treeview(infoFrame, columns=("Result"),
                                    yscrollcommand=scroll_y.set, height=18)

        memElection_table.column("#0", width=100)
        memElection_table.column("Result", anchor=CENTER, width=60)

        memElection_table.heading("Result", text="Result")

        memElection_table["show"] = "headings"

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y = ttk.Scrollbar(command=memElection_table.yview)

        memElection_table.pack(fill=BOTH, expand=1)


    # ==================== (Contributions) Set Comparison: ANY ====================  
    def setCompCon():
        def submit_query():
            insert_query = """
                            -- Checks if there are any contributions made to X that are larger than Y
                            SELECT *
                            FROM Contribution c1
                            WHERE c1.CommitteeID = %s
                            AND Amount > ALL (
                                SELECT Amount
                                FROM Contribution c2
                                WHERE c2.CommitteeID = %s
                            );
                            """
            comElection_data = (comElection_X_entry.get(), comElection_Y_entry.get())
            cursor.execute(insert_query, comElection_data)
            rows = cursor.fetchall()
            if len(rows) != 0:
                comElection_table.delete(*comElection_table.get_children())
                for row in rows:
                    comElection_table.insert("", END, values=row)

        
        # ==================== Main setCom Contribution Window ====================
        comElection_window = Toplevel(window)
        comElection_window.title("(Contribution Table) Set Comparison: ANY")
        comElection_window.geometry("1000x500")
        Label(comElection_window, font=("", 20, "bold"), text="Set Comparison Contribution Table (ANY)").pack()
        comElection_window.grab_set()

        # Insert ANY info frame 
        InfoFrame = Frame(comElection_window)
        InfoFrame.place(x=550, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Insert info")
        infoFrame.grid(row=0, column=0)

        comElection_X_label = Label(infoFrame, font=("", 15), text="Enter Committee ID X: ", height=1)
        comElection_X_label.grid(row=1, column=0)
        comElection_X_entry = Entry(infoFrame, font=("", 15), width=18)
        comElection_X_entry.grid(row=1, column=1)

        comElection_Y_label = Label(infoFrame, font=("", 15), text="Enter Committee ID Y: ", height=1)
        comElection_Y_label.grid(row=2, column=0)
        comElection_Y_entry = Entry(infoFrame, font=("", 15), width=18)
        comElection_Y_entry.grid(row=2, column=1)

        # Query info
        label1 = Label(comElection_window, font=("", 9), text= """ Query Info: 
Checks if there are any contributions made to Committee ID X that are larger than Y
Example input: X = Governor Election, Y = 2023""")
        label1.place(x=550, y=150)  # Positioning the label widget

        # Submit button
        SubmitFrame = Frame(comElection_window)
        SubmitFrame.place(x=550, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        # ==================== Table Result Info Frame ====================
        InfoFrame = Frame(comElection_window)
        InfoFrame.place(x=10, y=50, height=700, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Result")
        infoFrame.grid(row=0, column=0)

        scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
        comElection_table = ttk.Treeview(infoFrame, columns=("ContributionID", "DonorName", "CommitteeID", "Amount", "Date"),
                                    yscrollcommand=scroll_y.set, height=18)

        comElection_table.column("#0", width=100)
        comElection_table.column("ContributionID", anchor=CENTER, width=100)
        comElection_table.column("DonorName", anchor=W, width=125)
        comElection_table.column("CommitteeID", anchor=CENTER, width=100)
        comElection_table.column("Amount", anchor=CENTER, width=60)
        comElection_table.column("Date", anchor=CENTER, width=100)

        comElection_table.heading("ContributionID", text="Contribution ID")
        comElection_table.heading("DonorName", text="Donor Name")
        comElection_table.heading("CommitteeID", text="Committee ID")
        comElection_table.heading("Amount", text="Amount")
        comElection_table.heading("Date", text="Date")

        comElection_table["show"] = "headings"

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y = ttk.Scrollbar(command=comElection_table.yview)

        comElection_table.pack(fill=BOTH, expand=1)

    # ==================== (Contribution) Calculate the Cumulative Contributions made ====================  
    def calcCumCon():
        def fetch_data():
            insert_query = """
                            SELECT CommitteeID, Date, Amount,
                                SUM(Amount) OVER (PARTITION BY NULL ORDER BY Date) AS RunningTotal
                            FROM Contribution
                            ORDER BY CommitteeID, Date;
                            """
            cursor.execute(insert_query)
            rows = cursor.fetchall()
            if len(rows) != 0:
                calcCumElection_table.delete(*calcCumElection_table.get_children())
                for row in rows:
                    calcCumElection_table.insert("", END, values=row)

        
        # ==================== Main calCum Contribution Window ====================
        calcCumElection_window = Toplevel(window)
        calcCumElection_window.title("(Contribution Table) Advanced Aggregate Functions: WINDOW Functions")
        calcCumElection_window.geometry("900x500")
        Label(calcCumElection_window, font=("", 20, "bold"), text="Calculate Cumulative Contribution Table (SUM)").pack()
        calcCumElection_window.grab_set()

        # ==================== Table Result Info Frame ====================
        InfoFrame = Frame(calcCumElection_window)
        InfoFrame.place(x=300, y=50, height=700, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Result")
        infoFrame.grid(row=0, column=0)

        # Query info
        label1 = Label(calcCumElection_window, font=("", 9), text= """ Query Info: 
Calculates running total of contributions made to all committees.""")
        label1.place(x=300, y=450)  # Positioning the label widget

        scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
        calcCumElection_table = ttk.Treeview(infoFrame, columns=("CommitteeID", "date", "Amount", "RunningTotal"),
                                    yscrollcommand=scroll_y.set, height=18)

        calcCumElection_table.column("#0", width=100)
        calcCumElection_table.column("CommitteeID", anchor=CENTER, width=80)
        calcCumElection_table.column("date", anchor=CENTER, width=100)
        calcCumElection_table.column("Amount", anchor=CENTER, width=60)
        calcCumElection_table.column("RunningTotal", anchor=CENTER, width=80)


        calcCumElection_table.heading("CommitteeID", text="Committee ID")
        calcCumElection_table.heading("date", text="Date")
        calcCumElection_table.heading("Amount", text="Amount")
        calcCumElection_table.heading("RunningTotal", text="Running Total")

        calcCumElection_table["show"] = "headings"

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y = ttk.Scrollbar(command=calcCumElection_table.yview)

        calcCumElection_table.pack(fill=BOTH, expand=1)
        fetch_data()
    
    # ==================== (Contribution) Subqueries using the WITH Clause ====================  
    def withClauseCon():
        def submit_query():
            insert_query = """
                            -- CTE for contributions over 5000
                            WITH HighValueContributions AS (
                                SELECT *
                                FROM Contribution
                                WHERE Amount > %s
                            )
                            SELECT *
                            FROM HighValueContributions;
                            """
            withClauseElection_data = (withClauseElection_X_entry.get(),)
            cursor.execute(insert_query, withClauseElection_data)
            rows = cursor.fetchall()
            if len(rows) != 0:
                withClauseElection_table.delete(*withClauseElection_table.get_children())
                for row in rows:
                    withClauseElection_table.insert("", END, values=row)

        
        # ==================== Main withClause Election Window ====================
        withClauseElection_window = Toplevel(window)
        withClauseElection_window.title("(Election Table) Subqueries using the WITH Clause")
        withClauseElection_window.geometry("900x500")
        Label(withClauseElection_window, font=("", 20, "bold"), text="Subqueries using the WITH Clause").pack()
        withClauseElection_window.grab_set()

        # Insert ANY info frame 
        InfoFrame = Frame(withClauseElection_window)
        InfoFrame.place(x=525, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 10, "bold"), text="Insert Info")
        infoFrame.grid(row=0, column=0)

        withClauseElection_X_label = Label(infoFrame, font=("", 15), text="Enter Date X: ", height=1)
        withClauseElection_X_label.grid(row=1, column=0)
        withClauseElection_X_entry = Entry(infoFrame, font=("", 15), width=18)
        withClauseElection_X_entry.grid(row=1, column=1)

        # Query info
        label1 = Label(withClauseElection_window, font=("", 9), text= """ Query Info: 
This query uses a Common Table Expression (CTE) to find all contributions over X.
Example input: X = 5000""")
        label1.place(x=525, y=150)  # Positioning the label widget

        # Submit button
        SubmitFrame = Frame(withClauseElection_window)
        SubmitFrame.place(x=525, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        # ==================== Table Result Info Frame ====================
        InfoFrame = Frame(withClauseElection_window)
        InfoFrame.place(x=10, y=50, height=700, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Result")
        infoFrame.grid(row=0, column=0)

        scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
        withClauseElection_table = ttk.Treeview(infoFrame, columns=("ContributionID", "DonorName", "CommitteeID", "Amount", "Date"),
                                    yscrollcommand=scroll_y.set, height=18)

        withClauseElection_table.column("#0", width=100)
        withClauseElection_table.column("ContributionID", anchor=CENTER, width=100)
        withClauseElection_table.column("DonorName", anchor=W, width=125)
        withClauseElection_table.column("CommitteeID", anchor=CENTER, width=100)
        withClauseElection_table.column("Amount", anchor=CENTER, width=60)
        withClauseElection_table.column("Date", anchor=CENTER, width=85)

        withClauseElection_table.heading("ContributionID", text="Contribution ID")
        withClauseElection_table.heading("DonorName", text="Donor Name")
        withClauseElection_table.heading("CommitteeID", text="Committee ID")
        withClauseElection_table.heading("Amount", text="Amount")
        withClauseElection_table.heading("Date", text="Date")

        withClauseElection_table["show"] = "headings"

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y = ttk.Scrollbar(command=withClauseElection_table.yview)

        withClauseElection_table.pack(fill=BOTH, expand=1)

    
    # ==================== Main Contribution Window ====================
    contribution_window = Toplevel(window)
    contribution_window.title("Contribution Table")
    contribution_window.geometry("900x500")
    Label(contribution_window, font=("", 20, "bold"), text="Contribution").pack()
    contribution_window.grab_set()

    # ==================== Actions Frame ====================
    ActionFrame = Frame(contribution_window)
    ActionFrame.place(x=600, y=50, height=500, width=500)
    actionFrame = LabelFrame(ActionFrame, font=("", 15, "bold"), text="Select an action")
    actionFrame.grid(row=0, column=0)

    insert_button = Button(actionFrame, text="Insert Data", font=("", 15), width=10, height=1,
                           command=contribution_insert_window)
    insert_button.grid(row=1, column=0)

    update_button = Button(actionFrame, text="Update Data", font=("", 15), width=10, height=1,
                           command=contribution_update_window)
    update_button.grid(row=2, column=0)

    delete_button = Button(actionFrame, text="Delete Data", font=("", 15), width=10, height=1,
                           command=contribution_delete_window)
    delete_button.grid(row=3, column=0)

    setOP_button = Button(actionFrame, text="Set Operations", font=("", 15), width=10, height=1,
                           command= setOpCon)
    setOP_button.grid(row=4, column=0)

    setMem_button = Button(actionFrame, text="Set Membership", font=("", 15), width=10, height=1,
                           command= setMemCon)
    setMem_button.grid(row=5, column=0)

    setCom_button = Button(actionFrame, text="Set Comparison", font=("", 15), width=10, height=1,
                           command= setCompCon)
    setCom_button.grid(row=6, column=0)

    calCum_button = Button(actionFrame, text="Calculate Cumulative", font=("", 15), width=15, height=1,
                           command= calcCumCon)
    calCum_button.grid(row=7, column=0)

    withClause_button = Button(actionFrame, text="Subqueries using the WITH Clause", font=("", 15), width=23, height=1,
                           command= withClauseCon)
    withClause_button.grid(row=8, column=0)

    # ==================== Table Info Frame ====================
    InfoFrame = Frame(contribution_window)
    InfoFrame.place(x=0, y=50, height=700, width=600)
    infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Contribution Info")
    infoFrame.grid(row=0, column=0)

    scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
    contribution_table = ttk.Treeview(infoFrame, columns=("contributionID", "donorName", "committeeID", "amount", "date"),
                                      yscrollcommand=scroll_y, height=18)

    contribution_table.column("#0", width=100)
    contribution_table.column("contributionID", anchor=W, width=100)
    contribution_table.column("donorName", anchor=W, width=100)
    contribution_table.column("committeeID", anchor=W, width=100)
    contribution_table.column("amount", anchor=W, width=100)
    contribution_table.column("date", anchor=W, width=100)

    contribution_table.heading("contributionID", text="Contribution ID")
    contribution_table.heading("donorName", text="Donor Name")
    contribution_table.heading("committeeID", text="Committee ID")
    contribution_table.heading("amount", text="Amount")
    contribution_table.heading("date", text="Date")

    contribution_table["show"] = "headings"

    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_y = ttk.Scrollbar(command=contribution_table.yview)

    contribution_table.pack(fill=BOTH, expand=1)

    fetch_data()


# ==================== Expenditure Window ====================
def open_expenditure_window():
    # function to show everything in the table
    def fetch_data():
        cursor.execute("SELECT * FROM expenditure")
        rows = cursor.fetchall()
        if len(rows) != 0:
            expenditure_table.delete(*expenditure_table.get_children())
            for row in rows:
                expenditure_table.insert("", END, values=row)
            connection.commit()

    #function to highlight a row that you click on
    def get_cursor():
        cursor_row = expenditure_table.focus()

    # ==================== Button Windows ====================
    def expenditure_insert_window():
        def submit_query():
            insert_query = "INSERT INTO Expenditure (ExpenditureID, Payee, CommitteeID, Amount, Purpose, Date) VALUES (%s, %s, %s, %s, %s, %s)"
            expenditure_data = (expenditure_ID_entry.get(), payee_entry.get(), committee_ID_entry.get(),
                                amount_entry.get(), purpose_entry.get(), date_entry.get())
            cursor.execute(insert_query, expenditure_data)
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Inserted Successfully")

        insert_window = Toplevel(window)
        insert_window.title("Expenditure Insert")
        insert_window.geometry("500x400")
        Label(insert_window, font=("", 20, "bold"), text="Insert Expenditure").pack()

        InfoFrame = Frame(insert_window)
        InfoFrame.place(x=0, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Enter Info")
        infoFrame.grid(row=0, column=0)

        expenditure_ID_label = Label(infoFrame, font=("", 15), text="Enter Expenditure ID", height=1)
        expenditure_ID_label.grid(row=1, column=0)
        expenditure_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        expenditure_ID_entry.grid(row=1, column=1)

        payee_label = Label(infoFrame, font=("", 15), text="Enter Payee Name", height=1)
        payee_label.grid(row=2, column=0)
        payee_entry = Entry(infoFrame, font=("", 15), width=18)
        payee_entry.grid(row=2, column=1)

        committee_ID_label = Label(infoFrame, font=("", 15), text="Enter Committee ID", height=1)
        committee_ID_label.grid(row=3, column=0)
        committee_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        committee_ID_entry.grid(row=3, column=1)

        amount_label = Label(infoFrame, font=("", 15), text="Enter Amount", height=1)
        amount_label.grid(row=4, column=0)
        amount_entry = Entry(infoFrame, font=("", 15), width=18)
        amount_entry.grid(row=4, column=1)

        purpose_label = Label(infoFrame, font=("", 15), text="Enter Purpose", height=1)
        purpose_label.grid(row=5, column=0)
        purpose_entry = Entry(infoFrame, font=("", 15), width=18)
        purpose_entry.grid(row=5, column=1)

        date_label = Label(infoFrame, font=("", 15), text="Enter Date", height=1)
        date_label.grid(row=6, column=0)
        date_entry = Entry(infoFrame, font=("", 15), width=18)
        date_entry.grid(row=6, column=1)

        SubmitFrame = Frame(insert_window)
        SubmitFrame.place(x=0, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        insert_window.grab_set()

    def expenditure_update_window():
        def submit_query():
            update_query = """
            UPDATE Expenditure
            SET Payee = %s, 
                CommitteeID = %s, 
                Amount = %s,
                Purpose = %s,
                Date = %s
            WHERE ExpenditureID = %s;
        """
            cursor.execute(update_query, (payee_entry.get(), committee_ID_entry.get(), amount_entry.get(),
                                          payee_entry.get(), date_entry.get(), expenditure_ID_entry.get()))
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Updated Successfully")

        update_window = Toplevel(window)
        update_window.title("Expenditure Update")
        update_window.geometry("500x400")
        Label(update_window, font=("", 20, "bold"), text="Update Expenditure").pack()

        InfoFrame = Frame(update_window)
        InfoFrame.place(x=0, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Enter Info")
        infoFrame.grid(row=0, column=0)

        expenditure_ID_label = Label(infoFrame, font=("", 15), text="Enter Expenditure ID", height=1)
        expenditure_ID_label.grid(row=1, column=0)
        expenditure_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        expenditure_ID_entry.grid(row=1, column=1)

        payee_label = Label(infoFrame, font=("", 15), text="Enter Payee Name", height=1)
        payee_label.grid(row=2, column=0)
        payee_entry = Entry(infoFrame, font=("", 15), width=18)
        payee_entry.grid(row=2, column=1)

        committee_ID_label = Label(infoFrame, font=("", 15), text="Enter Committee ID", height=1)
        committee_ID_label.grid(row=3, column=0)
        committee_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        committee_ID_entry.grid(row=3, column=1)

        amount_label = Label(infoFrame, font=("", 15), text="Enter Amount", height=1)
        amount_label.grid(row=4, column=0)
        amount_entry = Entry(infoFrame, font=("", 15), width=18)
        amount_entry.grid(row=4, column=1)

        purpose_label = Label(infoFrame, font=("", 15), text="Enter Purpose", height=1)
        purpose_label.grid(row=5, column=0)
        purpose_entry = Entry(infoFrame, font=("", 15), width=18)
        purpose_entry.grid(row=5, column=1)

        date_label = Label(infoFrame, font=("", 15), text="Enter Date", height=1)
        date_label.grid(row=6, column=0)
        date_entry = Entry(infoFrame, font=("", 15), width=18)
        date_entry.grid(row=6, column=1)

        SubmitFrame = Frame(update_window)
        SubmitFrame.place(x=0, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        update_window.grab_set()

    def expenditure_delete_window():
        def submit_query():
            expenditureID = expenditure_ID_entry.get()
            delete_query = "DELETE FROM Expenditure WHERE ExpenditureID = %s;"
            cursor.execute(delete_query, (expenditureID,))
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Deleted Successfully")

        delete_window = Toplevel(window)
        delete_window.title("Expenditure Delete")
        delete_window.geometry("400x300")
        Label(delete_window, font=("", 20, "bold"), text="Delete Expenditure").pack()

        InfoFrame = Frame(delete_window)
        InfoFrame.place(x=0, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Enter Info")
        infoFrame.grid(row=0, column=0)

        expenditure_ID_label = Label(infoFrame, font=("", 15), text="Enter Expenditure ID", height=1)
        expenditure_ID_label.grid(row=1, column=0)
        expenditure_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        expenditure_ID_entry.grid(row=1, column=1)

        SubmitFrame = Frame(delete_window)
        SubmitFrame.place(x=0, y=150, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        delete_window.grab_set()

        # ==================== (Expenditure) Set Operations: UNION ====================
    def setOpExp():
        def submit_query():
            insert_query = """
                            SELECT Payee FROM Expenditure WHERE Purpose = %s
                            UNION
                            SELECT Payee FROM Expenditure WHERE Purpose = %s;
                            """
            opElection_data = (opElection_X_entry.get(), opElection_Y_entry.get())
            cursor.execute(insert_query, opElection_data)
            rows = cursor.fetchall()
            if len(rows) != 0:
                opElection_table.delete(*opElection_table.get_children())
                for row in rows:
                    opElection_table.insert("", END, values=row)

        
        # ==================== Main setOp Expenditure Window ====================
        opElection_window = Toplevel(window)
        opElection_window.title("(Expenditure Table) Set Operations: UNION")
        opElection_window.geometry("900x500")
        Label(opElection_window, font=("", 20, "bold"), text="Set Operations Expenditure Table (UNION)").pack()
        opElection_window.grab_set()
        
        # UNION text label
        #label1 = Label(opElection_window, font=("", 9), text="UNION of states involved in x and y elections")
        #label1.place(x=150, y=50)  # Positioning the label widget

        # Insert UNION info frame 
        InfoFrame = Frame(opElection_window)
        InfoFrame.place(x=175, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Insert info")
        infoFrame.grid(row=0, column=0)

        opElection_X_label = Label(infoFrame, font=("", 15), text="Enter Purpose X: ", height=1)
        opElection_X_label.grid(row=1, column=0)
        opElection_X_entry = Entry(infoFrame, font=("", 15), width=18)
        opElection_X_entry.grid(row=1, column=1)

        opElection_Y_label = Label(infoFrame, font=("", 15), text="Enter Purpose Y: ", height=1)
        opElection_Y_label.grid(row=2, column=0)
        opElection_Y_entry = Entry(infoFrame, font=("", 15), width=18)
        opElection_Y_entry.grid(row=2, column=1)

        # Query info
        label1 = Label(opElection_window, font=("", 9), text= """ Query Info: 
Using UNION to get distinct Payees who have received expenditures for either X or Y purposes.
Example input: X = Advertising, Y = Office Rent""")
        label1.place(x=175, y=150)  # Positioning the label widget

        # Submit button
        SubmitFrame = Frame(opElection_window)
        SubmitFrame.place(x=175, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        # ==================== Table Result Info Frame ====================
        InfoFrame = Frame(opElection_window)
        InfoFrame.place(x=10, y=50, height=700, width=150)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Result")
        infoFrame.grid(row=0, column=0)

        scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
        opElection_table = ttk.Treeview(infoFrame, columns=("Payee"),
                                    yscrollcommand=scroll_y.set, height=18)

        opElection_table.column("#0", width=100)
        opElection_table.column("Payee", anchor=CENTER, width=100)

        opElection_table.heading("Payee", text="Payee")

        opElection_table["show"] = "headings"

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y = ttk.Scrollbar(command=opElection_table.yview)

        opElection_table.pack(fill=BOTH, expand=1)
    
    # ==================== (Expenditure) Set Membership: IN ====================  
    def setMemExp():
        def submit_query():
            insert_query = """
                            SELECT CASE 
                                    WHEN %s IN (
                                        SELECT Payee
                                        FROM Expenditure
                                        WHERE CommitteeID = %s
                                    ) THEN 'Exists'
                                    ELSE 'Not Found'
                                END AS PayeeExpenditureStatus;
                            """
            memElection_data = (memElection_X_entry.get(), memElection_Y_entry.get())
            cursor.execute(insert_query, memElection_data)
            rows = cursor.fetchall()
            if len(rows) != 0:
                memElection_table.delete(*memElection_table.get_children())
                for row in rows:
                    memElection_table.insert("", END, values=row)

        
        # ==================== Main setMem Expenditure Window ====================
        memElection_window = Toplevel(window)
        memElection_window.title("(Expenditure Table) Set Membership: IN")
        memElection_window.geometry("900x500")
        Label(memElection_window, font=("", 20, "bold"), text="Set Membership Expenditure Table (IN)").pack()
        memElection_window.grab_set()

        # Insert IN info frame 
        InfoFrame = Frame(memElection_window)
        InfoFrame.place(x=225, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Insert info")
        infoFrame.grid(row=0, column=0)

        memElection_X_label = Label(infoFrame, font=("", 15), text="Enter Payee name X: ", height=1)
        memElection_X_label.grid(row=1, column=0)
        memElection_X_entry = Entry(infoFrame, font=("", 15), width=18)
        memElection_X_entry.grid(row=1, column=1)

        memElection_Y_label = Label(infoFrame, font=("", 15), text="Enter Committee ID Y: ", height=1)
        memElection_Y_label.grid(row=2, column=0)
        memElection_Y_entry = Entry(infoFrame, font=("", 15), width=18)
        memElection_Y_entry.grid(row=2, column=1)

        # Query info
        label1 = Label(memElection_window, font=("", 9), text= """ Query Info: 
Checks if Payee X has received an expenditure from committee ID Y.
Example input: X = David Johnson, Y = 7""")
        label1.place(x=215, y=150)  # Positioning the label widget

        # Submit button
        SubmitFrame = Frame(memElection_window)
        SubmitFrame.place(x=225, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        # ==================== Table Result Info Frame ====================
        InfoFrame = Frame(memElection_window)
        InfoFrame.place(x=10, y=50, height=700, width=150)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Result")
        infoFrame.grid(row=0, column=0)

        scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
        memElection_table = ttk.Treeview(infoFrame, columns=("Result"),
                                    yscrollcommand=scroll_y.set, height=18)

        memElection_table.column("#0", width=100)
        memElection_table.column("Result", anchor=CENTER, width=100)

        memElection_table.heading("Result", text="Result")

        memElection_table["show"] = "headings"

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y = ttk.Scrollbar(command=memElection_table.yview)

        memElection_table.pack(fill=BOTH, expand=1)


    # ==================== (Expenditure) Set Comparison: ANY ====================  
    def setCompExp():
        def submit_query():
            insert_query = """
                            SELECT *
                            FROM Expenditure
                            WHERE Amount > ANY (
                                SELECT Amount FROM Expenditure WHERE Purpose = %s
                            );
                            """
            comElection_data = (comElection_X_entry.get(),)
            cursor.execute(insert_query, comElection_data)
            rows = cursor.fetchall()
            if len(rows) != 0:
                comElection_table.delete(*comElection_table.get_children())
                for row in rows:
                    comElection_table.insert("", END, values=row)

        
        # ==================== Main setCom Election Window ====================
        comElection_window = Toplevel(window)
        comElection_window.title("(Expenditure Table) Set Comparison: ANY")
        comElection_window.geometry("1100x500")
        Label(comElection_window, font=("", 20, "bold"), text="Set Comparison Expenditure Table (ANY)").pack()
        comElection_window.grab_set()

        # Insert ANY info frame 
        InfoFrame = Frame(comElection_window)
        InfoFrame.place(x=650, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Insert info")
        infoFrame.grid(row=0, column=0)

        comElection_X_label = Label(infoFrame, font=("", 15), text="Enter Purpose X: ", height=1)
        comElection_X_label.grid(row=1, column=0)
        comElection_X_entry = Entry(infoFrame, font=("", 15), width=18)
        comElection_X_entry.grid(row=1, column=1)

        # Query info
        label1 = Label(comElection_window, font=("", 9), text= """ Query Info: 
Using the ANY operator to compare expenditures based on Amount for a specific purpose.
Returns all expenditures with an amount greater than the expenditure with purpose X.
Example input: X = Consulting fees""")
        label1.place(x=635, y=150)  # Positioning the label widget

        # Submit button
        SubmitFrame = Frame(comElection_window)
        SubmitFrame.place(x=650, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        # ==================== Table Result Info Frame ====================
        InfoFrame = Frame(comElection_window)
        InfoFrame.place(x=10, y=50, height=700, width=625)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Result")
        infoFrame.grid(row=0, column=0)

        scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
        comElection_table = ttk.Treeview(infoFrame, columns=("ExpenditureID", "Payee", "CommitteeID", "Amount", "Purpose", "Date"),
                                    yscrollcommand=scroll_y.set, height=18)

        comElection_table.column("#0", width=100)
        comElection_table.column("ExpenditureID", anchor=CENTER, width=100)
        comElection_table.column("Payee", anchor=W, width=125)
        comElection_table.column("CommitteeID", anchor=CENTER, width=100)
        comElection_table.column("Amount", anchor=CENTER, width=60)
        comElection_table.column("Purpose", anchor=CENTER, width=100)
        comElection_table.column("Date", anchor=CENTER, width=100)

        comElection_table.heading("ExpenditureID", text="Expenditure ID")
        comElection_table.heading("Payee", text="Payee")
        comElection_table.heading("CommitteeID", text="Committee ID")
        comElection_table.heading("Amount", text="Amount")
        comElection_table.heading("Purpose", text="Purpose")
        comElection_table.heading("Date", text="Date")

        comElection_table["show"] = "headings"

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y = ttk.Scrollbar(command=comElection_table.yview)

        comElection_table.pack(fill=BOTH, expand=1)

    # ==================== (Expenditure) Calculate the Average Elections ====================  
    def calcAvgExp():
        def fetch_data():
            insert_query = """
                            SELECT ExpenditureID, Payee, CommitteeID, Amount, Purpose, Date,
                                ROUND(AVG(Amount) OVER (PARTITION BY CommitteeID ORDER BY Date 
                                                    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW), 2) AS RunningAvgAmount
                            FROM Expenditure
                            ORDER BY CommitteeID, Date;
                            """
            cursor.execute(insert_query)
            rows = cursor.fetchall()
            if len(rows) != 0:
                calcCumElection_table.delete(*calcCumElection_table.get_children())
                for row in rows:
                    calcCumElection_table.insert("", END, values=row)

        
        # ==================== Main calAvg Election Window ====================
        calcCumElection_window = Toplevel(window)
        calcCumElection_window.title("(Expenditure Table) Advanced Aggregate Functions: WINDOW Functions")
        calcCumElection_window.geometry("900x500")
        Label(calcCumElection_window, font=("", 20, "bold"), text="Calculate the Average Expenditure Table (AVG)").pack()
        calcCumElection_window.grab_set()

        # ==================== Table Result Info Frame ====================
        InfoFrame = Frame(calcCumElection_window)
        InfoFrame.place(x=50, y=50, height=700, width=720)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Result")
        infoFrame.grid(row=0, column=0)

        # Query info
        label1 = Label(calcCumElection_window, font=("", 9), text= """ Query Info: 
Calculates the running average of the Amount spent by each Committee over time.""")
        label1.place(x=225, y=450)  # Positioning the label widget

        scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
        calcCumElection_table = ttk.Treeview(infoFrame, columns=("ExpenditureID", "Payee", "CommitteeID", "Amount", "Purpose", "Date", "RunningAvgAmount"),
                                    yscrollcommand=scroll_y.set, height=18)

        calcCumElection_table.column("#0", width=100)
        calcCumElection_table.column("ExpenditureID", anchor=CENTER, width=80)
        calcCumElection_table.column("Payee", anchor=CENTER, width=110)
        calcCumElection_table.column("CommitteeID", anchor=CENTER, width=75)
        calcCumElection_table.column("Amount", anchor=CENTER, width=60)
        calcCumElection_table.column("Purpose", anchor=CENTER, width=140)
        calcCumElection_table.column("Date", anchor=CENTER, width=100)
        calcCumElection_table.column("RunningAvgAmount", anchor=CENTER, width=120)


        calcCumElection_table.heading("ExpenditureID", text="Expenditure ID")
        calcCumElection_table.heading("Payee", text="Payee")
        calcCumElection_table.heading("CommitteeID", text="Committee ID")
        calcCumElection_table.heading("Amount", text="Amount")
        calcCumElection_table.heading("Purpose", text="Purpose")
        calcCumElection_table.heading("Date", text="Date")
        calcCumElection_table.heading("RunningAvgAmount", text="Running Avg Amount")
        
        calcCumElection_table["show"] = "headings"

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y = ttk.Scrollbar(command=calcCumElection_table.yview)

        calcCumElection_table.pack(fill=BOTH, expand=1)
        fetch_data()
    
    # ==================== (Expenditure) Subqueries using the WITH Clause ====================  
    def withClauseExp():
        def submit_query():
            insert_query = """
                            WITH LargeExpenditures AS (
                                SELECT * FROM Expenditure WHERE Amount > %s
                            )
                            SELECT * FROM LargeExpenditures WHERE Purpose = %s;
                            """
            withClauseElection_data = (withClauseElection_X_entry.get(), withClauseElection_Y_entry.get())
            cursor.execute(insert_query, withClauseElection_data)
            rows = cursor.fetchall()
            if len(rows) != 0:
                withClauseElection_table.delete(*withClauseElection_table.get_children())
                for row in rows:
                    withClauseElection_table.insert("", END, values=row)

        
        # ==================== Main withClause Expenditure Window ====================
        withClauseElection_window = Toplevel(window)
        withClauseElection_window.title("(Expenditure Table) Subqueries using the WITH Clause")
        withClauseElection_window.geometry("1100x500")
        Label(withClauseElection_window, font=("", 20, "bold"), text="Subqueries using the WITH Clause").pack()
        withClauseElection_window.grab_set()

        # Insert info frame 
        InfoFrame = Frame(withClauseElection_window)
        InfoFrame.place(x=700, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 10, "bold"), text="Insert Info")
        infoFrame.grid(row=0, column=0)

        withClauseElection_X_label = Label(infoFrame, font=("", 15), text="Enter Amount X: ", height=1)
        withClauseElection_X_label.grid(row=1, column=0)
        withClauseElection_X_entry = Entry(infoFrame, font=("", 15), width=18)
        withClauseElection_X_entry.grid(row=1, column=1)

        withClauseElection_Y_label = Label(infoFrame, font=("", 15), text="Enter Purpose Y: ", height=1)
        withClauseElection_Y_label.grid(row=2, column=0)
        withClauseElection_Y_entry = Entry(infoFrame, font=("", 15), width=18)
        withClauseElection_Y_entry.grid(row=2, column=1)

        # Query info
        label1 = Label(withClauseElection_window, font=("", 9), text= """ Query Info: 
This query uses a Common Table Expression (CTE) find all expenditures over a certain amount, 
then selecting those with a specific purpose. 
Example input: X = 1500, Y = Security""")
        label1.place(x=675, y=150)  # Positioning the label widget

        # Submit button
        SubmitFrame = Frame(withClauseElection_window)
        SubmitFrame.place(x=700, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        # ==================== Table Result Info Frame ====================
        InfoFrame = Frame(withClauseElection_window)
        InfoFrame.place(x=10, y=50, height=700, width=650)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Result")
        infoFrame.grid(row=0, column=0)

        scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
        withClauseElection_table = ttk.Treeview(infoFrame, columns=("ExenditureID", "Payee", "CommitteeID", "Amount", "Purpose", "Date"),
                                    yscrollcommand=scroll_y.set, height=18)

        withClauseElection_table.column("#0", width=100)
        withClauseElection_table.column("ExenditureID", anchor=CENTER, width=100)
        withClauseElection_table.column("Payee", anchor=W, width=125)
        withClauseElection_table.column("CommitteeID", anchor=CENTER, width=100)
        withClauseElection_table.column("Amount", anchor=CENTER, width=100)
        withClauseElection_table.column("Purpose", anchor=CENTER, width=100)
        withClauseElection_table.column("Date", anchor=CENTER, width=100)

        withClauseElection_table.heading("ExenditureID", text="Expenditure ID")
        withClauseElection_table.heading("Payee", text="Payee")
        withClauseElection_table.heading("CommitteeID", text="Committee ID")
        withClauseElection_table.heading("Amount", text="Amount")
        withClauseElection_table.heading("Purpose", text="Purpose")
        withClauseElection_table.heading("Date", text="Date")

        withClauseElection_table["show"] = "headings"

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y = ttk.Scrollbar(command=withClauseElection_table.yview)

        withClauseElection_table.pack(fill=BOTH, expand=1)

    
    # ==================== Main Expenditure Window ====================
    expenditure_window = Toplevel(window)
    expenditure_window.title("Expenditure Table")
    expenditure_window.geometry("1000x500")
    Label(expenditure_window, font=("", 20, "bold"), text="Expenditure").pack()
    expenditure_window.grab_set()
    # ==================== Actions Frame ====================
    ActionFrame = Frame(expenditure_window)
    ActionFrame.place(x=725, y=50, height=500, width=500)
    actionFrame = LabelFrame(ActionFrame, font=("", 15, "bold"), text="Select an action")
    actionFrame.grid(row=0, column=0)

    insert_button = Button(actionFrame, text="Insert Data", font=("", 15), width=10, height=1,
                           command=expenditure_insert_window)
    insert_button.grid(row=1, column=0)

    update_button = Button(actionFrame, text="Update Data", font=("", 15), width=10, height=1,
                           command=expenditure_update_window)
    update_button.grid(row=2, column=0)

    delete_button = Button(actionFrame, text="Delete Data", font=("", 15), width=10, height=1,
                           command=expenditure_delete_window)
    delete_button.grid(row=3, column=0)

    setOP_button = Button(actionFrame, text="Set Operations", font=("", 15), width=10, height=1,
                           command= setOpExp)
    setOP_button.grid(row=4, column=0)

    setMem_button = Button(actionFrame, text="Set Membership", font=("", 15), width=10, height=1,
                           command= setMemExp)
    setMem_button.grid(row=5, column=0)

    setCom_button = Button(actionFrame, text="Set Comparison", font=("", 15), width=10, height=1,
                           command= setCompExp)
    setCom_button.grid(row=6, column=0)

    calCum_button = Button(actionFrame, text="Calculate Average", font=("", 15), width=15, height=1,
                           command= calcAvgExp)
    calCum_button.grid(row=7, column=0)

    withClause_button = Button(actionFrame, text="Subqueries using the WITH Clause", font=("", 15), width=23, height=1,
                           command= withClauseExp)
    withClause_button.grid(row=8, column=0)

    # ==================== Table Info Frame ====================
    InfoFrame = Frame(expenditure_window)
    InfoFrame.place(x=0, y=50, height=700, width=700)
    infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Expenditure Info")
    infoFrame.grid(row=0, column=0)

    scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
    expenditure_table = ttk.Treeview(infoFrame, columns=("expenditureID", "payee", "committeeID",
                                                         "amount", "purpose", "date"),
                                     yscrollcommand=scroll_y, height=18)

    expenditure_table.column("#0", width=100)
    expenditure_table.column("expenditureID", anchor=W, width=100)
    expenditure_table.column("payee", anchor=W, width=100)
    expenditure_table.column("committeeID", anchor=W, width=100)
    expenditure_table.column("amount", anchor=W, width=100)
    expenditure_table.column("purpose", anchor=W, width=100)
    expenditure_table.column("date", anchor=W, width=100)

    expenditure_table.heading("expenditureID", text="Expenditure ID")
    expenditure_table.heading("payee", text="Payee")
    expenditure_table.heading("committeeID", text="Committee ID")
    expenditure_table.heading("amount", text="Amount")
    expenditure_table.heading("purpose", text="Purpose")
    expenditure_table.heading("date", text="Date")

    expenditure_table["show"] = "headings"

    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_y = ttk.Scrollbar(command=expenditure_table.yview)

    expenditure_table.pack(fill=BOTH, expand=1)

    fetch_data()


# ==================== Filing Window ====================
def open_filing_window():
    #function to show everything in the table
    def fetch_data():
        cursor.execute("SELECT * FROM filing")
        rows = cursor.fetchall()
        if len(rows) != 0:
            filing_table.delete(*filing_table.get_children())
            for row in rows:
                filing_table.insert("", END, values=row)
            connection.commit()

    #function to highlight a row that you click on
    def get_cursor():
        cursor_row = filing_table.focus()

    # ==================== Button Windows ====================
    def filing_insert_window():
        def submit_query():
            insert_query = "INSERT INTO Filing (FilingID, ReportType, ReportPeriod, DateFiled, CommitteeID) VALUES (%s, %s, %s, %s, %s)"
            filing_data = (filing_ID_entry.get(), report_type_entry.get(), report_period_entry.get(),
                           date_filed_entry.get(), committee_ID_entry.get())
            cursor.execute(insert_query, filing_data)
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Inserted Successfully")

        insert_window = Toplevel(window)
        insert_window.title("Filing Insert")
        insert_window.geometry("500x400")
        Label(insert_window, font=("", 20, "bold"), text="Insert Filing").pack()

        InfoFrame = Frame(insert_window)
        InfoFrame.place(x=0, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Enter Info")
        infoFrame.grid(row=0, column=0)

        filing_ID_label = Label(infoFrame, font=("", 15), text="Enter Filing ID", height=1)
        filing_ID_label.grid(row=1, column=0)
        filing_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        filing_ID_entry.grid(row=1, column=1)

        report_type_label = Label(infoFrame, font=("", 15), text="Enter Report Type", height=1)
        report_type_label.grid(row=2, column=0)
        report_type_entry = Entry(infoFrame, font=("", 15), width=18)
        report_type_entry.grid(row=2, column=1)

        report_period_label = Label(infoFrame, font=("", 15), text="Enter Report Period", height=1)
        report_period_label.grid(row=3, column=0)
        report_period_entry = Entry(infoFrame, font=("", 15), width=18)
        report_period_entry.grid(row=3, column=1)

        date_filed_label = Label(infoFrame, font=("", 15), text="Enter Date", height=1)
        date_filed_label.grid(row=4, column=0)
        date_filed_entry = Entry(infoFrame, font=("", 15), width=18)
        date_filed_entry.grid(row=4, column=1)

        committee_ID_label = Label(infoFrame, font=("", 15), text="Enter Committee ID", height=1)
        committee_ID_label.grid(row=5, column=0)
        committee_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        committee_ID_entry.grid(row=5, column=1)

        SubmitFrame = Frame(insert_window)
        SubmitFrame.place(x=0, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        insert_window.grab_set()

    def filing_update_window():
        def submit_query():
            update_query = """
                    UPDATE Filing
                    SET ReportType = %s, 
                        ReportPeriod = %s, 
                        DateFiled = %s,
                        CommitteeID = %s
                    WHERE FilingID = %s;
            """
            cursor.execute(update_query, (report_type_entry.get(), report_period_entry.get(), date_filed_entry.get(),
                                          committee_ID_entry.get(), filing_ID_entry.get()))
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Updated Successfully")

        update_window = Toplevel(window)
        update_window.title("Filing Update")
        update_window.geometry("500x400")
        Label(update_window, font=("", 20, "bold"), text="Update Filing").pack()

        InfoFrame = Frame(update_window)
        InfoFrame.place(x=0, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Enter Info")
        infoFrame.grid(row=0, column=0)

        filing_ID_label = Label(infoFrame, font=("", 15), text="Enter Filing ID", height=1)
        filing_ID_label.grid(row=1, column=0)
        filing_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        filing_ID_entry.grid(row=1, column=1)

        report_type_label = Label(infoFrame, font=("", 15), text="Enter Report Type", height=1)
        report_type_label.grid(row=2, column=0)
        report_type_entry = Entry(infoFrame, font=("", 15), width=18)
        report_type_entry.grid(row=2, column=1)

        report_period_label = Label(infoFrame, font=("", 15), text="Enter Report Period", height=1)
        report_period_label.grid(row=3, column=0)
        report_period_entry = Entry(infoFrame, font=("", 15), width=18)
        report_period_entry.grid(row=3, column=1)

        date_filed_label = Label(infoFrame, font=("", 15), text="Enter Date", height=1)
        date_filed_label.grid(row=4, column=0)
        date_filed_entry = Entry(infoFrame, font=("", 15), width=18)
        date_filed_entry.grid(row=4, column=1)

        committee_ID_label = Label(infoFrame, font=("", 15), text="Enter Committee ID", height=1)
        committee_ID_label.grid(row=5, column=0)
        committee_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        committee_ID_entry.grid(row=5, column=1)

        SubmitFrame = Frame(update_window)
        SubmitFrame.place(x=0, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        update_window.grab_set()

    def filing_delete_window():
        def submit_query():
            filingID = filing_ID_entry.get()
            delete_query = "DELETE FROM Filing WHERE FilingID = %s;"
            cursor.execute(delete_query, (filingID,))
            connection.commit()

            fetch_data()

            messagebox.showinfo("Success", "Data Deleted Successfully")

        delete_window = Toplevel(window)
        delete_window.title("Filing Delete")
        delete_window.geometry("400x300")
        Label(delete_window, font=("", 20, "bold"), text="Delete Filing").pack()

        InfoFrame = Frame(delete_window)
        InfoFrame.place(x=0, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Enter Info")
        infoFrame.grid(row=0, column=0)

        filing_ID_label = Label(infoFrame, font=("", 15), text="Enter Filing ID", height=1)
        filing_ID_label.grid(row=1, column=0)
        filing_ID_entry = Entry(infoFrame, font=("", 15), width=18)
        filing_ID_entry.grid(row=1, column=1)

        SubmitFrame = Frame(delete_window)
        SubmitFrame.place(x=0, y=150, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        delete_window.grab_set()

        # ==================== (Election) Set Operations: UNION ====================
    def setOpFil():
        def submit_query():
            insert_query = """
                            SELECT DateFiled FROM Filing WHERE CommitteeID = %s
                            UNION
                            SELECT DateFiled FROM Filing WHERE CommitteeID = %s;
                            """
            opElection_data = (opElection_X_entry.get(), opElection_Y_entry.get())
            cursor.execute(insert_query, opElection_data)
            rows = cursor.fetchall()
            if len(rows) != 0:
                opElection_table.delete(*opElection_table.get_children())
                for row in rows:
                    opElection_table.insert("", END, values=row)

        
        # ==================== Main setOp Filing Window ====================
        opElection_window = Toplevel(window)
        opElection_window.title("(Filing Table) Set Operations: UNION")
        opElection_window.geometry("900x500")
        Label(opElection_window, font=("", 20, "bold"), text="Set Operations Filing Table (UNION)").pack()
        opElection_window.grab_set()
        
        # UNION text label
        #label1 = Label(opElection_window, font=("", 9), text="UNION of states involved in x and y elections")
        #label1.place(x=150, y=50)  # Positioning the label widget

        # Insert UNION info frame 
        InfoFrame = Frame(opElection_window)
        InfoFrame.place(x=175, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Insert info")
        infoFrame.grid(row=0, column=0)

        opElection_X_label = Label(infoFrame, font=("", 15), text="Enter Committee ID X: ", height=1)
        opElection_X_label.grid(row=1, column=0)
        opElection_X_entry = Entry(infoFrame, font=("", 15), width=18)
        opElection_X_entry.grid(row=1, column=1)

        opElection_Y_label = Label(infoFrame, font=("", 15), text="Enter Committee ID Y: ", height=1)
        opElection_Y_label.grid(row=2, column=0)
        opElection_Y_entry = Entry(infoFrame, font=("", 15), width=18)
        opElection_Y_entry.grid(row=2, column=1)

        # Query info
        label1 = Label(opElection_window, font=("", 9), text= """ Query Info: 
Finds UNION filed dates by both committee X and Y.
Example input: X = Senate Election, Y = Governor Election""")
        label1.place(x=175, y=150)  # Positioning the label widget

        # Submit button
        SubmitFrame = Frame(opElection_window)
        SubmitFrame.place(x=175, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        # ==================== Table Result Info Frame ====================
        InfoFrame = Frame(opElection_window)
        InfoFrame.place(x=10, y=50, height=700, width=150)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Result")
        infoFrame.grid(row=0, column=0)

        scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
        opElection_table = ttk.Treeview(infoFrame, columns=("DateFiled"),
                                    yscrollcommand=scroll_y.set, height=18)

        opElection_table.column("#0", width=100)
        opElection_table.column("DateFiled", anchor=CENTER, width=100)

        opElection_table.heading("DateFiled", text="Date Filed")

        opElection_table["show"] = "headings"

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y = ttk.Scrollbar(command=opElection_table.yview)

        opElection_table.pack(fill=BOTH, expand=1)
    
    # ==================== (Filing) Set Membership: EXISTS ====================  
    def setMemFil():
        def submit_query():
            insert_query = """
                            SELECT CASE 
                            WHEN EXISTS (
                                SELECT 1
                                FROM Filing
                                WHERE ReportPeriod = %s
                                ) THEN 'Exists'
                            ELSE NULL
                            END AS Result;
                            """
            memElection_data = (memElection_X_entry.get(),)
            cursor.execute(insert_query, memElection_data)
            rows = cursor.fetchall()
            if len(rows) != 0:
                memElection_table.delete(*memElection_table.get_children())
                for row in rows:
                    memElection_table.insert("", END, values=row)

        
        # ==================== Main setMem Filing Window ====================
        memElection_window = Toplevel(window)
        memElection_window.title("(Filing Table) Set Membership: EXISTS")
        memElection_window.geometry("900x500")
        Label(memElection_window, font=("", 20, "bold"), text="Set Membership Filing Table (EXISTS)").pack()
        memElection_window.grab_set()

        # Insert info frame 
        InfoFrame = Frame(memElection_window)
        InfoFrame.place(x=225, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Insert info")
        infoFrame.grid(row=0, column=0)

        memElection_X_label = Label(infoFrame, font=("", 15), text="Enter Report Period X: ", height=1)
        memElection_X_label.grid(row=1, column=0)
        memElection_X_entry = Entry(infoFrame, font=("", 15), width=18)
        memElection_X_entry.grid(row=1, column=1)

        # Query info
        label1 = Label(memElection_window, font=("", 9), text= """ Query Info: 
checks if there's a filing for a specific period from any committee
Example input: X = Q1 2023""")
        label1.place(x=215, y=150)  # Positioning the label widget


        # Submit button
        SubmitFrame = Frame(memElection_window)
        SubmitFrame.place(x=225, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        # ==================== Table Result Info Frame ====================
        InfoFrame = Frame(memElection_window)
        InfoFrame.place(x=10, y=50, height=700, width=150)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Result")
        infoFrame.grid(row=0, column=0)

        scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
        memElection_table = ttk.Treeview(infoFrame, columns=("Result"),
                                    yscrollcommand=scroll_y.set, height=18)

        memElection_table.column("#0", width=100)
        memElection_table.column("Result", anchor=CENTER, width=60)

        memElection_table.heading("Result", text="Result")

        memElection_table["show"] = "headings"

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y = ttk.Scrollbar(command=memElection_table.yview)

        memElection_table.pack(fill=BOTH, expand=1)


    # ==================== (Filing) Set Comparison: ANY ====================  
    def setCompFil():
        def submit_query():
            insert_query = """
                                SELECT *
                                FROM Filing
                                WHERE DateFiled > ANY (
                                    SELECT DateFiled FROM Filing WHERE ReportPeriod = %s
                                );
                            """
            comElection_data = (comElection_X_entry.get(),)
            cursor.execute(insert_query, comElection_data)
            rows = cursor.fetchall()
            if len(rows) != 0:
                comElection_table.delete(*comElection_table.get_children())
                for row in rows:
                    comElection_table.insert("", END, values=row)

        
        # ==================== Main setCom Filing Window ====================
        comElection_window = Toplevel(window)
        comElection_window.title("(Filing Table) Set Comparison: ANY")
        comElection_window.geometry("900x500")
        Label(comElection_window, font=("", 20, "bold"), text="Set Comparison Filing Table (ANY)").pack()
        comElection_window.grab_set()

        # Insert info frame 
        InfoFrame = Frame(comElection_window)
        InfoFrame.place(x=525, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Insert info")
        infoFrame.grid(row=0, column=0)

        comElection_X_label = Label(infoFrame, font=("", 15), text="Enter Report Period X: ", height=1)
        comElection_X_label.grid(row=1, column=0)
        comElection_X_entry = Entry(infoFrame, font=("", 15), width=18)
        comElection_X_entry.grid(row=1, column=1)

        # Query info
        label1 = Label(comElection_window, font=("", 9), text= """ Query Info: 
Finds all filings that were filed later than the first filing of X.
Example input: X = Q1 2023""")
        label1.place(x=550, y=150)  # Positioning the label widget

        # Submit button
        SubmitFrame = Frame(comElection_window)
        SubmitFrame.place(x=525, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        # ==================== Table Result Info Frame ====================
        InfoFrame = Frame(comElection_window)
        InfoFrame.place(x=10, y=50, height=700, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Result")
        infoFrame.grid(row=0, column=0)

        scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
        comElection_table = ttk.Treeview(infoFrame, columns=("FilingID", "ReportType", "ReportPeriod", "DateFiled", "CommitteeID"),
                                    yscrollcommand=scroll_y.set, height=18)

        comElection_table.column("#0", width=100)
        comElection_table.column("FilingID", anchor=CENTER, width=100)
        comElection_table.column("ReportType", anchor=W, width=125)
        comElection_table.column("ReportPeriod", anchor=CENTER, width=100)
        comElection_table.column("DateFiled", anchor=CENTER, width=60)
        comElection_table.column("CommitteeID", anchor=CENTER, width=90)

        comElection_table.heading("FilingID", text="Filing ID")
        comElection_table.heading("ReportType", text="Report Type")
        comElection_table.heading("ReportPeriod", text="Report Period")
        comElection_table.heading("DateFiled", text="Date Filed")
        comElection_table.heading("CommitteeID", text="Committee ID")

        comElection_table["show"] = "headings"

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y = ttk.Scrollbar(command=comElection_table.yview)

        comElection_table.pack(fill=BOTH, expand=1)

    # ==================== (Filing) Calculate Cumulative Filing ====================  
    def calcCumFil():
        def fetch_data():
            insert_query = """
                            SELECT FilingID, ReportType, ReportPeriod, DateFiled, CommitteeID,
                                COUNT(*) OVER (PARTITION BY CommitteeID ORDER BY DateFiled) AS CumulativeFilings
                            FROM Filing
                            ORDER BY CommitteeID, DateFiled;
                            """
            cursor.execute(insert_query)
            rows = cursor.fetchall()
            if len(rows) != 0:
                calcCumElection_table.delete(*calcCumElection_table.get_children())
                for row in rows:
                    calcCumElection_table.insert("", END, values=row)

        
        # ==================== Main calCum Filing Window ====================
        calcCumElection_window = Toplevel(window)
        calcCumElection_window.title("(Filing Table) Advanced Aggregate Functions: WINDOW Functions")
        calcCumElection_window.geometry("900x500")
        Label(calcCumElection_window, font=("", 20, "bold"), text="Calculate Cumulative Filing Table (COUNT)").pack()
        calcCumElection_window.grab_set()

        # ==================== Table Result Info Frame ====================
        InfoFrame = Frame(calcCumElection_window)
        InfoFrame.place(x=150, y=50, height=700, width=550)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Result")
        infoFrame.grid(row=0, column=0)

        # Query info
        label1 = Label(calcCumElection_window, font=("", 9), text= """ Query Info: 
Calculates the cumulative number of filings made by each committee.""")
        label1.place(x=275, y=450)  # Positioning the label widget

        scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
        calcCumElection_table = ttk.Treeview(infoFrame, columns=("FilingID", "ReportType", "ReportPeriod", "DateFiled", "CommitteeID", "FilingRank"),
                                    yscrollcommand=scroll_y.set, height=18)

        calcCumElection_table.column("#0", width=100)
        calcCumElection_table.column("FilingID", anchor=CENTER, width=60)
        calcCumElection_table.column("ReportType", anchor=CENTER, width=100)
        calcCumElection_table.column("ReportPeriod", anchor=CENTER, width=100)
        calcCumElection_table.column("DateFiled", anchor=CENTER, width=90)
        calcCumElection_table.column("CommitteeID", anchor=CENTER, width=80)
        calcCumElection_table.column("FilingRank", anchor=CENTER, width=70)

        calcCumElection_table.heading("FilingID", text="Filing ID")
        calcCumElection_table.heading("ReportType", text="Report Type")
        calcCumElection_table.heading("ReportPeriod", text="Report Period")
        calcCumElection_table.heading("DateFiled", text="Date Filed")
        calcCumElection_table.heading("CommitteeID", text="Committee ID")
        calcCumElection_table.heading("FilingRank", text="Filing Rank")
        

        calcCumElection_table["show"] = "headings"

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y = ttk.Scrollbar(command=calcCumElection_table.yview)

        calcCumElection_table.pack(fill=BOTH, expand=1)
        fetch_data()
    
    # ==================== (Filing) Subqueries using the WITH Clause ====================  
    def withClauseFil():
        def submit_query():
            insert_query = """
                            WITH Filings2023 AS (
                                SELECT * FROM Filing
                                WHERE ReportPeriod LIKE '%' %s
                            )
                            SELECT *
                            FROM Filings2023
                            WHERE CommitteeID = %s;
                            """
            withClauseElection_data = (withClauseElection_X_entry.get(), withClauseElection_Y_entry.get())
            cursor.execute(insert_query, withClauseElection_data)
            rows = cursor.fetchall()
            if len(rows) != 0:
                withClauseElection_table.delete(*withClauseElection_table.get_children())
                for row in rows:
                    withClauseElection_table.insert("", END, values=row)

        
        # ==================== Main withClause Filing Window ====================
        withClauseElection_window = Toplevel(window)
        withClauseElection_window.title("(Filing Table) Subqueries using the WITH Clause")
        withClauseElection_window.geometry("950x500")
        Label(withClauseElection_window, font=("", 20, "bold"), text="Subqueries using the WITH Clause").pack()
        withClauseElection_window.grab_set()

        # Insert info frame 
        InfoFrame = Frame(withClauseElection_window)
        InfoFrame.place(x=525, y=50, height=500, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 10, "bold"), text="Insert Info")
        infoFrame.grid(row=0, column=0)

        withClauseElection_X_label = Label(infoFrame, font=("", 15), text="Enter the Report Period X: ", height=1)
        withClauseElection_X_label.grid(row=1, column=0)
        withClauseElection_X_entry = Entry(infoFrame, font=("", 15), width=18)
        withClauseElection_X_entry.grid(row=1, column=1)

        withClauseElection_Y_label = Label(infoFrame, font=("", 15), text="Enter the Committee ID Y: ", height=1)
        withClauseElection_Y_label.grid(row=2, column=0)
        withClauseElection_Y_entry = Entry(infoFrame, font=("", 15), width=18)
        withClauseElection_Y_entry.grid(row=2, column=1)

        # Query info
        label1 = Label(withClauseElection_window, font=("", 9), text= """ Query Info: 
This query uses a Common Table Expression (CTE) to get all filings for a specific period, 
then selecting those filed by a committee.
Example input: X = Q1 2023, Y = 1""")
        label1.place(x=525, y=150)  # Positioning the label widget

        # Submit button
        SubmitFrame = Frame(withClauseElection_window)
        SubmitFrame.place(x=525, y=300, height=250, width=250)
        submitFrame = LabelFrame(InfoFrame)
        submitFrame.grid(row=0, column=0)

        submit_button = Button(SubmitFrame, text="Submit", font=("", 15), width=10, command=submit_query)
        submit_button.grid(row=1, column=0)

        # ==================== Table Result Info Frame ====================
        InfoFrame = Frame(withClauseElection_window)
        InfoFrame.place(x=10, y=50, height=700, width=500)
        infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Result")
        infoFrame.grid(row=0, column=0)

        scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
        withClauseElection_table = ttk.Treeview(infoFrame, columns=("FilingID", "ReportType", "ReportPeriod", "DateFiled", "CommitteeID"),
                                    yscrollcommand=scroll_y.set, height=18)

        withClauseElection_table.column("#0", width=100)
        withClauseElection_table.column("FilingID", anchor=CENTER, width=100)
        withClauseElection_table.column("ReportType", anchor=W, width=100)
        withClauseElection_table.column("ReportPeriod", anchor=CENTER, width=100)
        withClauseElection_table.column("DateFiled", anchor=CENTER, width=90)
        withClauseElection_table.column("CommitteeID", anchor=CENTER, width=80)

        withClauseElection_table.heading("FilingID", text="Filing ID")
        withClauseElection_table.heading("ReportType", text="Report Type")
        withClauseElection_table.heading("ReportPeriod", text="Report Period")
        withClauseElection_table.heading("DateFiled", text="Date Filed")
        withClauseElection_table.heading("CommitteeID", text="Committee ID")

        withClauseElection_table["show"] = "headings"

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y = ttk.Scrollbar(command=withClauseElection_table.yview)

        withClauseElection_table.pack(fill=BOTH, expand=1)

    
    # ==================== Main Filing Window ====================
    filing_window = Toplevel(window)
    filing_window.title("Filing Table")
    filing_window.geometry("900x500")
    Label(filing_window, font=("", 20, "bold"), text="Filing").pack()
    filing_window.grab_set()

    # ==================== Actions Frame ====================
    ActionFrame = Frame(filing_window)
    ActionFrame.place(x=600, y=50, height=500, width=500)
    actionFrame = LabelFrame(ActionFrame, font=("", 15, "bold"), text="Select an action")
    actionFrame.grid(row=0, column=0)

    insert_button = Button(actionFrame, text="Insert Data", font=("", 15), width=10, height=1,
                           command=filing_insert_window)
    insert_button.grid(row=1, column=0)

    update_button = Button(actionFrame, text="Update Data", font=("", 15), width=10, height=1,
                           command=filing_update_window)
    update_button.grid(row=2, column=0)

    delete_button = Button(actionFrame, text="Delete Data", font=("", 15), width=10, height=1,
                           command=filing_delete_window)
    delete_button.grid(row=3, column=0)

    setOP_button = Button(actionFrame, text="Set Operations", font=("", 15), width=10, height=1,
                           command= setOpFil)
    setOP_button.grid(row=4, column=0)

    setMem_button = Button(actionFrame, text="Set Membership", font=("", 15), width=10, height=1,
                           command= setMemFil)
    setMem_button.grid(row=5, column=0)

    setCom_button = Button(actionFrame, text="Set Comparison", font=("", 15), width=10, height=1,
                           command= setCompFil)
    setCom_button.grid(row=6, column=0)

    calCum_button = Button(actionFrame, text="Calc. Cum. Elections", font=("", 15), width=15, height=1,
                           command= calcCumFil)
    calCum_button.grid(row=7, column=0)

    withClause_button = Button(actionFrame, text="Subqueries using the WITH Clause", font=("", 15), width=23, height=1,
                           command= withClauseFil)
    withClause_button.grid(row=8, column=0)

    # ==================== Table Info Frame ====================
    InfoFrame = Frame(filing_window)
    InfoFrame.place(x=0, y=50, height=500, width=600)
    infoFrame = LabelFrame(InfoFrame, font=("", 15, "bold"), text="Filing Info")
    infoFrame.grid(row=0, column=0)

    scroll_y = ttk.Scrollbar(infoFrame, orient=VERTICAL)
    filing_table = ttk.Treeview(infoFrame, columns=("filingID", "reportType", "reportPeriod",
                                                    "dateFiled", "committeeID"),
                                 yscrollcommand=scroll_y.set, height=18)

    filing_table.column("#0", width=100)
    filing_table.column("filingID", anchor=W, width=100)
    filing_table.column("reportType", anchor=W, width=100)
    filing_table.column("reportPeriod", anchor=W, width=100)
    filing_table.column("dateFiled", anchor=W, width=100)
    filing_table.column("committeeID", anchor=W, width=100)

    filing_table.heading("filingID", text="Filing ID")
    filing_table.heading("reportType", text="Report Type")
    filing_table.heading("reportPeriod", text="Report Period")
    filing_table.heading("dateFiled", text="Date")
    filing_table.heading("committeeID", text="Committee ID")

    filing_table["show"] = "headings"

    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_y = ttk.Scrollbar(command=filing_table.yview)

    filing_table.pack(fill=BOTH, expand=1)

    fetch_data()


def exit_program():
    cursor.close()
    connection.close()
    window.destroy()


# ======================================== Main Window ========================================
window = Tk()
window.title("FEC Database")
window.geometry("1280x720+0+0")

label_title = Label(window, text="Federal Election Committee Management System", font=("", 40, "bold"))
label_title.pack(side=TOP, fill=X)

# ==================== Tables Frame ====================
TablesFrame = Frame(window)
TablesFrame.place(x=0, y=120, width=1280, height=400)
tableFrame = LabelFrame(TablesFrame, font=("", 20, "bold"), text="Select a Table")
tableFrame.grid(row=0, column=0)

election_button = Button(tableFrame, text="Election", font=("", 20),
                         width=40, height=3, command=open_election_window)
election_button.grid(row=1, column=0)
committee_button = Button(tableFrame, text="Committee", font=("", 20),
                                  width=40, height=3, command=open_committee_window)
committee_button.grid(row=2, column=0)
candidate_button = Button(tableFrame, text="Candidate", font=("", 20),
                          width=40, height=3, command=open_candidate_window)
candidate_button.grid(row=3, column=0)
contribution_button = Button(tableFrame, text="Contribution", font=("", 20),
                          width=40, height=3, command=open_contribution_window)
contribution_button.grid(row=1, column=1)
expenditure_button = Button(tableFrame, text="Expenditure", font=("", 20),
                          width=40, height=3, command=open_expenditure_window)
expenditure_button.grid(row=2, column=1)
filing_button = Button(tableFrame, text="Filing", font=("", 20),
                          width=40, height=3, command=open_filing_window)
filing_button.grid(row=3, column=1)


# ==================== Exit Frame ====================
ExitFrame = Frame(window)
ExitFrame.place(x=0, y=550, width=1280, height=400)
exitFrame = LabelFrame(ExitFrame)
exitFrame.grid(row=0, column=0)

exit_button = Button(exitFrame, text="Exit", font=("", 20), command=exit_program, width=10)
exit_button.grid(row=1, column=0)


window.mainloop()