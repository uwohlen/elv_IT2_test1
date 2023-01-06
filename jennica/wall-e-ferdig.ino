#include <Servo.h>
Servo s1, s2;
int pin1 = 3;
int pin2 = 5;

int venstrefart = 1000;
int hoeyrefart = 2000;
#define echoPin 10  
#define trigPin 11

float airspeed = 0.034;
/*340 m/s = 34 000 cm/s = 34 cm/ms = 0.034 cm/µs*/

float duration, distance; 



void setup() {
  // put your setup code here, to run once:
 pinMode(pin1, OUTPUT);
 pinMode(pin2, OUTPUT);
 s1.attach(pin1);
 s2.attach(pin2);
 s1.write(90);
 s2.write(90);
 
 pinMode(echoPin, INPUT);
 pinMode(trigPin, OUTPUT);
 Serial.begin(9600); 
}


void loop() {
kjor();
avstand();
sjekkOmTreff();
}

void avstand(){
  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH); //mikrosekunder
  distance = airspeed * duration/2;
  Serial.println(String(distance));
  delay(1000);
  }

void kjor(){
  s2.writeMicroseconds(venstrefart);
  s1.writeMicroseconds(hoeyrefart);
}

void sjekkOmTreff(){
  if (distance < 13){
    venstrefart = 2000;
    hoeyrefart = 1500;
  }
  else{
    venstrefart = 1000;
    hoeyrefart = 2000;
  }
}
