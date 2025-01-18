import mysql.connector
from mysql.connector import Error
import __main__


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

cursor = connection.cursor()
def read_data_election():
    # Read data from the table
    select_query = "SELECT ElectionID, ElectionName, Date, State FROM Election"
    cursor = connection.cursor()
    cursor.execute(select_query)
    elections = cursor.fetchall()

    print("Election Data:")
    for election in elections:
        print (f"ElectionID: {election[0]}, ElectionName: {election[1]}, Date: {election[2]}, State: {election[3]}")

def write_data_election():
    # Get input data for a new election
    election_id = input("Enter Election ID: ")
    election_name = input("Enter Election Name: ")
    date = input("Enter Election Date (YYYY-MM-DD): ")
    state = input("Enter State: ")

    # SQL query to insert data into the Election table
    insert_query = "INSERT INTO Election (ElectionID, ElectionName, Date, State) VALUES (%s, %s, %s, %s)"
    election_data = (election_id, election_name, date, state)

    cursor = connection.cursor()
    cursor.execute(insert_query, election_data)
    connection.commit()
    print("Election data written/inserted successfully.")

def update_data_election(election_id, election_name, date, state):
    """
    Update an election record in the database.

    :param election_id: int - The ID of the election to update.
    :param election_name: str - The new name of the election.
    :param date: str - The new date of the election in YYYY-MM-DD format.
    :param state: str - The new state of the election.
    """
    # Prepare the SQL query with placeholders for the parameters
    update_query = """
        UPDATE Election 
        SET ElectionName = %s, 
            Date = %s, 
            State = %s
        WHERE ElectionID = %s;
    """
    
    # Connect to the database
    try:
        # Assuming 'connection' is the MySQL connection object
        cursor = connection.cursor()
        # Execute the update query with the provided parameters
        cursor.execute(update_query, (election_name, date, state, election_id))
        # Commit the changes to the database
        connection.commit()
        print(f"Election with ID {election_id} updated successfully.")
    except mysql.connector.Error as e:
        # Handle any SQL errors
        print(f"Error updating election: {e}")
    finally:
        # Ensure the cursor is closed after operation
        cursor.close()
        return

def delete_data_election():
    """
    Delete an election record from the database.
    """
    # Get the ElectionID of the election to delete
    election_id = input("Enter Election ID to delete: ")

    # First, delete dependent rows from the candidate table
    delete_dependent_rows(election_id)

    # Then, delete the election record
    delete_query = "DELETE FROM Election WHERE ElectionID = %s;"

    try:
        cursor = connection.cursor()
        cursor.execute(delete_query, (election_id,))
        connection.commit()
        print(f"Election with ID {election_id} deleted successfully.")
    except mysql.connector.Error as e:
        print(f"Error deleting election: {e}")
    finally:
        cursor.close()

def delete_dependent_rows(election_id):
    """
    Delete dependent rows from the candidate table.
    """
    delete_query = "DELETE FROM candidate WHERE ElectionID = %s;"
    try:
        cursor = connection.cursor()
        cursor.execute(delete_query, (election_id,))
        connection.commit()
        print(f"Dependent rows in the candidate table for ElectionID {election_id} deleted successfully.")
    except mysql.connector.Error as e:
        print(f"Error deleting dependent rows in the candidate table: {e}")
    finally:
        cursor.close()

def other_election():
    print("Other functionalities yet to come in Deliverable 5")
    return

def read_data_committee():
    select_query = "SELECT CommitteeID, CommitteeName, Treasurer, CommitteeType, State FROM Committee"
    cursor = connection.cursor()
    cursor.execute(select_query)
    committees = cursor.fetchall()

    print("Committee Data:")
    for committee in committees:
        print(f"CommitteeID: {committee[0]}, CommitteeName: {committee[1]}, Treasurer: {committee[2]}, CommitteeType: {committee[3]}, State: {committee[4]}")

