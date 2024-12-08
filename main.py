TWD=int(input("enter total working days of your school/collage ="))
AD=int(input("enter the days which you have spent in your house😤="))
AP=((TWD-AD)/TWD)*100
print(f"attandance percentage {AP:.3222}%")
if AP<75:
    print("sorry bro you are not able to give exams this year try next year with more the 75 percentage attendance😑")
else:
    print("bro now you are in truble because you have to give exams this year (your attendance is more then 75%) so prepare well for your exams")