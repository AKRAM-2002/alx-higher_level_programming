# Project README

## SQL - More Queries

### Overview
Welcome to the advanced tasks of the SQL project! In this project, you will dive deeper into MySQL and enhance your understanding of database management. The tasks cover various topics, including user privileges, database creation, table design, and querying.

### Learning Objectives
By the end of this project, you should be able to:
- Create and manage MySQL users
- Grant privileges to users on databases and tables
- Understand and implement PRIMARY KEY and FOREIGN KEY constraints
- Use NOT NULL and UNIQUE constraints
- Retrieve data from multiple tables using JOIN and subqueries
- Explore advanced SQL techniques like UNION

### Tasks
1. **My Privileges!**
   - Script: 0-privileges.sql
   - Lists all privileges of the MySQL users user_0d_1 and user_0d_2 on the localhost server.

2. **Root User**
   - Script: 1-create_user.sql
   - Creates the MySQL server user user_0d_1 with all privileges.

3. **Read User**
   - Script: 2-create_read_user.sql
   - Creates the database hbtn_0d_2 and the user user_0d_2 with SELECT privilege.

4. **Always a Name**
   - Script: 3-force_name.sql
   - Creates the table force_name with id (INT) and name (VARCHAR) on the specified MySQL server.

5. **ID Can't Be Null**
   - Script: 4-never_empty.sql
   - Creates the table id_not_null with id (INT default 1) and name (VARCHAR) on the specified MySQL server.

6. **Unique ID**
   - Script: 5-unique_id.sql
   - Creates the table unique_id with id (INT default 1, unique) and name (VARCHAR) on the specified MySQL server.

7. **States Table**
   - Script: 6-states.sql
   - Creates the database hbtn_0d_usa and the table states (id INT, name VARCHAR) on the specified MySQL server.

8. **Cities Table**
   - Script: 7-cities.sql
   - Creates the database hbtn_0d_usa and the table cities (id INT, state_id INT, name VARCHAR) with a foreign key on state_id on the specified MySQL server.

9. **Cities of California**
   - Script: 8-cities_of_california_subquery.sql
   - Lists all cities of California from the hbtn_0d_usa database without using the JOIN keyword.

10. **Cities by States**
    - Script: 9-cities_by_state_join.sql
    - Lists all cities from the hbtn_0d_usa database with corresponding states without using more than one SELECT statement.

11. **Genre ID by Show**
    - Script: 10-genre_id_by_show.sql
    - Lists all shows from hbtn_0d_tvshows with at least one linked genre, displaying title and genre_id.

