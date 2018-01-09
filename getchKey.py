from msvcrt import getch

def main():
    while True:
        keycode = ord(getch())
        if keycode == 27: #ESC
            break
        elif keycode == 13: #Enter
            print("Enter")
        elif keycode == 224: #Special keys (arrows, f keys, ins, del, etc.)
            keycode = ord(getch())
            if keycode == 80:
                print("Down Arrow")
            elif keycode == 72:
                print("Up Arrow")
            elif keycode == 75:
                print("Left Arrow")
            elif keycode == 77:
                print("Right Arrow")
            elif keycode == 71:
                print("Home")
            elif keycode == 79:
                print("End")
            elif keycode == 73:
                print("Page Up")
            elif keycode == 81:
                print("Page Down")
            elif keycode == 82:
                print("Insert")
            elif keycode == 83:
                print("Delete")
        else:
            print("Key code {}".format(keycode))

if __name__=='__main__':
        main()