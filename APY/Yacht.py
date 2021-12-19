import cv2
import cvzone
import random
from cvzone.HandTrackingModule import HandDetector


cap = cv2.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)
detector = HandDetector(detectionCon=0.8, maxHands=1)

imgFront = cv2.imread("background.PNG", cv2.IMREAD_UNCHANGED)
imgFront = cv2.resize(imgFront, (0, 0), None, 1080/976, 1080/976)

img = cap.read()


class Button:
    def __init__(self, pos, width, height, value):
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value

    def draw(self, img):
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                      (225, 225, 225), cv2.FILLED)
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                      (50, 50, 50), 3)
        cv2.putText(img, self.value, (int(self.pos[0] + self.width/10), int(self.pos[1] + self.height *15 /24)), cv2.FONT_HERSHEY_PLAIN,
                    2, (50, 50, 50), 2)

    def checkClick(self, x, y):
        if self.pos[0]<x<self.pos[0]+self.width and \
                self.pos[1]<y<self.pos[1]+self.height:
            cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                          (225, 0, 0), cv2.FILLED)
            cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                          (50, 0, 0), 3)
            cv2.putText(img, self.value, (int(self.pos[0] + self.width/10), int(self.pos[1] + self.height /2)), cv2.FONT_HERSHEY_PLAIN,
                        2, (0, 0, 0), 3)
            return True
        else:
            return False


class textBox:
    def __init__(self, pos, value):
        self.pos = pos
        self.value = value

    def draw(self, img):
        cv2.putText(img, self.value, (self.pos[0], self.pos[1]), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (50, 50, 50), 2)


class Dice:
    def __init__(self, pos, size, value):
        self.pos = pos
        self.size = size
        self.value = value

    def draw(self, img):
        cv2.rectangle(img, self.pos, (self.pos[0] + self.size[0], self.pos[1] + self.size[1]),
                      (225, 225, 225), cv2.FILLED)
        cv2.rectangle(img, self.pos, (self.pos[0] + self.size[0], self.pos[1] + self.size[1]),
                      (25, 25, 25), 3)

        if int(self.value) == 1:
                cv2.circle(img, (int(self.pos[0] + self.size[0] / 2), int(self.pos[1] + self.size[1] / 2)),
                           int(self.size[0] / 10), (100, 0, 0), -1)
        if int(self.value) == 2:
                cv2.circle(img, (int(self.pos[0] + self.size[0] / 5), int(self.pos[1] + self.size[1] / 5)),
                            int(self.size[0] / 10), (100, 0, 0), -1)
                cv2.circle(img, (int(self.pos[0] + self.size[0] * 4 / 5), int(self.pos[1] + self.size[1] * 4 / 5)),
                            int(self.size[0] / 10), (100, 0, 0), -1)
        if int(self.value) == 3:
                cv2.circle(img, (int(self.pos[0] + self.size[0] / 5), int(self.pos[1] + self.size[1] / 5)),
                           int(self.size[0] / 10), (100, 0, 0), -1)
                cv2.circle(img, (int(self.pos[0] + self.size[0] * 4 / 5), int(self.pos[1] + self.size[1] * 4 / 5)),
                           int(self.size[0] / 10), (100, 0, 0), -1)
                cv2.circle(img, (int(self.pos[0] + self.size[0] / 2), int(self.pos[1] + self.size[1] / 2)),
                           int(self.size[0] / 10), (100, 0, 0), -1)
        if int(self.value) == 4:
                cv2.circle(img, (int(self.pos[0] + self.size[0] / 5), int(self.pos[1] + self.size[1] / 5)),
                           int(self.size[0] / 10), (100, 0, 0), -1)
                cv2.circle(img, (int(self.pos[0] + self.size[0] / 5), int(self.pos[1] + self.size[1] * 4 / 5)),
                           int(self.size[0] / 10), (100, 0, 0), -1)
                cv2.circle(img, (int(self.pos[0] + self.size[0] * 4 / 5), int(self.pos[1] + self.size[1] / 5)),
                           int(self.size[0] / 10), (100, 0, 0), -1)
                cv2.circle(img, (int(self.pos[0] + self.size[0] * 4 / 5), int(self.pos[1] + self.size[1] * 4 / 5)),
                           int(self.size[0] / 10), (100, 0, 0), -1)
        if int(self.value) == 5:
                cv2.circle(img, (int(self.pos[0] + self.size[0] / 5), int(self.pos[1] + self.size[1] / 5)),
                           int(self.size[0] / 10), (100, 0, 0), -1)
                cv2.circle(img, (int(self.pos[0] + self.size[0] / 5), int(self.pos[1] + self.size[1] * 4 / 5)),
                           int(self.size[0] / 10), (100, 0, 0), -1)
                cv2.circle(img, (int(self.pos[0] + self.size[0] * 4 / 5), int(self.pos[1] + self.size[1] / 5)),
                           int(self.size[0] / 10), (100, 0, 0), -1)
                cv2.circle(img, (int(self.pos[0] + self.size[0] * 4 / 5), int(self.pos[1] + self.size[1] * 4 / 5)),
                           int(self.size[0] / 10), (100, 0, 0), -1)
                cv2.circle(img, (int(self.pos[0] + self.size[0] / 2), int(self.pos[1] + self.size[1] / 2)),
                           int(self.size[0] / 10), (100, 0, 0), -1)
        if int(self.value) == 6:
                cv2.circle(img, (int(self.pos[0] + self.size[0] / 5), int(self.pos[1] + self.size[1] / 5)),
                           int(self.size[0] / 10), (100, 0, 0), -1)
                cv2.circle(img, (int(self.pos[0] + self.size[0] / 5), int(self.pos[1] + self.size[1] * 4 / 5)),
                           int(self.size[0] / 10), (100, 0, 0), -1)
                cv2.circle(img, (int(self.pos[0] + self.size[0] * 4 / 5), int(self.pos[1] + self.size[1] / 5)),
                           int(self.size[0] / 10), (100, 0, 0), -1)
                cv2.circle(img, (int(self.pos[0] + self.size[0] * 4 / 5), int(self.pos[1] + self.size[1] * 4 / 5)),
                           int(self.size[0] / 10), (100, 0, 0), -1)
                cv2.circle(img, (int(self.pos[0] + self.size[0] / 5), int(self.pos[1] + self.size[1] * 2.5 / 5)),
                           int(self.size[0] / 10), (100, 0, 0), -1)
                cv2.circle(img, (int(self.pos[0] + self.size[0] * 4 / 5), int(self.pos[1] + self.size[1] * 2.5 / 5)),
                           int(self.size[0] / 10), (100, 0, 0), -1)
        else:
            return


