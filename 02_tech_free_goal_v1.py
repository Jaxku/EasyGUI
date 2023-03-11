import easygui

used_tech = easygui.enterbox("Enter the days on which you used tech. \n"
                             "Separate each day with a space",
                             "Days tech was used")
days = len(used_tech.split())
if days <= 3:
    easygui.msgbox(f"Congratulations. You used tech on only {days} days with "
                   f"{7-days} tech-free. \nGoal achieved!", "Goal achieved")

else:
    easygui.msgbox(f"Too bad. You used tech on {days} out of 7 days. \n"
                   f"That is {days-3} ,pre than your goal.",
                   "Goal failed")