def write_data_committee():
    committee_id = input("Enter Committee ID: ")
    committee_name = input("Enter Committee Name: ")
    treasurer = input("Enter Treasurer Name: ")
    committee_type = input("Enter Committee Type: ")
    state = input("Enter State: ")

    insert_query = "INSERT INTO Committee (CommitteeID, CommitteeName, Treasurer, CommitteeType, State) VALUES (%s, %s, %s, %s, %s)"
    committee_data = (committee_id, committee_name, treasurer, committee_type, state)

    cursor = connection.cursor()
    cursor.execute(insert_query, committee_data)
    connection.commit()
    print("Committee data written/inserted successfully.")

def update_data_committee(committee_id, committee_name, treasurer, committee_type, state):
    """
    Update a committee record in the database.

    :param committee_id: int - The ID of the committee to update.
    :param committee_name: str - The new name of the committee.
    :param treasurer: str - The new treasurer of the committee.
    :param committee_type: str - The new type of the committee.
    :param state: str - The new state of the committee.
    """
    # Prepare the SQL query with placeholders for the parameters
    update_query = """
        UPDATE Committee
        SET CommitteeName = %s, 
            Treasurer = %s, 
            CommitteeType = %s,
            State = %s
        WHERE CommitteeID = %s;
    """
    
    # Connect to the database
    try:
        cursor = connection.cursor()
        # Execute the update query with the provided parameters
        cursor.execute(update_query, (committee_name, treasurer, committee_type, state, committee_id))
        # Commit the changes to the database
        connection.commit()
        print(f"Committee with ID {committee_id} updated successfully.")
    except mysql.connector.Error as e:
        # Handle any SQL errors
        print(f"Error updating committee: {e}")
    finally:
        # Ensure the cursor is closed after operation
        cursor.close()
        return


def delete_data_committee():
    """
    Delete a committee record from the database.
    """
    committee_id = input("Enter Committee ID to delete: ")

    delete_query = "DELETE FROM Committee WHERE CommitteeID = %s;"

    try:
        cursor = connection.cursor()
        cursor.execute(delete_query, (committee_id,))
        connection.commit()
        print(f"Committee with ID {committee_id} deleted successfully.")
    except mysql.connector.Error as e:
        print(f"Error deleting committee: {e}")
    finally:
        cursor.close()

def other_committee():
    print("Other functionalities yet to come in Deliverable 5")
    return

def read_data_candidate():
    select_query = "SELECT CandidateID, CandidateName, PartyAffiliation, Office, State, CommitteeID, ElectionID FROM Candidate"
    cursor = connection.cursor()
    cursor.execute(select_query)
    candidates = cursor.fetchall()

    print("Candidate Data:")
    for candidate in candidates:
        print(f"CandidateID: {candidate[0]}, CandidateName: {candidate[1]}, PartyAffiliation: {candidate[2]}, Office: {candidate[3]}, State: {candidate[4]}, CommitteeID: {candidate[5]}, ElectionID: {candidate[6]}")

def write_data_candidate():
    candidate_id = input("Enter Candidate ID: ")
    candidate_name = input("Enter Candidate Name: ")
    party_affiliation = input("Enter Party Affiliation: ")
    office = input("Enter Office: ")
    state = input("Enter State: ")
    committee_id = input("Enter Committee ID: ")
    election_id = input("Enter Election ID: ")

    insert_query = "INSERT INTO Candidate (CandidateID, CandidateName, PartyAffiliation, Office, State, CommitteeID, ElectionID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    candidate_data = (candidate_id, candidate_name, party_affiliation, office, state, committee_id, election_id)

    cursor = connection.cursor()
    cursor.execute(insert_query, candidate_data)
    connection.commit()
    print("Candidate data written successfully.")

