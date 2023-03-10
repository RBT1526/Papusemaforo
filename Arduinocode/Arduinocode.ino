int rojo = 9;
int verde = 7;
int amarillo = 5;
void setup(){
pinMode(amarillo,OUTPUT);
pinMode(verde,OUTPUT);
pinMode(rojo,OUTPUT);
Serial.begin(115200);
digitalWrite(verde,HIGH);
digitalWrite(amarillo,HIGH);
digitalWrite(rojo,HIGH);
}
void loop(){
  if(Serial.available() > 0 ){
      char Dato = Serial.read();
      if(Dato == 'A') {
      digitalWrite(verde,LOW);
    }
      if(Dato == 'B') {
      digitalWrite(amarillo,LOW);
    } 
      if(Dato == 'C') {
      digitalWrite(rojo,LOW);
    }
      if(Dato == 'Z') {
      digitalWrite(verde,HIGH);
    } 
      if(Dato == 'X'){ 
       digitalWrite(amarillo,HIGH);
     } 
      if(Dato == 'Y'){ 
        digitalWrite(rojo,HIGH);
      }
      
  }
}