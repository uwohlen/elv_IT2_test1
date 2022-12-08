#include <LiquidCrystal_I2C.h>

#define WIDTH 5*4
#define HEIGHT 8*2

LiquidCrystal_I2C lcd(0x27, 16, 2); // I2C address 0x27, 16 column and 2 rows

bool canvas[WIDTH*HEIGHT];

void setPixel(int x, int y, bool value) {
  canvas[y*WIDTH+x] = value;
}

void drawScreen() {
  byte currentChar = 0;
  lcd.clear();
  for (int x = 0; x < 4; x++) {
    for (int y = 0; y < 2; y++) {
      byte customChar[8];
      bool allZero = true;
      for (int sy = 0; sy < 8; sy++) {
        customChar[sy] = 0;
        for (int sx = 0; sx < 5; sx++) {
          customChar[sy] |= canvas[(y*8+sy)*WIDTH+(x*5+sx)] << (4-sx);
        }
        if (customChar[sy] != 0) allZero = false;
      }
      if (!allZero) {
        lcd.createChar(currentChar, customChar);
        lcd.setCursor(x, y);
        lcd.write(currentChar);
        currentChar++;
      }
    }
  }
}

int pieces[][4][4] = {
  {{4, 5, 6, 8}, {0, 1, 5, 9}, {2, 4, 5, 6}, {1, 5, 9, 10}},
};

int gameWidth = HEIGHT;
int gameHeight = WIDTH;
bool squares[WIDTH*HEIGHT];
int currentPiece;
int pieceRotation;
int piecex;
int piecey;

void newPiece(bool first = false) {
  if (!first) {
    for (int i = 0; i < 4; i++) {
      int square = pieces[currentPiece][pieceRotation][i];
      int x = piecex + square%4;
      int y = piecey + square/4;
      squares[y*gameWidth+x] = true;
    }
    //checkForClear();
  }

  currentPiece = 0;
  pieceRotation = 0;
  piecex = gameWidth/2-2;
  piecey = 0;
}

bool collide() {
  for (int i = 0; i < 4; i++) {
    int square = pieces[currentPiece][pieceRotation][i];
    int x = piecex + square%4;
    int y = piecey + square/4;

    if (x < 0 || x >= gameWidth) return true;
    if (y < 0 || y >= gameHeight) return true;
    if (squares[y*gameWidth+x]) return true;
  }
  return false;
}

void tick() {
  piecey++;
  if (collide()) {
    piecey--;
    newPiece();
  }
}

void rotatePiece(int delta) {
  pieceRotation = (pieceRotation+delta)%4;
  if (collide()) {
    pieceRotation = (pieceRotation-delta)%4;
  }
  if (pieceRotation < 0) pieceRotation += 4;
}

void movePiece(int delta) {
  piecex += delta;
  if (collide()) {
    piecex -= delta;
  }
}

void drop() {
  while (!collide()) {
    piecey++;
  }
  piecey--;
  newPiece();
}

void checkForClear() {
  for (int y = gameHeight-1; y >= 0; y++) {
    bool clear = true;
    for (int x = 0; x < gameWidth; x++) {
      if (squares[y*gameWidth+x] == false) clear = false;
    }
    if (clear) {
      for (int yi = y; yi > 0; yi--) {
        for (int xi = 0; xi < gameWidth; xi++) {
          squares[yi*gameWidth+xi] = squares[(yi-1)*gameWidth+xi];
        }
      }
    }
  }
}

void drawGame() {
  for (int x = 0; x < gameWidth; x++) {
    for (int y = 0; y < gameHeight; y++) {
      setPixel(y, x, squares[y*gameWidth+x]);
    }
  }

  for (int i = 0; i < 4; i++) {
    int square = pieces[currentPiece][pieceRotation][i];
    int x = piecex + square%4;
    int y = piecey + square/4;
    setPixel(y, x, true);
  }
}

#define LEFT_PIN 2
#define RIGHT_PIN 3
#define ROTATE_PIN 4
#define DROP_PIN 6

void setup()
{
  lcd.init();
  lcd.backlight();

  pinMode(LEFT_PIN, INPUT_PULLUP);
  pinMode(RIGHT_PIN, INPUT_PULLUP);
  pinMode(ROTATE_PIN, INPUT_PULLUP);
  pinMode(DROP_PIN, INPUT_PULLUP);

  Serial.begin(9600);

  newPiece(true);
}

void loop()
{
  if (digitalRead(LEFT_PIN) == LOW) {
    movePiece(1);
  }
  if (digitalRead(RIGHT_PIN) == LOW) {
    movePiece(-1);
  }
  if (digitalRead(ROTATE_PIN) == LOW) {
    rotatePiece(1);
  }
  if (digitalRead(DROP_PIN) == LOW) {
    drop();
  }

  tick();
  drawGame();
  drawScreen();
  delay(1000);
}
