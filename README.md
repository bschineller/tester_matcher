# tester_matcher
Matches Testers based on User search Criteria.

Written in Python and SQL, loads CSV files into SQLLite database.
Command line implementation prompts user for search criteria, queries database and returns results to console.

## Prerequisite
Python3 installed on your system.
Clone the git repository, go inside top-level directory via command line and run

```
python3 matcher.py
```

## Examples

1) Criteria: Country = ALL and Device=  'Galaxy S4' or'iPhone 4S'

```
$ python3 matcher.py
Database setup complete. (Testers, Devices, and Bugs loaded.)
===============================================================================================
Tester Matching Application.
  Matches Testers based on User's search Criteria.
   Search results ranked in order of Experience.
   Experience is measured by the number of Bug(s) a given Tester filed for the given Device(s).
===============================================================================================
Available countries are:
('GB',)
('JP',)
('US',)
What Countries? ('ALL' or a comma-separated list of single-quoted country codes) : 'ALL'
You entered: 'ALL'
Available devices are:
('Droid DNA',)
('Droid Razor',)
('Galaxy S3',)
('Galaxy S4',)
('HTC One',)
('Nexus 4',)
('iPhone 3',)
('iPhone 4',)
('iPhone 4S',)
('iPhone 5',)
What Devices? ('ALL' or a comma-separated list of single-quoted device names) : 'Galaxy S4','iPhone 4S'
You entered: 'Galaxy S4','iPhone 4S'
There are 7 matching Testers.
First Name, Last Name, Country, Device, Experience(# Bugs)
('Taybin', 'Rutkin', 'US', 'iPhone 4S', 59)
('Miguel', 'Bautista', 'US', 'iPhone 4S', 26)
('Lucas', 'Lowry', 'JP', 'Galaxy S4', 22)
('Darshini', 'Thiagarajan', 'GB', 'Galaxy S4', 21)
('Mingquan', 'Zheng', 'JP', 'Galaxy S4', 20)
('Michael', 'Lubavin', 'US', 'Galaxy S4', 19)
('Leonard', 'Sutton', 'GB', 'Galaxy S4', 19)
```

2) Criteria: Country = 'JP' and Device=  ALL

```
$ python3 matcher.py
Database setup complete. (Testers, Devices, and Bugs loaded.)
===============================================================================================
Tester Matching Application.
  Matches Testers based on User's search Criteria.
   Search results ranked in order of Experience.
   Experience is measured by the number of Bug(s) a given Tester filed for the given Device(s).
===============================================================================================
Available countries are:
('GB',)
('JP',)
('US',)
What Countries? ('ALL' or a comma-separated list of single-quoted country codes) : 'JP' 
You entered: 'JP'
Available devices are:
('Droid DNA',)
('Droid Razor',)
('Galaxy S3',)
('Galaxy S4',)
('HTC One',)
('Nexus 4',)
('iPhone 3',)
('iPhone 4',)
('iPhone 4S',)
('iPhone 5',)
What Devices? ('ALL' or a comma-separated list of single-quoted device names) : ALL
You entered: ALL
There are 15 matching Testers.
First Name, Last Name, Country, Device, Experience(# Bugs)
('Mingquan', 'Zheng', 'JP', 'Droid Razor', 36)
('Sean', 'Wellington', 'JP', 'iPhone 5', 30)
('Lucas', 'Lowry', 'JP', 'Galaxy S3', 28)
('Sean', 'Wellington', 'JP', 'iPhone 4', 28)
('Lucas', 'Lowry', 'JP', 'Nexus 4', 25)
('Sean', 'Wellington', 'JP', 'Nexus 4', 23)
('Lucas', 'Lowry', 'JP', 'Galaxy S4', 22)
('Mingquan', 'Zheng', 'JP', 'iPhone 4', 21)
('Lucas', 'Lowry', 'JP', 'Droid Razor', 21)
('Lucas', 'Lowry', 'JP', 'Droid DNA', 21)
('Mingquan', 'Zheng', 'JP', 'Galaxy S4', 20)
('Mingquan', 'Zheng', 'JP', 'iPhone 3', 19)
('Sean', 'Wellington', 'JP', 'iPhone 3', 18)
('Sean', 'Wellington', 'JP', 'HTC One', 17)
('Mingquan', 'Zheng', 'JP', 'Nexus 4', 13)
```
