// Automating JDY-16 configuration to Slave Mode (Role 0)
// For Arduino Mega: JDY TX -> Pin 19 (RX1), JDY RX -> Pin 18 (TX1)

void setup() {
  Serial.begin(9600);   // To monitor progress on PC
  Serial1.begin(9600);  // To talk to JDY-16
  
  delay(1000); // Wait for module to stabilize
  
  Serial.println("Starting Auto-Config...");

  // Send AT command to set Role to 0 (Slave/Peripheral)
  // Use "AT+ROLE1" if you needed Master mode, but Role 0 is for Python/Bleak.
  Serial1.print("AT+ROLE0\r\n"); 
  
  // Give it a moment to process
  delay(500);

  // Check for response
  while (Serial1.available()) {
    char c = Serial1.read();
    Serial.write(c); // Should see "+OK" or "OK" in Serial Monitor
  }

  // Optional: Reset module to apply changes
  Serial1.print("AT+RESET\r\n");
  
  Serial.println("\nConfiguration complete. You can now upload your Robot code.");
}

void loop() {
  // Nothing needed here once configured
}