class outBox:
    def __init__(self, pos, size, thick):
        self.pos = pos
        self.size = size
        self.thick = thick

    def draw(self, img):
        cv2.rectangle(img, self.pos, (self.pos[0] + self.size[0], self.pos[1] + self.size[1]),
                      (25, 25, 255), self.thick)




# Variables
delayCounter = 0
diceList = []
diceXList = []
outBoxList = []
valueList = []
valueCount = [0,0,0,0,0,0]
valueTemp = [0,0,0,0,
             0,0,0,0,
             0,0,0,0]
diceStatus = [0, 0, 0, 0, 0]
textBoxList = []
cateOutList = []
showVal = 0
handCount = 0
tipIds = [4, 8, 12, 16, 20]

def dependTrue():
    for i in range(6):
        valueCount[i]= valueList.count(i+1)
    valueTemp[0] = 1 * valueCount[0]
    valueTemp[1] = 2 * valueCount[1]
    valueTemp[2] = 3 * valueCount[2]
    valueTemp[3] = 4 * valueCount[3]
    valueTemp[4] = 5 * valueCount[4]
    valueTemp[5] = 6 * valueCount[5]
    for k in range(5):
        valueTemp[6] += valueList[k]
    for k in range(6):
        if valueCount[k]>3:
            for k1 in range(5):
                valueTemp[7]+=valueList[k1]
    for l in range(6):
        for m in range(6):
            if (valueCount[l]==3 and valueCount[m]==2):
                for n in range(5):
                    valueTemp[8] += valueList[n]
    for o in range(3):
        if valueCount[0 + o] >= 1 and valueCount[1 + o]>=1 and valueCount[2 + o]>=1 and valueCount[3 + o]>=1:
            valueTemp[9] = 15
    for p in range(2):
        if valueCount[0 + p] == 1 and valueCount[1 + p]== 1 and valueCount[2 + p]== 1 and valueCount[3 + p]== 1 and valueCount[4 + p]== 1:
            valueTemp[10] = 30
    for q in range(6):
        if valueCount[q] == 5:
            valueTemp[11] = 50