def update_data_candidate(candidate_id, candidate_name, party_affiliation, office, state, committee_id, election_id):
    """
    Update a candidate record in the database.

    :param candidate_id: int - The ID of the candidate to update.
    :param candidate_name: str - The new name of the candidate.
    :param party_affiliation: str - The new party affiliation of the candidate.
    :param office: str - The new office of the candidate.
    :param state: str - The new state of the candidate.
    :param committee_id: int - The new committee ID associated with the candidate.
    :param election_id: int - The new election ID associated with the candidate.
    """
    # Prepare the SQL query with placeholders for the parameters
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

    # Connect to the database
    try:
        cursor = connection.cursor()
        # Execute the update query with the provided parameters
        cursor.execute(update_query, (candidate_name, party_affiliation, office, state, committee_id, election_id, candidate_id))
        # Commit the changes to the database
        connection.commit()
        print(f"Candidate with ID {candidate_id} updated successfully.")
    except mysql.connector.Error as e:
        # Handle any SQL errors
        print(f"Error updating candidate: {e}")
    finally:
        # Ensure the cursor is closed after operation
        cursor.close()
        return

def delete_data_candidate():
    """
    Delete a candidate record from the database.
    """
    # Get the CandidateID of the candidate to delete
    candidate_id = input("Enter Candidate ID to delete: ")

    # Prepare the SQL query to delete the record
    delete_query = "DELETE FROM Candidate WHERE CandidateID = %s;"

    try:
        cursor = connection.cursor()
        cursor.execute(delete_query, (candidate_id,))
        connection.commit()
        print(f"Candidate with ID {candidate_id} deleted successfully.")
    except mysql.connector.Error as e:
        # Handle any SQL errors
        print(f"Error deleting candidate: {e}")
    finally:
        # Ensure the cursor is closed after operation
        cursor.close()

def other_candidate():
    print("Other functionalities yet to come in Deliverable 5")
    return

def read_data_contribution():
    select_query = "SELECT ContributionID, DonorName, CommitteeID, Amount, Date FROM Contribution"
    cursor = connection.cursor()
    cursor.execute(select_query)
    contributions = cursor.fetchall()

    print("Contribution Data:")
    for contribution in contributions:
        print(f"ContributionID: {contribution[0]}, DonorName: {contribution[1]}, CommitteeID: {contribution[2]}, Amount: {contribution[3]}, Date: {contribution[4]}")

def write_data_contribution():
    contribution_id = input("Enter Contribution ID: ")
    donor_name = input("Enter Donor Name: ")
    committee_id = input("Enter Committee ID: ")
    amount = input("Enter Amount: ")
    date = input("Enter Date (YYYY-MM-DD): ")

    insert_query = "INSERT INTO Contribution (ContributionID, DonorName, CommitteeID, Amount, Date) VALUES (%s, %s, %s, %s, %s)"
    contribution_data = (contribution_id, donor_name, committee_id, amount, date)

    cursor = connection.cursor()
    cursor.execute(insert_query, contribution_data)
    connection.commit()
    print("Contribution data written successfully.")

def update_data_contribution(contribution_id, donor_name, committee_id, amount, date):
    """
    Update a contribution record in the database.

    :param contribution_id: int - The ID of the contribution to update.
    :param donor_name: str - The new name of the donor.
    :param committee_id: int - The new committee ID associated with the contribution.
    :param amount: float - The new amount of the contribution.
    :param date: str - The new date of the contribution in YYYY-MM-DD format.
    """
    # Prepare the SQL query with placeholders for the parameters
    update_query = """
        UPDATE Contribution
        SET DonorName = %s, 
            CommitteeID = %s, 
            Amount = %s,
            Date = %s
        WHERE ContributionID = %s;
    """

    # Connect to the database
    try:
        cursor = connection.cursor()
        # Execute the update query with the provided parameters
        cursor.execute(update_query, (donor_name, committee_id, amount, date, contribution_id))
        # Commit the changes to the database
        connection.commit()
        print(f"Contribution with ID {contribution_id} updated successfully.")
    except mysql.connector.Error as e:
        # Handle any SQL errors
        print(f"Error updating contribution: {e}")
    finally:
        # Ensure the cursor is closed after operation
        cursor.close()
        return

