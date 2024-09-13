#Module5Lesson3:Assignments Applying SQL in Python
#1.Gym Database Management with Python and SQL
#Task 1: Add a Member


CREATE TABLE Members (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT,
);
CREATE TABLE WorkoutSessions (
    session_id INT PRIMARY KEY,
    member_id INT,
    session_date DATE,
    session_time VARCHAR(50),
    activity VARCHAR(255),
    FOREIGN KEY (member_id) REFERENCES Members(id)
);


    # Example code structure
def add_member(id, name, age):
    INSERT INTO Members ('id','name','age')
        VALUES ();

     # Error handling for duplicate IDs or other constraints
     # Example code structure
def add_workout_session(member_id, date, duration_minutes, calories_burned):
    INSERT INTO WorkoutSession ('member_id','date','duration_minutes','calories_burned')
            VALUES ();
def update_member_age(member_id, new_age):
    UPDATE WorkoutSessions
    SET name = 'member_id', session_time = 'new_age'
    WHERE session_id = 'member_id';

 # Example code structure
def delete_workout_session(session_id):
    DELETE FROM Members WHERE name = 'session_id';


 def get_members_in_age_range(start_age, end_age):
    SELECT * FROM Members
        WHERE M BETWEEN 'start_age' AND 'end_age';

 def get_members_in_age_range(start_age, end_age):
    SELECT * FROM Members
        WHERE M BETWEEN 'start_age' AND 'end_age';