for x in range(5):
    valueList.append(random.randrange(1, 7))

for x1 in range(5):
    xpos = x1 * 170 + 650
    outBoxList.append(outBox((xpos,100),(150,150),10))
    diceXList.append(xpos)
    diceList.append(Dice((xpos,100),(150,150), valueList[x1]))

buttonReroll = Button((1500,100),200,60,'Reroll')
buttonCalcul = Button((1500,170),200,60,'Calculate')
buttonUP = Button((1500,240),150,60,'UP')
buttonDOWN = Button((1500,310),150,60,'DOWN')

for y in range(12):
    xpos = 325
    if(y<6):
        ypos = y * 50+250
    elif y==6:
        ypos = 670
    elif y>6:
        ypos = (y-7) * 50+730
    textBoxList.append(textBox((xpos,ypos),str(valueTemp[y])))
    cateOutList.append(outBox((xpos-50,ypos-30),(110,45),5))
#640 700
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)
    buttonCalcul.draw(img)
    buttonReroll.draw(img)
    buttonUP.draw(img)
    buttonDOWN.draw(img)


    if hands:
        lmList = hands[0]['lmList']
        length, _, img = detector.findDistance(lmList[8], lmList[12], img)
        #print(length)
        x, y = lmList[8]
        if length<50 and delayCounter == 0:
            for i in range(5):
                if diceXList[i]< x <diceXList[i]+150 and 100<y<250:
                    if diceStatus[i] == 0:
                        diceStatus[i] = 1
                    else:
                        diceStatus[i] = 0
                    delayCounter = 1

            if buttonReroll.checkClick(x,y):
                for x1 in range(5):
                    if diceStatus[x1] == 0:
                        valueList[x1]= random.randrange(1,7)
                        xpos = x1 * 170 + 650
                        diceList[x1]= Dice((xpos, 100), (150, 150), valueList[x1])
                        dependTrue()
                        for y in range(12):
                            xpos = 325
                            if (y < 6):
                                ypos = y * 50 + 250
                            elif y == 6:
                                ypos = 670
                            elif y > 6:
                                ypos = (y - 7) * 50 + 730
                            textBoxList[y] = textBox((xpos, ypos), str(valueTemp[y]))
                        valueCount = [0,0,0,0,0,0]
                        valueTemp = [0,0,0,0,0,0,0,0,0,0,0,0]
                delayCounter = 1
            if buttonCalcul.checkClick(x,y):
                dependTrue()
                for y in range(12):
                    xpos = 325
                    if (y < 6):
                        ypos = y * 50 + 250
                    elif y == 6:
                        ypos = 670
                    elif y > 6:
                        ypos = (y - 7) * 50 + 730
                    textBoxList[y] = textBox((xpos, ypos), str(valueTemp[y]))
                valueCount = [0,0,0,0,0,0]
                valueTemp = [0,0,0,0,0,0,0,0,0,0,0,0]
                delayCounter = 1
            if buttonUP.checkClick(x, y):
                showVal-= 1
                delayCounter = 1
            if buttonDOWN.checkClick(x, y):
                showVal+= 1
                delayCounter = 1

    for i in range(5):
        if diceStatus[i] == 1:
            outBoxList[i].draw(img)
    for dices in diceList:
        dices.draw(img)

    if delayCounter != 0:
        delayCounter += 1
        if delayCounter > 30:
            delayCounter = 0

    # Display
    imgResult = cvzone.overlayPNG(img, imgFront, [0, 0])

    for texts in textBoxList:
        texts.draw(imgResult)

    cateOutList[showVal].draw(imgResult)

    cv2.imshow("Image", imgResult)
    key = cv2.waitKey(1)
    if key == ord('c'):
        myEquation = ''
    if key == ord('q') or key == 27:  # 'q' 이거나 'esc' 이면 종료
        break

cv2.destroyAllWindows()






