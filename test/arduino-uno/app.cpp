const int RGB[3] = {A1, A2, A3}; // 50 Ohm
const char *ID[3] = {"R:", "G:", "B:"};
int c = 0;

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
    int num = 0;
    num = map(analogRead(RGB[c]), 0, 1023, 0, 255);
    Serial.print(ID[c]);
    Serial.println(num);
    c++;
    if (c == 3) c = 0;
    delay(100);
}