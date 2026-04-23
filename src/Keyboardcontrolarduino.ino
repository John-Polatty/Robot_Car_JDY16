/*
 * LAFVIN 4WD Robot - Bluetooth Control 
 * Using your specific motor pin mapping (2, 4, 5, 6)
 */

// Pin mapping from your IR script
const int LEFT_DIR  = 2;
const int LEFT_PWM  = 5;
const int RIGHT_DIR = 4;
const int RIGHT_PWM = 6;

// Speed settings
int driveSpeed = 230; 
int turnSpeed  = 150;

void setup() {
  // JDY-16 Bluetooth speed
  Serial.begin(9600); 

  pinMode(LEFT_DIR,  OUTPUT);
  pinMode(LEFT_PWM,  OUTPUT);
  pinMode(RIGHT_DIR, OUTPUT);
  pinMode(RIGHT_PWM, OUTPUT);

  // Default to stopped
  stopRobot();
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();

    if (command == 'F') { // Forward (W key)
      digitalWrite(LEFT_DIR,  LOW);
      analogWrite(LEFT_PWM,   driveSpeed);
      digitalWrite(RIGHT_DIR, HIGH);
      analogWrite(RIGHT_PWM,  driveSpeed);
    } 
    else if (command == 'B') { // Backward (S key)
      digitalWrite(LEFT_DIR,  HIGH);
      analogWrite(LEFT_PWM,   driveSpeed);
      digitalWrite(RIGHT_DIR, LOW);
      analogWrite(RIGHT_PWM,  driveSpeed);
    } 
    else if (command == 'L') { // Left (A key)
      digitalWrite(LEFT_DIR,  LOW);
      analogWrite(LEFT_PWM,   turnSpeed);
      digitalWrite(RIGHT_DIR, LOW);
      analogWrite(RIGHT_PWM,  turnSpeed);
    } 
    else if (command == 'R') { // Right (D key)
      digitalWrite(LEFT_DIR,  HIGH);
      analogWrite(LEFT_PWM,   turnSpeed);
      digitalWrite(RIGHT_DIR, HIGH);
      analogWrite(RIGHT_PWM,  turnSpeed);
    } 
    else if (command == 'S') { // Stop (Release keys)
      stopRobot();
    }
  }
}

void stopRobot() {
  // Based on your IR_KEYCODE_OK logic
  digitalWrite(LEFT_DIR,  LOW);
  analogWrite(LEFT_PWM,   0);
  digitalWrite(RIGHT_DIR, HIGH);
  analogWrite(RIGHT_PWM,  0);
}