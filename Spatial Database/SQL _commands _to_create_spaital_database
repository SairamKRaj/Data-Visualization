Table creation command:
  
  CREATE EXTENSION postgis;

Table – LOCATION_COORDS (Containing the longitude and latitude co-ordinates of the above locations):

  CREATE TABLE LOCATION_COORDS(ID SMALLINT PRIMARY KEY,LNAME VARCHAR(15),LADDRESS varchar(50),Point_coordinates POINT);

Listing the tables present in the postgres instance:

  \dt

Inserting the location co-ordinate (latitudes and longitudes) values into the table:

  INSERT INTO LOCATION_COORDS VALUES (1, 'HOME', '875W 23RD St', POINT(-118.279541,34.033416));
  INSERT INTO LOCATION_COORDS VALUES (2, '23RD St Cafe', '936W 23rd St Los Angeles CA 90007', POINT(-118.280984,34.033719));
  INSERT INTO LOCATION_COORDS VALUES (3, 'PapaJohnsHoover', '2222 S Hoover St Los Angeles CA 90007', POINT(-118.283735,34.035441));
  INSERT INTO LOCATION_COORDS VALUES (4, 'Lorenzo', '325 W Adams Blvd Los Angeles CA 90007', POINT(-118.273153,34.028614));
  INSERT INTO LOCATION_COORDS VALUES (5, 'SaintMarysDohenyCampus', '10 Chester Pl Los Angeles CA 90007', POINT(-118.277695,34.031396));
  INSERT INTO LOCATION_COORDS VALUES (7, 'AoL Foundation', '948 W Adams Blvd Los Angeles CA 90007', POINT(-118.282983,34.031143));
  INSERT INTO LOCATION_COORDS VALUES (8, 'USCFoundersAPT', '2610 Portland St Los Angeles CA 90007', POINT(-118.282058,34.030543));
  INSERT INTO LOCATION_COORDS VALUES (9, 'NorwoodSchool', '2020 Oak St Los Angeles CA 90007', POINT(-118.278749,34.035146));
  INSERT INTO LOCATION_COORDS VALUES (10, 'NaturesBrewCafe', '2316 S Union Ave Los Angeles CA 90007', POINT(-118.283520,34.034662));
  INSERT INTO LOCATION_COORDS VALUES (11, 'PetesBurger', '2400 Hoover St Los Angeles CA 90007', POINT(-118.283805,34.034148));
  
Display Table (LOCATION_COORDS) Contents:

  SELECT * FROM LOCATION_COORDS;  
