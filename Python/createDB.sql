DROP TABLE IF EXISTS Person_Door;
DROP TABLE IF EXISTS Role_Door;
DROP TABLE IF EXISTS Person;
DROP TABLE IF EXISTS Door;
DROP TABLE IF EXISTS Role;

CREATE TABLE Role (
	id INT NOT NULL,
	name TEXT NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE Person (
	id INT NOT NULL,
	key_uid TEXT NOT NULL,
	name TEXT NOT NULL,
	role_id INT NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (role_id) REFERENCES Role(id)
);

CREATE TABLE Door (
	id INT NOT NULL,
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

INSERT INTO Role VALUES (0, 'Client');
INSERT INTO Role VALUES (1, 'Nurse');
INSERT INTO Role VALUES (2, 'Doctor');

INSERT INTO Person VALUES (0, 'DC 7C 98 1E', 'Chris Witteveen', 0);
INSERT INTO Person VALUES (1, 'AD 3B 4E 12', 'Milo Cesar', 0);
INSERT INTO Person VALUES (2, '61 D2 E1 C4', 'Danique Lummen', 1);
INSERT INTO Person VALUES (3, '82 DE C1 44', 'Suzanna Wentzel', 1);
INSERT INTO Person VALUES (4, '8D 52 7F CA', 'Jesper Simon', 2);
INSERT INTO Person VALUES (5, '1B 53 DE 4E', 'Apostolis Christoulias', 2);