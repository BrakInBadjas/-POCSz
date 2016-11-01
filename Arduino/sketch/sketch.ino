#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN         9          // Configurable, see typical pin layout above
#define SS_PIN          10         // Configurable, see typical pin layout above

#define RED_PIN         3
#define GREEN_PIN       5

MFRC522 mfrc522(SS_PIN, RST_PIN);  // Create MFRC522 instance

int door_ID = 1;

void setup() {
  setupLights();
  
  Serial.begin(9600);   // Initialize serial communications with the PC
  while (!Serial);    // Do nothing if no serial port is opened (added for Arduinos based on ATMEGA32U4)
  SPI.begin();      // Init SPI bus
  mfrc522.PCD_Init();   // Init MFRC522
  setupDoor();
}

void loop() {
  // Look for new cards
  if (mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial()) {
    handleNewCard(getPresentUID());
  }

  // say what you got:
  String received = Serial.readString();
  if(received != ""){
    printToSerial(received);
  }
}

void setupDoor() {
  String msg = "door:"+ String(door_ID) +",status:online";
  printToSerial(msg);
}

void handleNewCard(String UID){
  String msg = "door:" + String(door_ID) + ",key:" + UID;
  printToSerial(msg);
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

String encryptMsg(String msg){
  return msg;
}

void printToSerial(String msg){
  Serial.println(encryptMsg(msg));
}

void setupLights(){
  pinMode(RED_PIN, OUTPUT);
  pinMode(GREEN_PIN, OUTPUT);
}



