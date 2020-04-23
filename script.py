import pyautogui, time, argparse, random

messages = ['Press F to pay respects', 'GGWP!', 'Denied!', 'Hi!', 'Noob!', 'Pro!', '2Ez4You','Camper']

def get_args():
    parser = argparse.ArgumentParser("Auto mouse mover and Chat spammer")

    time_desc = "Time after which the mouse to move and click simulataneously"
    start_desc = "The Starting position keep a space in between the coordinates X and Y"
    end_desc = "The Ending position keep a space in between the coordinates X and Y"
    message_desc = "The position of the Chat box from the UI window"

    #TODO add defaults
    parser.add_argument("-time", help=time_desc, default=0)
    parser.add_argument("-start_location", help=start_desc) 
    parser.add_argument("-end_location", help=end_desc)
    parser.add_argument("-chat_box_location", help = message_desc)

    args = parser.parse_args()

    return args

def main():
    args = get_args()
    chatFlag = False
    start = list(map(int, (args.start_location).split()))
    end = list(map(int, (args.end_location).split()))
    timeToClick = int(args.time)
    
    if(len(args.chat_box_location) > 0):
        chatFlag = True
        chat_box = list(map(int, (args.chat_box_location).split()))

    startTime = time.time()

    print('Press Ctrl-C to quit.')
    try:
        while True:
            pyautogui.moveTo(start[0],start[1])
            pyautogui.click()
            time.sleep(timeToClick)
            pyautogui.moveTo(end[0],end[1])
            pyautogui.click()
            
            if (int(time.time() - startTime) % 2 == 0) and chatFlag:
                pyautogui.moveTo(chat_box[0], chat_box[1])
                pyautogui.click()
                pyautogui.typewrite(messages[random.randint(0,7)])
                pyautogui.press('return')

    except KeyboardInterrupt:
        print('\n')

if __name__ == "__main__":
    main()