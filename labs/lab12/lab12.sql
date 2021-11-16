.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet from students where color = 'blue' and pet = 'dog';

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song from students where color = 'blue' and pet = 'dog';


CREATE TABLE smallest_int AS
  SELECT smallest from students where smallest > 2 order by LIMIT 20;


CREATE TABLE matchmaker AS
  SELECT s1.pet as pet, s1.song as song, s1.color, s2.color from students as s1, students as s2
  where s1.pet = s2.pet and s1.song = s2.song and s1.time < s2.time;


CREATE TABLE sevens AS
  SELECT seven from students, numbers where students.time = numbers.time and students.number = 7 and number.'7' = True;

