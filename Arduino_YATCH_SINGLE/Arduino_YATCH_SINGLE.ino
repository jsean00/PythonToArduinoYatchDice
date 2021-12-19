#include <Wire.h>                     
#include <LiquidCrystal_I2C.h>        
LiquidCrystal_I2C lcd(0x27, 20, 4);   
#include <Keypad.h>
const byte numRows = 4;
const byte numCols = 4;

char keymap[numRows][numCols] =
{
  {'1', '2', '3', '*'},
  {'4', '5', '*', '*'},
  {'R', '*', '*', '*'},
  {'U', 'D', 'S', '*'}
};

int diceValues[] = {0, 0, 0, 0, 0};
int diceStatus[] = {0, 0, 0, 0, 0};

char*category[] = {"Aces      ", "Deuces    ", "Threes    ", "Fours      ", "Fives     ", "Sixes     ", "Choice    ", "4ofaKind  ", "FullHouse ", "S.Straight", "L.Straight", "Yacht     "};
int cateAns[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int cateSta[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int cateSel = 0;
int cateSelDiv;
int valcount[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int valtemp[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int TOTAL;
int BONUS;
bool depend = false;
int rolls = 3;
// 1 : 1번다이스
// 2 : 2번다이스
// 3 : 3번다이스
// 4 : 4번다이스
// 5 : 5번다이스

byte rowPins[numRows] = {7, 6, 5, 4};
byte colPins[numCols] = {8, 9, 10, 11};

Keypad myKeypad = Keypad(makeKeymap(keymap), rowPins, colPins, numRows, numCols);

void setup()
{
  randomSeed(analogRead(A0));
  Serial.begin(9600);
  lcd.init();                      // LCD 초기화
  lcd.backlight();                // 백라이트 켜기

  lcd.setCursor(0, 0);
  lcd.print("Dice:0 0 0 0 0 ROLL3");

  lcd.setCursor(0, 1);
  lcd.print("Category:Aces");

  lcd.setCursor(0, 2);
  lcd.print("SUM:0");
  lcd.setCursor(7, 2);
  lcd.print("BONUS:  /63");

  lcd.setCursor(0, 3);
  lcd.print("Total:   ");
  lcd.setCursor(10, 3);
  lcd.print("Turn:P1");

}

void loop()
{
  //------------------------------------------------------ KEYPAD
  char keypressed = myKeypad.getKey();
  if (keypressed == 'R' && rolls != 0)
  {
    rollDice();
    depend = false;
  }
  if ((keypressed == 'S') && (cateSta[cateSelDiv] == 0) && (rolls != 3))
  {
    cateAns[cateSelDiv] = valtemp[cateSelDiv];
    TOTAL += valtemp[cateSelDiv];
    if (cateSelDiv < 6) {
      BONUS += valtemp[cateSelDiv];
      if (BONUS > 62) {
        TOTAL += 35;
      }
    }
    cateSta[cateSelDiv] = 1;

    depend = false;
    for (int l = 0; l < 12; l++) {
      valcount[l] = 0;
      valtemp[l] = 0;
    }
    for (int i = 0; i < 5; i++) {
      diceValues[i] = 0;
      diceStatus[i] = 0;
    }
    rolls = 3;

  }
  if (keypressed == '1') {
    press1();
  }
  if (keypressed == '2') {
    press2();
  }
  if (keypressed == '3') {
    press3();
  }
  if (keypressed == '4') {
    press4();
  }
  if (keypressed == '5') {
    press5();
  }

  if (keypressed == 'U')
  {
    cateSel += 1;
  }
  if (keypressed == 'D')
  {
    cateSel += 11;
  }
  //-----------------------------------------------------------Update
  for (int i = 0; i < 5; i++)
  {
    lcd.setCursor(5 + i * 2, 0);
    lcd.print(diceValues[i]);
    lcd.setCursor(6 + i * 2, 0);
    if ( diceStatus[i] == 1) {
      lcd.print("s");
    }
    else {
      lcd.print(" ");
    }
  }
  lcd.setCursor(19, 0);
  lcd.print(rolls);
  lcd.setCursor(9, 1);
  cateSelDiv = cateSel % 12;
  lcd.print(category[cateSelDiv]);
  if (depend == false) {
    dependTrue();
  }
  if (cateSta[cateSelDiv] == 1) {
    lcd.setCursor(19, 1);
    lcd.print('X');
  }
  else{
    lcd.setCursor(19, 1);
    lcd.print(' ');
  }
  lcd.setCursor(4, 2);
  if (valtemp[cateSelDiv] / 10 < 1) {
    lcd.print(' ');
    lcd.setCursor(5, 2);
  }
  lcd.print(valtemp[cateSelDiv]);
  lcd.setCursor(13, 2);
  lcd.print(BONUS);
  lcd.setCursor(6, 3);
  lcd.print(TOTAL);

}

//--------------------------------------------------------------------------------------------------------------------------------------------------------
void rollDice() {
  for (int i = 0; i < 5; i++)
  {
    if ( diceStatus[i] == 0) {
      diceValues[i] = random(1, 7);
    }
  }
  rolls -= 1;
}
void press1() {
  if (diceStatus[0] == 1) {
    diceStatus[0] = 0;
  }
  else {
    diceStatus[0] = 1;
  }
}

void press2() {
  if (diceStatus[1] == 1) {
    diceStatus[1] = 0;
  }
  else {
    diceStatus[1] = 1;
  }
}

void press3() {
  if (diceStatus[2] == 1) {
    diceStatus[2] = 0;
  }
  else {
    diceStatus[2] = 1;
  }
}

void press4() {
  if (diceStatus[3] == 1) {
    diceStatus[3] = 0;
  }
  else {
    diceStatus[3] = 1;
  }
}

void press5() {
  if (diceStatus[4] == 1) {
    diceStatus[4] = 0;
  }
  else {
    diceStatus[4] = 1;
  }
}

void dependTrue() {
  for (int l = 0; l < 12; l++) {
    valcount[l] = 0;
    valtemp[l] = 0;
  }

  for (int i = 0; i < 5; i++) {
    if (diceValues[i] == 1) {
      valcount[0] += 1;
    }
    if (diceValues[i] == 2) {
      valcount[1] += 1;
    }
    if (diceValues[i] == 3) {
      valcount[2] += 1;
    }
    if (diceValues[i] == 4) {
      valcount[3] += 1;
    }
    if (diceValues[i] == 5) {
      valcount[4] += 1;
    }
    if (diceValues[i] == 6) {
      valcount[5] += 1;
    }
  }

  valtemp[0] = valcount[0];
  valtemp[1] = valcount[1] * 2;
  valtemp[2] = valcount[2] * 3;
  valtemp[3] = valcount[3] * 4;
  valtemp[4] = valcount[4] * 5;
  valtemp[5] = valcount[5] * 6;
  for (int i = 0; i < 5; i++) {
    valtemp[6] += diceValues[i];
  }
  for (int i = 0; i < 6; i++) {
    if (valcount[i] > 3) {
      for (int i = 0; i < 5; i++) {
        valtemp[7] += diceValues[i];
      }
    }
  }
  if ((valcount[0] == 3 || valcount[1] == 3 || valcount[2] == 3 || valcount[3] == 3 || valcount[4] == 3 || valcount[5] == 3) && (valcount[0] == 3 || valcount[1] == 3 || valcount[2] == 3 || valcount[3] == 3 || valcount[4] == 3 || valcount[5] == 3))
  {
    for (int i = 0; i < 5; i++) {
      valtemp[8] += diceValues[i];
    }
  }

  for (int j = 0; j < 3; j++) {
    if ((valcount[0 + j] >= 1) && (valcount[1 + j] >= 1) && (valcount[2 + j] >= 1) && (valcount[3 + j] >= 1))
    {
      valtemp[9] = 15;
    }
  }

  for (int k = 0; k < 2; k++) {
    if ((valcount[0 + k] >= 1) && (valcount[1 + k] >= 1) && (valcount[2 + k] >= 1) && (valcount[3 + k] >= 1) && (valcount[4 + k] >= 1))
    {
      valtemp[10] = 30;
    }
  }

  for (int i = 0; i < 5; i++) {
    if (valcount[i] == 5) {
      valtemp[11] = 50;
    }
  }

  depend = true;
}
