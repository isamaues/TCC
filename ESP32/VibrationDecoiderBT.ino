
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
  delay(450); // Aguarda 0.5 segundos
  digitalWrite(motorPin, LOW); // Desliga Vibração
}

void long_vibration(){
  digitalWrite(motorPin, HIGH);
  delay(700); //Aguarda 1 segundo
  digitalWrite(motorPin, LOW);
}

void loop() {
  if (SerialBT.available()) {
    int message = SerialBT.read();
    Serial.write(message);
    
    switch (message) {
    case '1': // 1 - Jogador 1 faz um ponto
      long_vibration();
      delay(300);
      short_vibration();
      break;
    
    case '2': // 2 - Jogador 2 faz um ponto
      long_vibration();
      delay(300);
      short_vibration();
      delay(300);
      short_vibration();
      break;
    
    case '3': // 3 - Bola servida
      long_vibration();
      break;
    
    case '4': // 4 - Bola quica
      short_vibration();
      break;
      
    case '5': // 5 - Fim de jogo
      long_vibration();
      long_vibration();
      break;
    }
    delay(20);
  }
}

// Eventos
// 1 - Jogador 1 faz um ponto
// 2 - Jogador 2 faz um ponto
// 3 - Bola servida
// 4 - Bola quica
// 5 - Fim de jogo