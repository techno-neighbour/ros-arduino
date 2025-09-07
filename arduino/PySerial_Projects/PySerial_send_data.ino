int pin = 3;
int data = 0;

void setup() {
  Serial.begin(9600);
  pinMode(pin, INPUT_PULLUP); // activates the internal pullup-resistor
}

void loop() {
  data = digitalRead(pin);

  if (data == LOW) {
    Serial.println("Pressed");
  }
  else {
    Serial.println("Released");
  }
  delay(750);
}
