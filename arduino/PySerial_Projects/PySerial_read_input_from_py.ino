int r = 3;
int g = 4;
int b = 5;
char input;
void setup() {
  Serial.begin(9600);
  pinMode(r, OUTPUT);
  pinMode(g, OUTPUT);
  pinMode(b, OUTPUT);

}

void loop() {
    input = Serial.read();
    if (input == 'r') {
      digitalWrite(r, HIGH);
      digitalWrite(g, LOW);
      digitalWrite(b, LOW);
      Serial.println("LED ON: RED");
    }
    else if (input == 'g') {
      digitalWrite(g, HIGH);
      digitalWrite(r, LOW);
      digitalWrite(b, LOW);
      Serial.println("LED ON: GREEN");
    }

    else if (input == 'b') {
      digitalWrite(b, HIGH);
      digitalWrite(g, LOW);
      digitalWrite(r, LOW);
      Serial.println("LED ON: BLUE");
    }

    else if (input == '0') {
      digitalWrite(b, LOW);
      digitalWrite(g, LOW);
      digitalWrite(r, LOW);
      Serial.println("LED ON: NIL");
    }

    else if (input == '1') {
      digitalWrite(r, HIGH);
      delay(300);
      digitalWrite(r, LOW);

      // Green ON
      digitalWrite(g, HIGH);
      delay(300);
      digitalWrite(g, LOW);

      // Blue ON
      digitalWrite(b, HIGH);
      delay(300);
      digitalWrite(b, LOW);

      // Backwards
      digitalWrite(g, HIGH);
      delay(300);
      digitalWrite(g, LOW);

      digitalWrite(r, HIGH);
      delay(300);
      digitalWrite(r, LOW);
    }
}
