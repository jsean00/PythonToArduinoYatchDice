#include <Wire.h>
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 20, 4);

int totalValue= 0;
void setup()
{
  // put your setup code here, to run once:
  Serial.begin(115200);
  lcd.init(); // initalize the lcd
  lcd.backlight();
}

String read_serial()
{
  String str = "";

  while (Serial.available())
  {
    str = Serial.readString();
    delay(10);
  }

  return str;
}

void loop()
{
  String str = read_serial();
  
  int string1 = str.indexOf(",");
  int string2 = str.indexOf(",",string1+1);
  int string3 = str.indexOf(",",string2+1);
  int string4 = str.indexOf(",",string3+1);
  int string5 = str.indexOf(",",string4+1);
  int string6 = str.indexOf(",",string5+1);
  int lengthS = str.length(); 
 
  String statusD = str.substring(0, string1);
  String dice1 = str.substring(string1+1, string2);
  String dice2 = str.substring(string2+1, string3);
  String dice3 = str.substring(string3+1, string4);
  String dice4 = str.substring(string4+1, string5);
  String dice5 = str.substring(string5+1, string6);
  String showValue = str.substring(string6+1, lengthS);
 
  lcd.setCursor(0, 0);
  lcd.print("Category :");
  lcd.setCursor(11, 0);
  lcd.print(statusD);
  
  lcd.setCursor(0, 1);
  lcd.print("Dice : ");
  lcd.setCursor(7, 1);
  lcd.print(dice1);
  lcd.setCursor(9, 1);
  lcd.print(dice2);
  lcd.setCursor(11, 1);
  lcd.print(dice3);
  lcd.setCursor(13, 1);
  lcd.print(dice4);
  lcd.setCursor(15, 1);
  lcd.print(dice5);
  
  lcd.setCursor(0, 2);
  lcd.print("CategoryValue :");
  lcd.setCursor(15, 2);
  lcd.print(showValue);

  lcd.setCursor(0, 3);
  lcd.print("Total :");
  totalValue = totalValue + showValue.toInt();
  lcd.setCursor(8,3);
  lcd.print(totalValue);
}
