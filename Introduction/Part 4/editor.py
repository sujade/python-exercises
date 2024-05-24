while True:
    editor = input("Editor: ").strip().lower()
    if editor == "pycharm":
        print("an excellent choice!")
        break
    elif editor in ["word", "notepad"]:
        print("awful")
    else:
        print("not good")