def delete_data_contribution():
    """
    Delete a contribution record from the database.
    """
    # Get the ContributionID of the contribution to delete
    contribution_id = input("Enter Contribution ID to delete: ")

    # Prepare the SQL query to delete the record
    delete_query = "DELETE FROM Contribution WHERE ContributionID = %s;"

    try:
        cursor = connection.cursor()
        cursor.execute(delete_query, (contribution_id,))
        connection.commit()
        print(f"Contribution with ID {contribution_id} deleted successfully.")
    except mysql.connector.Error as e:
        # Handle any SQL errors
        print(f"Error deleting contribution: {e}")
    finally:
        # Ensure the cursor is closed after operation
        cursor.close()

def other_contributions():
    print("Other functionalities yet to come in Deliverable 5")
    return

def read_data_expenditure():
    select_query = "SELECT ExpenditureID, Payee, CommitteeID, Amount, Purpose, Date FROM Expenditure"
    cursor = connection.cursor()
    cursor.execute(select_query)
    expenditures = cursor.fetchall()

    print("Expenditure Data:")
    for expenditure in expenditures:
        print(f"ExpenditureID: {expenditure[0]}, Payee: {expenditure[1]}, CommitteeID: {expenditure[2]}, Amount: {expenditure[3]}, Purpose: {expenditure[4]}, Date: {expenditure[5]}")

def write_data_expenditure():
    expenditure_id = input("Enter Expenditure ID: ")
    payee = input("Enter Payee Name: ")
    committee_id = input("Enter Committee ID: ")
    amount = input("Enter Amount: ")
    purpose = input("Enter Purpose: ")
    date = input("Enter Date (YYYY-MM-DD): ")

    insert_query = "INSERT INTO Expenditure (ExpenditureID, Payee, CommitteeID, Amount, Purpose, Date) VALUES (%s, %s, %s, %s, %s, %s)"
    expenditure_data = (expenditure_id, payee, committee_id, amount, purpose, date)

    cursor = connection.cursor()
    cursor.execute(insert_query, expenditure_data)
    connection.commit()
    print("Expenditure data written successfully.")

def update_data_expenditure(expenditure_id, payee, committee_id, amount, purpose, date):
    """
    Update an expenditure record in the database.

    :param expenditure_id: int - The ID of the expenditure to update.
    :param payee: str - The new name of the payee.
    :param committee_id: int - The committee ID associated with the expenditure.
    :param amount: float - The new amount of the expenditure.
    :param purpose: str - The new purpose of the expenditure.
    :param date: str - The new date of the expenditure in YYYY-MM-DD format.
    """
    # Prepare the SQL query with placeholders for the parameters
    update_query = """
        UPDATE Expenditure
        SET Payee = %s, 
            CommitteeID = %s, 
            Amount = %s,
            Purpose = %s,
            Date = %s
        WHERE ExpenditureID = %s;
    """

    # Connect to the database
    try:
        cursor = connection.cursor()
        # Execute the update query with the provided parameters
        cursor.execute(update_query, (payee, committee_id, amount, purpose, date, expenditure_id))
        # Commit the changes to the database
        connection.commit()
        print(f"Expenditure with ID {expenditure_id} updated successfully.")
    except mysql.connector.Error as e:
        # Handle any SQL errors
        print(f"Error updating expenditure: {e}")
    finally:
        # Ensure the cursor is closed after operation
        cursor.close()
        return

def delete_data_expenditure():
    """
    Delete an expenditure record from the database.
    """
    # Get the ExpenditureID of the expenditure to delete
    expenditure_id = input("Enter Expenditure ID to delete: ")

    # Prepare the SQL query to delete the record
    delete_query = "DELETE FROM Expenditure WHERE ExpenditureID = %s;"

    try:
        cursor = connection.cursor()
        cursor.execute(delete_query, (expenditure_id,))
        connection.commit()
        print(f"Expenditure with ID {expenditure_id} deleted successfully.")
    except mysql.connector.Error as e:
        # Handle any SQL errors
        print(f"Error deleting expenditure: {e}")
    finally:
        # Ensure the cursor is closed after operation
        cursor.close()

def other_expenditure():
    print("Other functionalities yet to come in Deliverable 5")
    return

