#define red_led 6
#define green_led 5
#define blue_led 3

int steps = 20;

int old_red_value = 0;
int old_green_value = 0;
int old_blue_value = 0;

void setup() {
  Serial.begin(9600);

  pinMode(red_led, OUTPUT);
  pinMode(green_led, OUTPUT);
  pinMode(blue_led, OUTPUT);
}


void loop() {
  if (Serial.available() >= 3) { // Wait for 3 bytes
    int new_red_value = Serial.read();   // Read red value
    int new_green_value = Serial.read(); // Read green value
    int new_blue_value = Serial.read();  // Read blue value

    int delta_red_value = new_red_value - old_red_value;
    int delta_green_value = new_green_value - old_green_value;
    int delta_blue_value = new_blue_value - old_blue_value;

    for(int i = 1; i <= steps; i++){
      analogWrite(red_led, old_red_value+(i*delta_red_value)/steps);
      analogWrite(green_led, old_green_value+(i*delta_green_value)/steps);
      analogWrite(blue_led, old_blue_value+(i*delta_blue_value)/steps);

      delay(50);
    }
    
    old_red_value = new_red_value;
    old_green_value = new_green_value;
    old_blue_value = new_blue_value;
  }
}


