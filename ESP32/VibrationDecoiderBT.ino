
//This example code is in the Public Domain (or CC0 licensed, at your option.)
//By Evandro Copercini - 2018
//
//This example creates a bridge between Serial and Classical Bluetooth (SPP)
//and also demonstrate that SerialBT have the same functionalities of a normal Serial

#include "BluetoothSerial.h"

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

BluetoothSerial SerialBT;

const int LED_BUILTIN = 2;
const int motorPin = 15;

void setup() {
  Serial.begin(9600);
  SerialBT.begin("ESP32_SinesTA"); //Bluetooth device name
  Serial.println("The device started, now you can pair it with bluetooth!");
  SerialBT.available();
  
  pinMode (LED_BUILTIN, OUTPUT);
  pinMode (motorPin, OUTPUT);
  
  digitalWrite(LED_BUILTIN, HIGH);
}

void short_vibration(){
  digitalWrite(motorPin, HIGH); // Liga Vibração
  delay(3000); // Aguarda 3 centésimos segundos
  digitalWrite(motorPin, LOW); // Desliga Vibração
}

void long_vibration(){
  digitalWrite(motorPin, HIGH);
  delay(5000); //Aguarda 1 segundo
  digitalWrite(motorPin, LOW);
}

void loop() {
  if (SerialBT.available()) {
    int message = SerialBT.read();
    Serial.write(message);
    
    
    switch (message) {
    case 65: //A = ascii dec 65
      //1 Vibração Curta
      short_vibration();
      break;
    
    case 66: //B
      //2 Vibrações Curtas
      short_vibration();
      delay(300);
      short_vibration();
      break;
    
    case 67: //C
      //1 Vibração Longa
      long_vibration();
      break;
    
    case 68: //D
      //2 Vibrações Longas
      long_vibration();
      delay(300);
      long_vibration();
      break;
      
    case 69: //E
      //1 Vibração curta + 1 Vibração Longa
      short_vibration();
      delay(300);
      long_vibration();
      break;
    }
  delay(20);
  }
}