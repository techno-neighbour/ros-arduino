int pin = 3;
int data = 0;
int last = 1;

void setup() {
  Serial.begin(9600);
  pinMode(pin, INPUT_PULLUP); // activates the internal pullup-resistor
}

void loop() {
  data = digitalRead(pin);
  if (data != last) {
    if (data == LOW) {
      Serial.println("Pressed");
    }
    else {
      Serial.println("Released");
    }
    last = data;
    delay(500);
  }
}

