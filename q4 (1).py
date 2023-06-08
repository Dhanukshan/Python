current_year=2023
birth_year=int(input("enter your year of birth="))
age=current_year - birth_year
if(age>60):
    original_face=1020
    discount_face=original_face-(original_face*0.2)
    print("the amount to be paid:",discount_face)
else:
    print("sorry you are not eligible for this consession")
    print("the original face:rs",1020)
