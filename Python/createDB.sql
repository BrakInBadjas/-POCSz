DROP TABLE IF EXISTS Person_Door;
DROP TABLE IF EXISTS Role_Door;
DROP TABLE IF EXISTS Person;
DROP TABLE IF EXISTS Door;
DROP TABLE IF EXISTS Role;

CREATE TABLE Role (
    id INT NOT NULL AUTO_INCREMENT,
    name TEXT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE Person (
	id INT NOT NULL AUTO_INCREMENT,
	key_uid TEXT NOT NULL,
	name TEXT NOT NULL,
	role_id INT NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (role_id) REFERENCES Role(id)
);

CREATE TABLE Door (
	id INT NOT NULL AUTO_INCREMENT,
	public_key TEXT NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE Role_Door (
	role_id INT NOT NULL,
	door_id INT NOT NULL,
	PRIMARY KEY (role_id, door_id),
	FOREIGN KEY (role_id) REFERENCES Role(id),
	FOREIGN KEY (door_id) REFERENCES Door(id)
);

CREATE TABLE Person_Door (
	person_id INT NOT NULL,
	door_id INT NOT NULL,
	PRIMARY KEY (person_id, door_id),
	FOREIGN KEY (person_id) REFERENCES Person(id),
	FOREIGN KEY (door_id) REFERENCES Door(id)
);

INSERT INTO Role VALUES (null, 'Client');
INSERT INTO Role VALUES (null, 'Nurse');
INSERT INTO Role VALUES (null, 'Doctor');

INSERT INTO Person VALUES (null, 'DC 7C 98 1E', 'Chris Witteveen', 3);
INSERT INTO Person VALUES (null, 'AD 3B 4E 12', 'Milo Cesar', 3);
INSERT INTO Person VALUES (null, '61 D2 E1 C4', 'Danique Lummen', 2);
INSERT INTO Person VALUES (null, '82 DE C1 44', 'Suzanna Wentzel', 2);
INSERT INTO Person VALUES (null, '8D 52 7F CA', 'Jesper Simon', 1);
INSERT INTO Person VALUES (null, '1B 53 DE 4E', 'Apostolis Christoulias', 1);