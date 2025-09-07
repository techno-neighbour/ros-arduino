// Blink the built-in LED on an Arduino 
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);  // Turn the LED on
  delay(3000);                      // Wait for 3 seconds
  digitalWrite(LED_BUILTIN, LOW);   // Turn the LED off
  delay(2000);                      // Wait for 1 second
}