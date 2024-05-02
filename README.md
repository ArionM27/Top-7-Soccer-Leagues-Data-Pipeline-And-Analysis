Overview
This project focuses on analyzing soccer statistics from UEFA's top 7 leagues using Python, SQL, and Tableau. It involves engineering an automated ETL pipeline to retrieve player statistics from FotMob APIs, processing the data into a structured format, storing it in a PostgreSQL database, conducting data analysis, and finally, visualizing some analysis using Tableau.

Features
Data Retrieval: An automated pipeline to fetch player statistics from FotMob APIs for UEFA's top 7 leagues on a weekly basis.
Data Processing: Used Python's pandas library to process and clean the retrieved data, ensuring data integrity.
Database Management: Designed and implemented a PostgreSQL database solution to store and manage player, team, and league statistics effectively.
Data Analysis: Conducted data analysis using SQL queries to derive insights into player and team performance trends.
Visualization: Created interactive sheets in Tableau to better visualize player and team performances, including all team's highest contributers, overperformers, underperfomers, etc.

- I Plan to Keep working on and Improving this project. Any Feedback will be greatly appreciated.
- Future Additions include, more leagues, implementation of NumPy arrays/analysis. I also plan to do much more analysis with SQL Queries, More In-Depth Tableau Dashboards, cloud work, etc.
  
Requirements
Python 3.x
pandas
SQLAlchemy (To Transfer into PostgreSQL Database)
Tableau Desktop or Tableau Public (for visualization)
NumPy (For a Future Update)

Usage
Clone the repository to your local machine.
Ensure that all the Requirements are installed. 
Set up a PostgreSQL database and replace create_engine("   Add In Your Own Database Here       ") with your database information.
Run the Python scripts to retrieve data, process it, and store it in the database.
Use SQL queries to analyze the data stored in the PostgreSQL database.
Connect to Tableau by either connecting it with the PostgreSQL (Tableau Desktop) or if on Tableau Public, convert to CSV either through Python (Pandas) or SQL. 

Contributor
Arkadiuz A. Mercado

Acknowledgments
FotMob for providing access to its APIs.
UEFA for providing access to its league rankings.

THIS IS FOR PERSONAL USE ONLY, ANY COMMERCIAL USE IS NOT PERMITTED BY FotMob ToS
