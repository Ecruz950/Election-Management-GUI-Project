DROP DATABASE IF EXISTS FEC_Schema;
CREATE DATABASE FEC_Schema;
USE FEC_Schema;

CREATE TABLE Election (
	ElectionID INT PRIMARY KEY,
    ElectionName VARCHAR(100),
    Date DATE,
    State VARCHAR(25)
);

INSERT INTO Election 
VALUES	(1, 'Senate Election', '2022-10-08', 'NY'),
		(2, 'Governor Election', '2023-10-05', 'CA'),
		(3, 'House Election', '2020-11-05', 'TX'),
		(4, 'Senate Election', '2021-09-10', 'FL'),
		(5, 'Governor Election', '2022-12-20', 'IL'),
		(6, 'House Election', '2023-01-05', 'OH'),
		(7, 'Senate Election', '2022-03-05', 'PA'),
		(8, 'Governor Election', '2023-10-22', 'WA'),
		(9, 'House Election', '2021-07-05', 'CA'),
		(10, 'Senate Election', '2021-05-05', 'OR'),
		(11, 'Governor Election', '2023-06-10', 'IL'),
		(12, 'House Election', '2022-11-12', 'NC'),
		(13, 'Senate Election', '2023-11-25', 'MA'),
		(14, 'Governor Election', '2022-03-12', 'CO'),
		(15, 'House Election', '2020-04-10', 'AZ');


CREATE TABLE Committee (
	CommitteeID INT PRIMARY KEY,
    CommitteeName VARCHAR(25),
    Treasurer VARCHAR(25),
    CommitteeType VARCHAR(25),
    State VARCHAR(25)
	
);

INSERT INTO Committee 
VALUES	
(1, 'Smith for Senate', 'John Doe', 'Campaign', 'NY'),
(2, 'Johnson for Senate', 'Alice Brown', 'Campaign', 'NY'),
(3, 'Brown for Governor', 'Michael Green', 'Campaign', 'CA'),
(4, 'Davis for Governor', 'Emily Smith', 'Campaign', 'CA'),
(5, 'Lee for Congress', 'Robert White', 'Campaign', 'TX'),
(6, 'Martinez for Congress', 'Sophia Lee', 'Campaign', 'TX'),
(7, 'Johnson for Senate', 'David Johnson', 'Campaign', 'FL'),
(8, 'Wilson for Senate', 'Emma Wilson', 'Campaign', 'FL'),
(9, 'White for Governor', 'Sarah Brown', 'Campaign', 'IL'),
(10, 'Taylor for Governor', 'Jason Taylor', 'Campaign', 'IL'),
(11, 'Brown for Congress', 'Olivia Harris', 'Campaign', 'OH'),
(12, 'Clark for Congress', 'Matthew Taylor', 'Campaign', 'OH'),
(13, 'Harris for Senate', 'Daniel Harris', 'Campaign', 'PA'),
(14, 'Rodriguez for Senate', 'Ella Rodriguez', 'Campaign', 'PA'),
(15, 'Garcia for Governor', 'Aiden Smith', 'Campaign', 'WA'),
(16, 'Anderson for Governor', 'Mia Davis', 'Campaign', 'WA'),
(17, 'Johnson for Congress', 'Sophia Johnson', 'Campaign', 'MI'),
(18, 'Martinez for Congress', 'Logan Martinez', 'Campaign', 'MI'),
(19, 'Thompson for Senate', 'Ethan White', 'Campaign', 'OR'),
(20, 'Scott for Senate', 'Madison Green', 'Campaign', 'OR'),
(21, 'Hall for Governor', 'Chloe Hall', 'Campaign', 'GA'),
(22, 'King for Governor', 'Elijah King', 'Campaign', 'GA'),
(23, 'Carter for Congress', 'Ava Brown', 'Campaign', 'NC'),
(24, 'White for Congress', 'Jackson White', 'Campaign', 'NC'),
(25, 'Adams for Senate', 'Harper Green', 'Campaign', 'MA'),
(26, 'Thomas for Senate', 'William Thomas', 'Campaign', 'MA'),
(27, 'Harris for Governor', 'Abigail Harris', 'Campaign', 'CO'),
(28, 'Martin for Governor', 'James Martin', 'Campaign', 'CO'),
(29, 'Young for Congress', 'Natalie Young', 'Campaign', 'AZ'),
(30, 'Hall for Congress', 'Benjamin Hall', 'Campaign', 'AZ');

CREATE TABLE Candidate (
	CandidateID INT PRIMARY KEY,
    CandidateName VARCHAR(25),
    PartyAffiliation VARCHAR(25),
    Office VARCHAR(25),
    State VARCHAR(25),
    CommitteeID INT,
    ElectionID INT,
    FOREIGN KEY(CommitteeID) REFERENCES Committee(CommitteeID) ON DELETE CASCADE,
    FOREIGN KEY(ElectionID) REFERENCES Election(ElectionID) ON DELETE CASCADE
	
);

