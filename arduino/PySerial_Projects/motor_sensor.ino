//-------------------- PIN DEFINITIONS --------------------
int led = 3;
int trig = 9;
int echo = 10;

int ena = 5;
int in1 = 6;
int in2 = 7;

int enb = 11;
int in3 = 12;
int in4 = 13;

//-------------------- TIMING --------------------
unsigned long last = 0;
const unsigned long interval = 500; // ms

//-------------------- SETUP --------------------
void setup() {
  Serial.begin(9600);

  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  pinMode(led, OUTPUT);

  pinMode(ena, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);

  pinMode(enb, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
}

//-------------------- MOTOR FUNCTIONS --------------------
void forward() {
  Serial.println("Forward");
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  analogWrite(ena, 106);
  analogWrite(enb, 75);
}

void backward() {
  Serial.println("Backward");
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
  analogWrite(ena, 106);
  analogWrite(enb, 75);
}

void left() {
  Serial.println("Left");
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  analogWrite(ena, 0);
  analogWrite(enb, 75);
}

void right() {
  Serial.println("Right");
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
  analogWrite(ena, 106);
  analogWrite(enb, 0);
}

void stop() {
  Serial.println("No");
  analogWrite(ena, 0);
  analogWrite(enb, 0);
}

//-------------------- ULTRASONIC SENSOR --------------------
float readUltrasonic() {
  // Trigger pulse
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);

  // Non-blocking pulse read
  long duration = pulseIn(echo, HIGH, 30000); // 30ms timeout
  if (duration == 0) return -1; // no echo
  float distance = duration * 0.01715; // cm
  distance += 0.3; // calibration
  return distance;
}

//-------------------- LOOP --------------------
void loop() {
  //----------------- MOTOR CONTROL -----------------
  if (Serial.available() > 0) {
    char input = Serial.read();
    switch (input) {
      case '1': forward(); break;
      case '2': backward(); break;
      case '3': left(); break;
      case '4': right(); break;
      case '0': stop(); break;
    }
  }

  //----------------- SENSOR&LED -----------------
  unsigned long now = millis();
  if (now - last >= interval) {
    last = now;
    float dist = readUltrasonic();
    if (dist > 0) {
      Serial.println(dist);
      if (dist < 10) digitalWrite(led, HIGH);
      else digitalWrite(led, LOW);
    }
  }
}
