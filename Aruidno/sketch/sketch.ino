#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN         9          // Configurable, see typical pin layout above
#define SS_PIN          10         // Configurable, see typical pin layout above

MFRC522 mfrc522(SS_PIN, RST_PIN);  // Create MFRC522 instance

int door_ID = 1;

void setup() {
  Serial.begin(9600);   // Initialize serial communications with the PC
  while (!Serial);    // Do nothing if no serial port is opened (added for Arduinos based on ATMEGA32U4)
  SPI.begin();      // Init SPI bus
  mfrc522.PCD_Init();   // Init MFRC522
}

void loop() {
  // Look for new cards
  if ( ! mfrc522.PICC_IsNewCardPresent()) {
    return;
  }

  // Select one of the cards
  if ( ! mfrc522.PICC_ReadCardSerial()) {
    return;
  }

  String msg = String(door_ID) + ":" + getPresentUID();
  Serial.println(msg);
}

String getPresentUID() {
  // Dump UID
  String UIDstring = "";
  for (byte i = 0; i < mfrc522.uid.size; i++) {
    UIDstring = UIDstring + String(mfrc522.uid.uidByte[i]);
  }
  mfrc522.PICC_HaltA();
  return UIDstring;
}



