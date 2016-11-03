#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN         9          // Configurable, see typical pin layout above
#define SS_PIN          10         // Configurable, see typical pin layout above

#define RED_PIN         3
#define GREEN_PIN       5
#define BUZZER          2

MFRC522 mfrc522(SS_PIN, RST_PIN);  // Create MFRC522 instance

char door_ID = '201';
char key[] = {'K', 'C', 'Q', 'W', 'P'}; //Can be any chars, and any size array
String read_key = "";

void setup() {
  setupLights();
  
  Serial.begin(9600);   // Initialize serial communications with the PC
  while (!Serial);    // Do nothing if no serial port is opened (added for Arduinos based on ATMEGA32U4)
  SPI.begin();      // Init SPI bus
  mfrc522.PCD_Init();   // Init MFRC522
  setupDoor();
  digitalWrite(RED_PIN, HIGH);
}

void loop() {
  // Look for new cards
  if (mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial()) {
    handleNewCard(String(getPresentUID()));
  }

  // say what you got:
  String received = Serial.readString();
  if(received != ""){
    printToSerial(received);
    handleInput(received);
  }
}


void setupDoor() {
  String msg = "door:"+ String(door_ID) +",status:online";
  printToSerial(msg);
}

void handleNewCard(String UID){
  read_key = UID;
  
  String msg = "door:" + String(door_ID) + ",key:" + UID;
  printToSerial(msg);
  readTone();
}

String getPresentUID() {
  // Dump UID
  char output[4]; 
  
  int i;
  for(i = 0; i < 4; i++) {
    output[i] = mfrc522.uid.uidByte[i] ^ key[i % (sizeof(key)/sizeof(char))];
  }
  
  mfrc522.PICC_HaltA();
  return String(output);
}

void printToSerial(String msg){
  Serial.println(msg);
}

void handleInput(String msg){
  String keypair1 = getValue(msg, ',', 1);
  if (keypair1 != ""){
    String key1 = getValue(keypair1, ':', 0);
    String value1 = getValue(getValue(keypair1, ':', 1), '!', 0);
    if(key1.equals("key") && value1 == read_key + "!"){
      String keypair2 = getValue(msg, ',', 2);
      String key2 = getValue(keypair2, ':', 0);
      String value2 = getValue(keypair2, ':', 1);
      if(key2.equals("auth")){
        if(getValue(value2, 'e', 0) == "True"){
           allowEntry();
        } else {
          unallowedEntry();
        }
      } else {
        errorTone();
      }
    } else {
      errorTone();
    }
  }
  read_key = ""; 
}

 String getValue(String data, char separator, int index){
  int found = 0;
  int strIndex[] = {0, -1};
  int maxIndex = data.length()-1;

  for(int i=0; i<=maxIndex && found<=index; i++){
    if(data.charAt(i)==separator || i==maxIndex){
        found++;
        strIndex[0] = strIndex[1]+1;
        strIndex[1] = (i == maxIndex) ? i+1 : i;
    }
  }

  return found>index ? data.substring(strIndex[0], strIndex[1]) : "";
}

void setupLights(){
  pinMode(RED_PIN, OUTPUT);
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(BUZZER, OUTPUT);
}

void readTone(){
  tone(BUZZER, 1000);
  delay(100);
  noTone(BUZZER);
  tone(BUZZER, 1500);
  delay(100);
  noTone(BUZZER);
}

void errorTone(){
  tone(BUZZER, 1000);
  delay(200);
  noTone(BUZZER);
  delay(200);
  tone(BUZZER, 1000);
  delay(200);
  noTone(BUZZER);
}

void openTone(){
  tone(BUZZER, 1000); // Send 1KHz sound signal...
  delay(500);        // ...for 3 sec
  noTone(BUZZER);     // Stop sound
}

void closeTone(){
  tone(BUZZER, 1500);
  delay(200);
  noTone(BUZZER);
  tone(BUZZER, 1000);
  delay(200);
  noTone(BUZZER);
}

void allowEntry() {
  digitalWrite(RED_PIN, LOW);
  digitalWrite(GREEN_PIN, HIGH);
  openTone();
  delay(2100);
  closeTone();
  digitalWrite(GREEN_PIN, LOW);
  digitalWrite(RED_PIN, HIGH);
}

void unallowedEntry(){
  digitalWrite(RED_PIN, LOW);
  errorTone();
  digitalWrite(RED_PIN, HIGH);
}

