//LDR
#define LDR A0

void setup() {
  Serial.begin(9600);
}

void loop() {
  int light = map(analogRead(LDR), 0, 1023, 0, 100);

  //Light output
  Serial.println(light);
}