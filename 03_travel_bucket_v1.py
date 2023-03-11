import easygui

while True:
    bucket_list = easygui.enterbox("Enter five countries you want to visit with a comma inbetween them")

    places = bucket_list.split(",")
    if len(places) !=5:
        easygui.msgbox(f"Your bucket list must contain only five locations"
                       f"you entered {len(places)}")


else:
    break

easygui.msgbox(f"My bucket list: \n\n*")


