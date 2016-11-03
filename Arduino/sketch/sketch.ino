#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN         9          // Configurable, see typical pin layout above
#define SS_PIN          10         // Configurable, see typical pin layout above

#define RED_PIN         3
#define GREEN_PIN       5
#define BUZZER          2

MFRC522 mfrc522(SS_PIN, RST_PIN);  // Create MFRC522 instance
char* door_ID = "1";
char key[] = {'K', 'C', 'Q', 'W','K', 'C', 'Q', 'W','K', 'C', 'Q', 'W','K', 'C', 'Q', 'W','K', 'C', 'Q', 'W','K', 'C', 'Q', 'W','K', 'C', 'Q', 'W','K', 'C', 'Q', 'W','K', 'C', 'Q', 'W','K', 'C', 'Q', 'W','K', 'C', 'Q', 'W','K', 'C', 'Q', 'W','K', 'C', 'Q', 'W','K', 'C', 'Q', 'W','K', 'C', 'Q', 'W','K', 'C', 'Q', 'W','K', 'C', 'Q', 'W','K', 'C', 'Q', 'W','K', 'C', 'Q', 'W','K', 'C', 'Q', 'W'}; //Can be any chars, and any size array
char read_key[4] = "";

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
    getPresentUID();
    handleNewCard();
  }
}

void serialEvent(){
  // say what you got:
  String receivedStr;

  while(Serial.available()) {
    delay(3);
    if (Serial.available()>0){
      char c = Serial.read();
      receivedStr += c;
    }
  }

  if(receivedStr.length() > 0){
    char received[receivedStr.length()];
    receivedStr.toCharArray(received, receivedStr.length());
    printToSerial(received);
    handleInput(received);
  }
}


void setupDoor() {
  char msg1[127];
  strcpy(msg1, "door:");
  strcat(msg1, door_ID);
  strcat(msg1, ",status:online");
  printToSerial(msg1);
}

void handleNewCard(){
  char msg1[127];
  strcpy(msg1, "door:");
  strcat(msg1, door_ID);
  strcat(msg1, ",key:");
  strcat(msg1, read_key);
  
  printToSerial(msg1);
  readTone();
}

void getPresentUID() {
  int i;
  for(i = 0; i < mfrc522.uid.size; i++) {
    read_key[i] = mfrc522.uid.uidByte[i] ^ key[i % (sizeof(key)/sizeof(char))];
  }
  mfrc522.PICC_HaltA();
}

void printToSerial(char* msg){
  Serial.println(msg);
}

void handleInput(String input){
  String keypair1 = getValue(input, ',', 1);
  if (keypair1 != ""){
    String key1 = getValue(keypair1, ':', 0);
    String value1 = getValue(getValue(keypair1, ':', 1), '!', 0);
    if(key1.equals("key") && value1 == read_key + '!'){
      String keypair2 = getValue(input, ',', 2);
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
  clean(read_key);
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
  clean(read_key);
}

void unallowedEntry(){
  digitalWrite(RED_PIN, LOW);
  errorTone();
  digitalWrite(RED_PIN, HIGH);
}

void clean(char *var) {
    int i = 0;
    while(var[i] != '\0') {
        var[i] = '\0';
        i++;
    }
}

