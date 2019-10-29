int output_lift1 = 3;
int output_lift2 = 5;
int output_left1 = 6;
int output_left2 = 9;
int output_right1 = 10;
int output_right2 = 11;



void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(output_lift1, OUTPUT);
  pinMode(output_lift2, OUTPUT);
  pinMode(output_left1, OUTPUT);
  pinMode(output_left2, OUTPUT);
  pinMode(output_right1, OUTPUT);
  pinMode(output_right2, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  int val = 128;
  int input_lift1 = analogRead(A0);
  int input_lift2 = analogRead(A1);
  int input_left1 = analogRead(A2);
  int input_left2 = analogRead(A3);
  int input_right1 = analogRead(A4);
  int input_right2 = analogRead(A5);

  if (analogRead(A0) == 1){
   for(int i = 0; i < val; i = i + 2){
     Serial.print(val);
     analogWrite(output_lift1, i);
   }
   while(analogRead(A0) == 1){}
   for(int i = val; i <= 0; i = i - 2){
     analogWrite(output_lift1, i);
   }
  }
  else {
   digitalWrite(output_lift1, LOW);
  }

  if (analogRead(A1) == 1)){
   for(int i = 0; i < val; i = i + 2){
     Serial.print(val);
     analogWrite(output_lift2, i);
   }
   while(analogRead(A1) == 1)){}
   for(int i = val; i <= 0; i = i - 2){
     analogWrite(output_lift2, i);
   }
  }
  else {
   digitalWrite(output_lift2, LOW);
  }

  if (analogRead(A2) == 1)){
   for(int i = 0; i < val; i = i + 2){
     Serial.print(val);
     analogWrite(output_left1, i);
   }
   while(analogRead(A2) == 1)){}
   for(int i = val; i <= 0; i = i - 2){
     analogWrite(output_left1, i);
   }
  }
  else {
   digitalWrite(output_left1, LOW);
  }

  if (analogRead(A3) == 1)){
   for(int i = 0; i < val; i = i + 2){
     Serial.print(val);
     analogWrite(output_left2, i);
   }
   while(analogRead(A3) == 1)){}
   for(int i = val; i <= 0; i = i - 2){
     analogWrite(output_left2, i);
   }
  }
  else {
   digitalWrite(output_left2, LOW);
  }

  if (analogRead(A4) == 1)){
   for(int i = 0; i < val; i = i + 2){
     Serial.print(val);
     analogWrite(output_right1, i);
   }
   while(analogRead(A4) == 1)){}
   for(int i = val; i <= 0; i = i - 2){
     analogWrite(output_right1, i);
   }
  }
  else {
   digitalWrite(output_right1, LOW);
  }

  if (analogRead(A5) == 1)){
   for(int i = 0; i < val; i = i + 2){
     Serial.print(val);
     analogWrite(output_right2, i);
   }
   while(analogRead(A5) == 1)){}
   for(int i = val; i <= 0; i = i - 2){
     analogWrite(output_right2, i);
   }
  }
  else {
   digitalWrite(output_right2, LOW);
  }

}