def read_data_filing():
    select_query = "SELECT FilingID, ReportType, ReportPeriod, DateFiled, CommitteeID FROM Filing"
    cursor = connection.cursor()
    cursor.execute(select_query)
    filings = cursor.fetchall()

    print("Filing Data:")
    for filing in filings:
        print(f"FilingID: {filing[0]}, ReportType: {filing[1]}, ReportPeriod: {filing[2]}, DateFiled: {filing[3]}, CommitteeID: {filing[4]}")

def write_data_filing():
    filing_id = input("Enter Filing ID: ")
    report_type = input("Enter Report Type: ")
    report_period = input("Enter Report Period: ")
    date_filed = input("Enter Date Filed (YYYY-MM-DD): ")
    committee_id = input("Enter Committee ID: ")

    insert_query = "INSERT INTO Filing (FilingID, ReportType, ReportPeriod, DateFiled, CommitteeID) VALUES (%s, %s, %s, %s, %s)"
    filing_data = (filing_id, report_type, report_period, date_filed, committee_id)

    cursor = connection.cursor()
    cursor.execute(insert_query, filing_data)
    connection.commit()
    print("Filing data written successfully.")
    

def update_data_filing(filing_id, report_type, report_period, date_filed, committee_id):
    """
    Update a filing record in the database.

    :param filing_id: int - The ID of the filing to update.
    :param report_type: str - The new type of the report.
    :param report_period: str - The new period of the report.
    :param date_filed: str - The new filing date in YYYY-MM-DD format.
    :param committee_id: int - The committee ID associated with the filing.
    """
    # Prepare the SQL query with placeholders for the parameters
    update_query = """
        UPDATE Filing
        SET ReportType = %s, 
            ReportPeriod = %s, 
            DateFiled = %s,
            CommitteeID = %s
        WHERE FilingID = %s;
    """

    # Connect to the database
    try:
        cursor = connection.cursor()
        # Execute the update query with the provided parameters
        cursor.execute(update_query, (report_type, report_period, date_filed, committee_id, filing_id))
        # Commit the changes to the database
        connection.commit()
        print(f"Filing with ID {filing_id} updated successfully.")
    except mysql.connector.Error as e:
        # Handle any SQL errors
        print(f"Error updating filing: {e}")
    finally:
        # Ensure the cursor is closed after operation
        cursor.close() # Jumps to lin 672 and converts committee_id and filing_id to a string which causes error
        return # fix this by returning

def delete_data_filing():
    """
    Delete a filing record from the database.
    """
    # Get the FilingID of the filing to delete
    filing_id = input("Enter Filing ID to delete: ")

    # Prepare the SQL query to delete the record
    delete_query = "DELETE FROM Filing WHERE FilingID = %s;"

    try:
        cursor = connection.cursor()
        cursor.execute(delete_query, (filing_id,))
        connection.commit()
        print(f"Filing with ID {filing_id} deleted successfully.")
    except mysql.connector.Error as e:
        # Handle any SQL errors
        print(f"Error deleting filing: {e}")
    finally:
        # Ensure the cursor is closed after operation
        cursor.close()

def other_filing():
    print("Other functionalities yet to come in Deliverable 5")
    return

def main():
    exit_program = False
    while exit_program == False:
        print("Select a Table to Work With:")
        print("1. Election")
        print("2. Committee")
        print("3. Candidate")
        print("4. Contribution")
        print("5. Expenditure")
        print("6. Filing")
        print("7. Exit")

        table_choice = input("Enter your choice of table: ")

        if table_choice == '7':
            print("Exiting program.")
            exit_program = True

        while exit_program == False:
            print(f"Table: {table_choice}")
            print("Select an Action:")
            print("1. Read/output all data from a given table.")
            print("2. Write/insert new data into a given table.")
            print("3. Update existing data in a given table")
            print("4. Delete any row from a given table.")
            print("5. Other functionalities yet to come in Deliverable 5")
            print("6. Return to Table Selection")
            print("7. Exit")

            action_choice = input("Enter your action choice: ")

            if action_choice == '6':
                break
            elif action_choice == '7':
                print("Exiting program.")
                exit_program = True
                break
            else:
                perform_action(table_choice, action_choice)
                #break
            continue_choice = input("Do you want to perform another action on this table? (Y/N): ").strip().upper()

            if continue_choice == 'Y' or continue_choice == 'y':
                continue
            else:
                break
    # Close the database connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Connection to MySQL database closed")

