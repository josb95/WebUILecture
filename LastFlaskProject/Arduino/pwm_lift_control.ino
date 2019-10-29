int input_lift1 = 1;
int input_lift2 = 2;
int input_left1 = 7;
int input_left2 = 8;
int input_right1 = 12;
int input_right2 = 13;
int output_lift1 = 3;
int output_lift2 = 5;
int output_left1 = 6;
int output_left2 = 9;
int output_right1 = 10;
int output_right2 = 11;
// int val = 0;


void setup() {
  // put your setup code here, to run once:
  pinMode(input_lift1, OUTPUT);
  pinMode(input_lift2, OUTPUT);
  pinMode(input_left1, OUTPUT);
  pinMode(input_left2, OUTPUT);
  pinMode(input_right1, OUTPUT);
  pinMode(input_right2, OUTPUT);
  pinMode(output_lift1, OUTPUT);
  pinMode(output_lift2, OUTPUT);
  pinMode(output_left1, OUTPUT);
  pinMode(output_left2, OUTPUT);
  pinMode(output_right1, OUTPUT);
  pinMode(output_right2, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  if (digitalRead(input_lift1) == HIGH){
   for(int i = 0; i < 60; i = i + 2){
     analogWrite(output_lift1, i);
   }
   while(digitalRead(input_lift1) == HIGH){}
   for(int i = 60; i <= 0; i = i - 2){
     analogWrite(output_lift1, i);
   }
  }
  else {
   digitalWrite(output_lift1, LOW);
  }

  if (digitalRead(input_lift2) == HIGH){
   for(int i = 0; i < 60; i = i + 2){
     analogWrite(output_lift2, i);
   }
   while(digitalRead(input_lift2) == HIGH){}
   for(int i = 60; i <= 0; i = i - 2){
     analogWrite(output_lift2, i);
   }
  }
  else {
   digitalWrite(output_lift2, LOW);
  }

  if (digitalRead(input_left1) == HIGH){
   for(int i = 0; i < 60; i = i + 2){
     analogWrite(output_left1, i);
   }
   while(digitalRead(input_left1) == HIGH){}
   for(int i = 60; i <= 0; i = i - 2){
     analogWrite(output_left1, i);
   }
  }
  else {
   digitalWrite(output_left1, LOW);
  }

  if (digitalRead(input_left2) == HIGH){
   for(int i = 0; i < 60; i = i + 2){
     analogWrite(output_left2, i);
   }
   while(digitalRead(input_left2) == HIGH){}
   for(int i = 60; i <= 0; i = i - 2){
     analogWrite(output_left2, i);
   }
  }
  else {
   digitalWrite(output_left2, LOW);
  }

  if (digitalRead(input_right1) == HIGH){
   for(int i = 0; i < 60; i = i + 2){
     analogWrite(output_right1, i);
   }
   while(digitalRead(input_right1) == HIGH){}
   for(int i = 60; i <= 0; i = i - 2){
     analogWrite(output_right1, i);
   }
  }
  else {
   digitalWrite(output_right1, LOW);
  }

  if (digitalRead(input_right2) == HIGH){
   for(int i = 0; i < 60; i = i + 2){
     analogWrite(output_right2, i);
   }
   while(digitalRead(input_right2) == HIGH){}
   for(int i = 60; i <= 0; i = i - 2){
     analogWrite(output_right2, i);
   }
  }
  else {
   digitalWrite(output_right2, LOW);
  }

}
