Created By:

| Student                                               | StudentNumber  | E-mail adress
| --------------                                        |:-------------: | -------------------
| [Chris Witteveen] (https://github.com/cwitteveen)     | S1847821       | chriswitteveen2@hotmail.com
| [Milo Cesar](https://github.com/milo526)              | S1829688       | milocesar1@gmail.com
| [Suzanna Wentzel] (https://github.com/SuzannaWentzel) | S1850512       | suzannawentzel1708@gmail.com
| [Danique Lummen](https://github.com/daniquel)         | S1853155       | daniquelummen@gmail.com
| Jesper Simon                                          | S1820338       | jespersimon@live.nl
| Apostolis Christoulias                                | S1833383       | apochri@hotmail.com


# Python Requirements
Please make sure you have microsoft visual studio 2015 installed

- PIP (For installing dependencies)
- PyMySQL
- pySerial
- Kivy

=======

# Arduino Requirements
### Libraries
- MFRC522

# Installation
=======
# Software installation
For MAC:
 1. Install the python requirements
 2. Install the arduino requirements
 3. Upload the [sketch.ino](/Arduino/sketch/sketch.ino) to the Arduino
 4. Change the values in [db.py](/Python/db.py) and [readSerial.py](/Python/readSerial.py) to reflect your current environment and the db settings
 5. Run [readSerial.py](/Python/readSerial.py)

For Windows:
 1. Run setup.bat to install python requirements\n
    If there are problems with the Kivy installation, check the installation of Microsoft Visual Studio. Microsoft Visual Studio 2015 is required. 
 2. Install the arduino requirements
 3. Upload the [sketch.ino](/Arduino/sketch/sketch.ino) to the Arduino
 4. Change the values in [db.py](/Python/db.py) and [readSerial.py](/Python/readSerial.py) to reflect your current environment and the db settings
 5. Run [readSerial.py](/Python/readSerial.py)


# Hardware setup
## RFID
| Connect arduino pin   | Connect To    |
|:------------------:   |:---------:    |
| 9                     |RFID RST       |
| 10                    |RFID SDA       |
| 11                    |RFID MOSI      |
| 12                    |RFID MISO      |
| 13                    |RFID SCK       |
| 3.3V                  |RFID 3.3V      |
| GND                   |RFID GND       |

## Extra's
| Connect arduino pin   | Connect To    |
|:------------------:   |:---------:    |
| 2                     | Buzzer 5V     |
| GND                   | Buzzer Ground |
| 3                     | Red LED +     |
| GND                   | Red LED GND   |
| 5                     | Green LED +   |
| GND                   | Green LED GND |

=======
# Database Requirements
A database running MySQL

# Database setup
1. Change the values in [create.py](/Python/create.py) to match your database settings
2. Run [create.py](/Python/create.py)

alternatively run [createDB.sql](/Python/createDB.sql) on your database
