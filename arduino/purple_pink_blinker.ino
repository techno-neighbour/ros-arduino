int r = 9;
int g = 10;
int b = 11;

void setup() {
  pinMode(r, OUTPUT);
  pinMode(g, OUTPUT);
  pinMode(b, OUTPUT);
}

void loop() {
  analogWrite(r, 200);
  analogWrite(g, 192);
  analogWrite(b, 203);
  delay(1000);

  analogWrite(r, 157);
  analogWrite(g, 0);
  analogWrite(b, 255);
  delay(500);
}
