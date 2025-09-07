#define ldr A2
int moisture = 0;

void setup() {
  Serial.begin(9600);
  pinMode(A0, OUTPUT);
  pinMode(A1, INPUT);
}

void loop() {
  int light = map(analogRead(ldr), 0, 1023, 0, 100);
  digitalWrite(A0, HIGH);
  delay(10);
  moisture = analogRead(A1);

  digitalWrite(A0, LOW);
  Serial.println(light);
  Serial.println(moisture);

  delay(100);
}