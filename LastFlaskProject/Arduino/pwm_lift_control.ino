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

  Serial.println(input_lift1);
  Serial.println(input_lift2);
  Serial.println(input_left1);
  Serial.println(input_left2);
  Serial.println(input_right1);
  Serial.println(input_right2);

  //blank
  
  /*
  전체를 if와 else if문으로 모든 조건 걸어주는 하드 코딩
  or status 변수를 이용한 코딩
  */

}
