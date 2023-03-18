#include <Arduino.h>
#include <SoftwareSerial.h>
#include <WiFly.h>
#include "HTTPClient.h"

#define SSID      "myssid"
#define KEY       "mypassword"
// WIFLY_AUTH_OPEN / WIFLY_AUTH_WPA1 / WIFLY_AUTH_WPA1_2 / WIFLY_AUTH_WPA2_PSK
#define AUTH      WIFLY_AUTH_WPA2_PSK



   
#define HTTP_POST_URL "http://IPADDRESS/physcatch/callservergsr.php"
#define HTTP_POST_DATA "181"

// Pins' connection
// Arduino       WiFly
//  2    <---->    TX
//  3    <---->    RX
SoftwareSerial uart(2, 3);
WiFly wifly(uart);
HTTPClient client;
char get;

const int GSR=A0;
int sensorValue=0;
int gsr_average=0;


void setup() {
  Serial.begin(9600);    
  uart.begin(9600);         // WiFly UART Baud Rate: 9600
  delay(3000);
  Serial.println("Joining " SSID );
  if (wifly.join(SSID, KEY, AUTH)) {
    Serial.println("OK");
    wifly.save();    // save configuration, 
  } else {
    Serial.println("Failed");
  } 
}

void posttohttp(int gsr_average) {
  //Serial.println("\r\nTrying to connect to " HTTP_GET_URL);
  //Serial.println("------------------------------");
  //Serial.print("GSR: ");
  //Serial.println(gsr_average);
   char cstr[16];
   itoa(gsr_average, cstr, 10);
   #ifdef HTTP_POST_DATA //if the macro MEDIAN_MAX_SIZE is defined 
   #undef HTTP_POST_DATA //un-define it
   #define HTTP_POST_DATA cstr  //redefine it with the new value
   #endif 
   while (client.post(HTTP_POST_URL, HTTP_POST_DATA, 10000) < 0) {}
  
 
  while (wifly.receive((uint8_t *)&get, 1, 1000) == 1) {
    Serial.print(get);
  }
}


void loop() {
  int c;
 
 long sum=0;
  for(int i=0;i<10;i++)           //Average the 10 measurements to remove the glitch
      {
      sensorValue=analogRead(GSR);
      sum += sensorValue;
      delay(5);
      }
   gsr_average = (sum/10)-10;
   int human_resistance = ((1024+2*gsr_average)*10000)/(516-gsr_average);
   //Serial.print("human_resistance = ");
   //Serial.println(human_resistance);
   //Serial.println(gsr_average);
   posttohttp(gsr_average);
   //delay(5000);
}
