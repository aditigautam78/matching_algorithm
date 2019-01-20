#Matching algorithm for User input Property or Requirement:

Following files are present in the project:
- `radius_db.py`: Database creationg file do that a sample databases can be created in real time.
- `dataset.py` : Contains all the datasets and environment variables.
- `matching.py` : Main algorithm file.
- `rules.py` : Matching rules.
- `util.py` : Utility functions.

#Usage:
- Navigate to the cloned repository:
    `cd Radius`
    
- The following two commands have to be executed in sccession:
    `python radius_db.py` to create sample Database.
    `python matching.py` to run the main logic.
    

#Assumptions:
- User will always provide latitude and longitude.
- User will always provide the min and max bedrooms/bathrooms.
- User will specify the type of input they are entering.