INSERT INTO Candidate 
VALUES 
(1, 'John Smith', 'Democratic Party', 'Senator', 'NY', 1, 1),
(2, 'Alice Johnson', 'Republican Party', 'Senator', 'NY', 2, 1),
(3, 'Michael Brown', 'Green Party', 'Governor', 'CA', 3, 2),
(4, 'Emily Davis', 'Independent', 'Governor', 'CA', 4, 2),
(5, 'Robert Lee', 'Democratic Party', 'Representative', 'TX', 5, 3),
(6, 'Sophia Martinez', 'Republican Party', 'Representative', 'TX', 6, 3),
(7, 'David Johnson', 'Libertarian Party', 'Senator', 'FL', 7, 4),
(8, 'Emma Wilson', 'Independent', 'Senator', 'FL', 8, 4),
(9, 'Sarah White', 'Democratic Party', 'Governor', 'IL', 9, 5),
(10, 'Jason Taylor', 'Republican Party', 'Governor', 'IL', 10, 5),
(11, 'Olivia Brown', 'Green Party', 'Representative', 'OH', 11, 6),
(12, 'Matthew Clark', 'Independent', 'Representative', 'OH', 12, 6),
(13, 'Daniel Harris', 'Democratic Party', 'Senator', 'PA', 13, 7),
(14, 'Ella Rodriguez', 'Republican Party', 'Senator', 'PA', 14, 7),
(15, 'Aiden Garcia', 'Libertarian Party', 'Governor', 'WA', 15, 8),
(16, 'Mia Anderson', 'Independent', 'Governor', 'WA', 16, 8),
(17, 'Sophia Johnson', 'Democratic Party', 'Representative', 'MI', 17, 9),
(18, 'Logan Martinez', 'Republican Party', 'Representative', 'MI', 18, 9),
(19, 'Ethan Thompson', 'Green Party', 'Senator', 'OR', 19, 10),
(20, 'Madison Scott', 'Independent', 'Senator', 'OR', 20, 10),
(21, 'Chloe Hall', 'Democratic Party', 'Governor', 'GA', 21, 11),
(22, 'Elijah King', 'Republican Party', 'Governor', 'GA', 22, 11),
(23, 'Ava Carter', 'Libertarian Party', 'Representative', 'NC', 23, 12),
(24, 'Jackson White', 'Independent', 'Representative', 'NC', 24, 12),
(25, 'Harper Adams', 'Democratic Party', 'Senator', 'MA', 25, 13),
(26, 'William Thomas', 'Republican Party', 'Senator', 'MA', 26, 13),
(27, 'Abigail Harris', 'Green Party', 'Governor', 'CO', 27, 14),
(28, 'James Martin', 'Independent', 'Governor', 'CO', 28, 14),
(29, 'Natalie Young', 'Democratic Party', 'Representative', 'AZ', 29, 15),
(30, 'Benjamin Hall', 'Republican Party', 'Representative', 'AZ', 30, 15);

CREATE TABLE Contribution (
	ContributionID INT PRIMARY KEY,
    DonorName VARCHAR(25),
    CommitteeID INT,
	Amount INT,
    Date DATE,
    FOREIGN KEY(CommitteeID) REFERENCES Committee(CommitteeID) ON DELETE CASCADE
	
);

INSERT INTO Contribution 
VALUES 
(1, 'John Smith', 1, 1000.00, '2023-01-15'),
(2, 'Alice Johnson', 2, 1500.00, '2023-02-20'),
(3, 'Michael Green', 3, 2000.00, '2023-03-25'),
(4, 'Emily Brown', 4, 2500.00, '2023-04-30'),
(5, 'Robert White', 5, 3000.00, '2023-05-05'),
(6, 'Sophia Lee', 6, 3500.00, '2023-06-10'),
(7, 'David Johnson', 7, 4000.00, '2023-07-15'),
(8, 'Emma Wilson', 8, 4500.00, '2023-08-20'),
(9, 'Sarah Brown', 9, 5000.00, '2023-09-25'),
(10, 'Jason Taylor', 10, 5500.00, '2023-10-30'),
(11, 'Olivia Harris', 11, 6000.00, '2023-11-05'),
(12, 'Matthew Taylor', 12, 6500.00, '2023-12-10'),
(13, 'Daniel Harris', 13, 7000.00, '2024-01-15'),
(14, 'Ella Rodriguez', 14, 7500.00, '2024-02-20'),
(15, 'Aiden Smith', 15, 8000.00, '2024-03-25');

