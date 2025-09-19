int ena = 5;
int in1 = 6;
int in2 = 7;

int enb = 11;
int in3 = 12;
int in4 = 13;

void setup() {
  pinMode(ena, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);

  pinMode(enb, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);

  Serial.begin(9600);
}

void loop() {
  char input = Serial.read();

  if (input == '1') {
    // Forward
    Serial.println("Forward");
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    digitalWrite(in3, HIGH);
    digitalWrite(in4, LOW);
    analogWrite(ena, 106.25);
    analogWrite(enb, 75);
    delay(4000);
  }

  else if (input == '2') {
    // Backward
    Serial.println("Backward");
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
    digitalWrite(in3, LOW);
    digitalWrite(in4, HIGH);
    analogWrite(ena, 106.25);
    analogWrite(enb, 75);
    delay(4000);
  }

  else if (input == '3') {
    // Left turn (left motor stop, right motor forward)
    Serial.println("Left");
    digitalWrite(in1, LOW);
    digitalWrite(in2, LOW);
    digitalWrite(in3, HIGH);
    digitalWrite(in4, LOW);
    analogWrite(ena, 0);     // Left motor OFF
    analogWrite(enb, 75);   // Right motor ON
    delay(4000);
  }

  else if (input == '4') {
    // Right turn (right motor stop, left motor forward)
    Serial.println("Right");
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    digitalWrite(in3, LOW);
    digitalWrite(in4, LOW);
    analogWrite(ena, 106.25);   // Left motor ON
    analogWrite(enb, 0);     // Right motor OFF
    delay(4000);
  }

  // Stop motors after each move
  analogWrite(ena, 0);
  analogWrite(enb, 0);
}
