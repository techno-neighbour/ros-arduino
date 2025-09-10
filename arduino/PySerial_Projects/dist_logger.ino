int trig = 9;
int echo = 10;
int led = 3;

void setup() {
  Serial.begin(9600);
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  pinMode(led, OUTPUT);
}

void loop() {
  digitalWrite(trig, LOW);
  delayMicroseconds(2);

  digitalWrite(trig, HIGH);
  delayMicroseconds(30);
  digitalWrite(trig, LOW);

  long time = pulseIn(echo, HIGH);
  float dist = time*0.017;
  dist = dist + 0.3;

  if (dist < 10) {
    digitalWrite(led, HIGH);
    delay(60);
    digitalWrite(led, LOW);
  }

  else {
    digitalWrite(led, LOW);
  }

  Serial.println(dist);
  delay(500);
}
