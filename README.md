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

- PIP (For installing dependencies)
- pycrypto
- PyMySQL
- pySerial

# Arduino Requirements
### Libraries
- MFRC522

# Instalation
1. Install the pyton requirements
2. Install the arduino requirements
3. Upload the [sketch.ino](/Arduino/sketch/sketch.ino) to the Arduino
4. Change the values in [db.py](/Python/db.py) and [readSerial.py](/Python/readSerial.py) to reflect your current environment and the db settings
5. Run [readSerial.py](/Python/readSerial.py)

# Hardware setup
## RDIF
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

# Database Requirements
A database running MySQL

# Database setup
1. Run [create.py](/Python/create.py)
    alternatively run [createDB.sql](/Python/createDB.sql) on your database
