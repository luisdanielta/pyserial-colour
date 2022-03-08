const int RGB[3] = {A1, A2, A3}; // 50 Ohm
const char *ID[3] = {"R:", "G:", "B:"};

void setup()
{
    Serial.begin(9600);
    // initialize the digital pin as an output.
    for (int i = 0; i < 3; i++)
    {
        pinMode(RGB[i], INPUT);
    }
}

void loop()
{
    int number = 0;
    for (int i = 0; i < 3; i++)
    {
        number = map(analogRead(RGB[i]), 0, 1023, 0, 255);
        Serial.print(ID[i]);
        Serial.println(number);
    }
    delay(100);
}