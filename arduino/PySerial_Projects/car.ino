//-------------------- PIN DEFINITIONS --------------------
int led = 3;
int stby = 8;

int trig = 2;
int echo = 4;

int ain1 = 5;
int ain2 = 6;

int bin1 = 9;
int bin2 = 10;

const int bPin = A0;
float R1 = 10000.0;
float R2 = 10000.0;
//-------------------- TIMING --------------------
unsigned long last = 0;
const unsigned long interval = 500; // ms
//-------------------- SETUP --------------------
void setup() {
  Serial.begin(9600);

  pinMode(led, OUTPUT);
  pinMode(stby, OUTPUT);

  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);

  pinMode(ain1, OUTPUT);
  pinMode(ain2, OUTPUT);

  pinMode(bin1, OUTPUT);
  pinMode(bin2, OUTPUT);

  digitalWrite(stby, HIGH);
}

//-------------------- MOTOR FUNCTIONS --------------------
void forward() {
  Serial.println("Forward");
  analogWrite(ain1, 175);
  digitalWrite(ain2, LOW);
  analogWrite(bin1, 175);
  digitalWrite(bin2, LOW);
}

void backward() {
  Serial.println("Backward");
  digitalWrite(ain1, LOW);
  analogWrite(ain2, 175);
  digitalWrite(bin1, LOW);
  analogWrite(bin2, 175);
}

void left() {
  Serial.println("Left");
  digitalWrite(ain1, LOW);
  digitalWrite(ain2, LOW);
  analogWrite(bin1, 175);
  digitalWrite(bin2, LOW);
}

void right() {
  Serial.println("Right");
  analogWrite(ain1, 175);
  digitalWrite(ain2, LOW);
  digitalWrite(bin1, LOW);
  digitalWrite(bin2, LOW);
}

void stop() {
  Serial.println("No");
  analogWrite(ain1, 0);
  analogWrite(ain2, 0);
  analogWrite(bin1, 0);
  analogWrite(bin2, 0);
}
//------------------------- VOLTAGE -------------------------
String voltage() {
  int get = analogRead(bPin);
  float div_val = R2 /(R1 + R2);
  float conv = get * (5.0/1023.0) ;
  float volt = conv / div_val ;
  volt = volt + 0.25 ;

  String volt_str = String(volt);
  volt_str = volt_str+"V";

  return volt_str;
}
//-------------------- ULTRASONIC SENSOR --------------------
float readUltrasonic() {
  // Trigger pulse
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);

  // No-block pulse read
  long duration = pulseIn(echo, HIGH, 30000); // 30ms timeout
  if (duration == 0) return -1; // no echo
  float distance = duration * 0.01715; // cm
  distance += 0.3; // calibration
  return distance;
}

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
  //----------------- SENSOR, VOLTAGE, LED -----------------
  unsigned long now = millis();
  if (now - last >= interval) {
    last = now;
    float dist = readUltrasonic();
    String volt = voltage();
    Serial.println(volt);
    if (dist > 0) {
      Serial.println(dist);
      if (dist < 10) digitalWrite(led, HIGH);
      else digitalWrite(led, LOW);
    }
  }
}
