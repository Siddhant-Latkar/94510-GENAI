
import area_calculation

while (True):

        print("\n1.Area of circle")
        print("2.Area of squre")
        print("3.Area of rectangle")
        print("4.Area of triangle")
        print("5.EXIT")

        choice=int(input("\nEnter choice="))
        if(choice==1):
            r=float(input("Enter radious of circle="))
            area_calculation.circle(r)
        elif(choice==2):
            l=float(input("\n Enter leangth of squre="))
            area_calculation.squre(l)

        elif(choice==3):
            l=float(input("Enter leangth of rectangle="))
            w=float(input("Enter Width of rectangle="))
            area_calculation.rectangle(l,w)

        elif(choice==4):
            b=float(input("Enter base of Triangle="))
            h=float(input("Enter height of Triangle="))
            area_calculation.triangle(b,h)
        elif (choice ==5):
            print("Exiting... Goodbye!")
            break
        
        else:
            print("Invalid Choice! Please try again.")


