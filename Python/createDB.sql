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
	role_id INT,
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

INSERT INTO Person VALUES (null, '799d91fa5e3c5e4a3f78710c6e742aef91c0cf7890850f1eb3439146e4de3a88', 'Chris Witteveen', 3);
INSERT INTO Person VALUES (null, '247a01d33fe1fcff76be5a5d3fdd0b2096d6b4fed3a4dcd15af912e9bc021f61', 'Milo Cesar', 3);
INSERT INTO Person VALUES (null, '5792327d6be5ae9cb9dd7b1fbba52530992de8057d3fc59d7c1fcdb0e81c4e96 ', 'Danique Lummen', 2);
INSERT INTO Person VALUES (null, '0c02a7316ff5199d880c0b801bac67a654dbb68f26cfae801dc634b622a79184', 'Suzanna Wentzel', 2);
INSERT INTO Person VALUES (null, '7547efa482a345a2530c0e00ae5a443c3b5a31ad85f111debabcdb844a5dcc78', 'Jesper Simon', 1);
INSERT INTO Person VALUES (null, 'ba6cc572469d6318af1ad510f24bce71156f2a5ca47aa2f70b43af71da81db08', 'Apostolis Christoulias', 1);

INSERT INTO Door VALUES (null, '123');

INSERT INTO Person_Door VALUES (1, 1);

INSERT INTO Role_Door VALUES (2, 1);