def perform_action(table_choice, action_choice):
    # Mapping table_choice to table names
    table_mapping = {
        '1': 'election',
        '2': 'committee',
        '3': 'candidate',
        '4': 'contribution',
        '5': 'expenditure',
        '6': 'filing'
    }

    # Mapping action_choice to action names
    action_mapping = {
        '1': 'read_data',
        '2': 'write_data',
        '3': 'update_data',
        '4': 'delete_data',
        '5': 'others'
    }

    table_name = table_mapping.get(table_choice)
    action_name = action_mapping.get(action_choice)

    if action_name == 'update_data':
        if table_name == 'election':
            print("Preparing to update election data")
            election_id = input("Enter Election ID: ")
            election_name = input("Enter Election Name: ")
            date = input("Enter Election Date (YYYY-MM-DD): ")
            state = input("Enter State: ")
            update_data_election(int(election_id), election_name, date, state)
            return
       
        elif table_name == 'committee':
            print("Preparing to update committee data")  # Debugging statement
            # Get user input for the committee update
            committee_id = input("Enter Committee ID: ")
            committee_name = input("Enter Committee Name: ")
            treasurer = input("Enter Treasurer Name: ")
            committee_type = input("Enter Committee Type: ")
            state = input("Enter State: ")
            # Call the update function with the required arguments
            update_data_committee(int(committee_id), committee_name, treasurer, committee_type, state)
            return

    
        elif table_name == 'candidate':
            print("Preparing to update candidate data")
            candidate_id = input("Enter Candidate ID: ")
            candidate_name = input("Enter Candidate Name: ")
            party_affiliation = input("Enter Party Affiliation: ")
            office = input("Enter Office: ")
            state = input("Enter State: ")
            committee_id = input("Enter Committee ID: ")
            election_id = input("Enter Election ID: ")
            update_data_candidate(int(candidate_id), candidate_name, party_affiliation, office, state, int(committee_id), int(election_id))
            return
        
        elif table_name == 'contribution':
            print("Preparing to update contribution data")
            contribution_id = input("Enter Contribution ID: ")
            donor_name = input("Enter Donor Name: ")
            committee_id = input("Enter Committee ID: ")
            amount = input("Enter Amount: ")
            date = input("Enter Date (YYYY-MM-DD): ")
            update_data_contribution(int(contribution_id), donor_name, int(committee_id), float(amount), date)
            return
        
        elif table_name == 'expenditure':
            print("Preparing to update expenditure data")
            expenditure_id = input("Enter Expenditure ID: ")
            payee = input("Enter Payee Name: ")
            committee_id = input("Enter Committee ID: ")
            amount = input("Enter Amount: ")
            purpose = input("Enter Purpose: ")
            date = input("Enter Date (YYYY-MM-DD): ")
            update_data_expenditure(int(expenditure_id), payee, int(committee_id), float(amount), purpose, date)
            return
        
        elif table_name == 'filing':
            print("Preparing to update filing data")
            filing_id = input("Enter Filing ID: ")
            report_type = input("Enter Report Type: ")
            report_period = input("Enter Report Period: ")
            date_filed = input("Enter Date Filed (YYYY-MM-DD): ")
            committee_id = input("Enter Committee ID: ")
            update_data_filing(int(filing_id), report_type, report_period, date_filed, int(committee_id))
            return


    if table_name and action_name:
        # Construct function name
        func_name = f"{action_name}_{table_name}"

        # Check if function exists and call it
        if hasattr(__main__, func_name):
            func = getattr(__main__, func_name)
            func()
        else:
            print(f"No function found for the choice: {func_name}")
    else:
        print("Invalid table or action choice. Please select a valid option.")

if __name__ == "__main__":
    main()