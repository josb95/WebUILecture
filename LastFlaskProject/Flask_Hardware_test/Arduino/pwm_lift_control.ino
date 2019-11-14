int output_lift1 = 3;
int output_lift_pwm = 4;
int output_lift2 = 5;
int output_left1 = 6;
int output_left2 = 9;
int output_right1 = 10;
int output_right2 = 11;



void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(output_lift1, OUTPUT);
  pinMode(output_lift_pwm, OUTPUT);
  pinMode(output_lift2, OUTPUT);
  pinMode(output_left1, OUTPUT);
  pinMode(output_left2, OUTPUT);
  pinMode(output_right1, OUTPUT);
  pinMode(output_right2, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  int val = 100;
  int input_lift1 = analogRead(A0);
  int input_lift2 = analogRead(A1);
  int input_left1 = analogRead(A2);
  int input_left2 = analogRead(A3);
  int input_right1 = analogRead(A4);
  int input_right2 = analogRead(A5);

  // Serial.println(input_lift1);
  // Serial.println(input_lift2);
  // Serial.println(input_left1);
  // Serial.println(input_left2);
  // Serial.println(input_right1);
  // Serial.println(input_right2);

  if (analogRead(A2) > 200 && analogRead(A4) > 200){
    analogWrite(output_left1, val);
    analogWrite(output_right1, val);
    while (analogRead(A2) > 200 && analogRead(A4) > 200) {}
    digitalWrite(output_left1, LOW);
    digitalWrite(output_right1, LOW);
  }
  else if (analogRead(A3) > 200 && analogRead(A5) > 200){
    analogWrite(output_left2, val);
    analogWrite(output_right2, val);
    while (analogRead(A3) > 200 && analogRead(A5) > 200) {}
    digitalWrite(output_left2, LOW);
    digitalWrite(output_right2, LOW);
  }
  else if (analogRead(A2) > 200){
    analogWrite(output_left1, val);
    while (analogRead(A2) > 200){}
    digitalWrite(output_left1, LOW);
  }
  else if (analogRead(A3) > 200){
    analogWrite(output_left2, val);
    while (analogRead(A3) > 200){}
    digitalWrite(output_left2, LOW);
  }
  else if (analogRead(A4) > 200){
    analogWrite(output_right1, val);
    while (analogRead(A4) > 200){}
    digitalWrite(output_right1, LOW);
  }
  else if (analogRead(A5) > 200){
    analogWrite(output_right2, val);
    while (analogRead(A5) > 200){}
    digitalWrite(output_right2, LOW);
  }

  if (analogRead(A0) > 200){
    analogWrite(output_lift_pwm, val);
    digitalWrite(output_lift1, HIGH);
    while (analogRead(A0) > 200){}
    digitalWrite(output_lift1, LOW);
  }
  else if (analogRead(A1) > 200){
    analogWrite(output_lift_pwm, val);
    digitalWrite(output_lift2, HIGH);
    while (analogRead(A1) > 200){}
    digitalWrite(output_lift2, LOW);
  }

}