CREATE TABLE Expenditure (
	ExpenditureID INT PRIMARY KEY,
	Payee VARCHAR(25),
    CommitteeID INT,
	Amount INT,
    Purpose VARCHAR(250),
    Date DATE,
    FOREIGN KEY(CommitteeID) REFERENCES Committee(CommitteeID) ON DELETE CASCADE
	
);

INSERT INTO Expenditure
VALUES 
(1, 'John Doe', 1, 500.00, 'Advertising', '2023-01-05'),
(2, 'Alice Brown', 2, 600.00, 'Event expenses', '2023-02-10'),
(3, 'Michael Green', 3, 700.00, 'Office rent', '2023-03-15'),
(4, 'Emily Smith', 4, 800.00, 'Travel expenses', '2023-04-20'),
(5, 'Robert White', 5, 900.00, 'Printing', '2023-05-25'),
(6, 'Sophia Lee', 6, 1000.00, 'Consulting fees', '2023-06-30'),
(7, 'David Johnson', 7, 1100.00, 'Website development', '2023-07-05'),
(8, 'Emma Wilson', 8, 1200.00, 'Telecommunications', '2023-08-10'),
(9, 'Sarah Brown', 9, 1300.00, 'Legal fees', '2023-09-15'),
(10, 'Jason Taylor', 10, 1400.00, 'Catering', '2023-10-20'),
(11, 'Olivia Harris', 11, 1500.00, 'Transportation', '2023-11-25'),
(12, 'Matthew Taylor', 12, 1600.00, 'Security', '2023-12-30'),
(13, 'Daniel Harris', 13, 1750.00, 'Utilities', '2024-01-05'),
(14, 'Ella Rodriguez', 14, 1800.00, 'Equipment purchase', '2024-02-10'),
(15, 'Aiden Smith', 15, 1900.00, 'Advertising', '2024-03-15');

CREATE TABLE Filing (
	FilingID INT PRIMARY KEY,
    ReportType VARCHAR(25),
    ReportPeriod VARCHAR(25),
    DateFiled DATE,
    CommitteeID INT,
    FOREIGN KEY(CommitteeID) REFERENCES Committee(CommitteeID) ON DELETE CASCADE
	
);

INSERT INTO Filing
VALUES 
(1, 'Quarterly', 'Q1 2023', '2023-04-15', 1),
(2, 'Quarterly', 'Q2 2023', '2023-07-15', 2),
(3, 'Quarterly', 'Q3 2023', '2023-10-15', 3),
(4, 'Quarterly', 'Q4 2023', '2024-01-15', 4),
(5, 'Quarterly', 'Q1 2024', '2024-04-15', 5),
(6, 'Quarterly', 'Q2 2024', '2024-07-15', 6),
(7, 'Quarterly', 'Q3 2024', '2024-10-15', 7),
(8, 'Quarterly', 'Q4 2024', '2025-01-15', 8),
(9, 'Quarterly', 'Q1 2025', '2025-04-15', 9),
(10, 'Quarterly', 'Q2 2025', '2025-07-15', 10),
(11, 'Quarterly', 'Q3 2025', '2025-10-15', 11),
(12, 'Quarterly', 'Q4 2025', '2026-01-15', 12),
(13, 'Quarterly', 'Q1 2026', '2026-04-15', 13),
(14, 'Quarterly', 'Q2 2026', '2026-07-15', 14),
(15, 'Quarterly', 'Q3 2026', '2026-10-15', 15);

CREATE TABLE CandidateElectionAssociation (
	AssociationID INT PRIMARY KEY, 
    CandidateID INT,
    ElectionID INT,
    FOREIGN KEY(CandidateID) REFERENCES Candidate(CandidateID) ON DELETE CASCADE,
    FOREIGN KEY(ElectionID) REFERENCES Election(ElectionID) ON DELETE CASCADE

);

INSERT INTO CandidateElectionAssociation
VALUES	
	(1, 1, 1),
	(2, 2, 1),
	(3, 3, 2),
	(4, 4, 2),
	(5, 5, 3),
	(6, 6, 3),
	(7, 7, 4),
	(8, 8, 4),
	(9, 9, 5),
	(10, 10, 5),
	(11, 11, 6),
	(12, 12, 6),
	(13, 13, 7),
	(14, 14, 7),
	(15, 15, 8),
	(16, 16, 8),
	(17, 17, 9),
	(18, 18, 9),
	(19, 19, 10),
	(20, 20, 10),
	(21, 21, 11),
	(22, 22, 11),
	(23, 23, 12),
	(24, 24, 12),
	(25, 25, 13),
	(26, 26, 13),
	(27, 27, 14),
	(28, 28, 14),
	(29, 29, 15),
	(30, 30, 15);
