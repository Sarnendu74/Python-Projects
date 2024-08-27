# Define a dictionary 
class_list = {}

# Define function for add stuent
def add_Student(class_list):
        name = input("Enter student name: ").capitalize().strip()
        try:
            score = int(input("Enter student marks(out of 500): "))
            class_list[name] = score
            print(f'Name : {name},Marks : {score} added.')
        except ValueError as v:
            print(v)
            print("Marks should be integer.")
            
# Define function for view list
def view(class_list):
    if not class_list:
        print("Your list is empty!")
    else:
        for key,value in class_list.items():
            print(f'Name : {key},Marks : {value}')
    
# Define function for update marks        
def upadate(class_list):
    if not class_list:
        print("Your list is empty!")
    else:
        name = input("Enter student name: ").capitalize().strip()
        score = int(input("Enter marks(out of 500): "))
        class_list[name] = score
        print(f"{name}'s marks updated.")
        
# Define function for delete student
def delete(class_list):
        if not class_list:
         print("Your list is empty!") 
        else:
            name = input("Enter student name: ").capitalize().strip() 
            del class_list[name]
            print(f" {name} Successfully removed.")
     
# Define funtion for checking grade
def overall_grades(class_list):
         if not class_list:
           print("Your list is empty!")
         else:
             for key,value in class_list.items():
                if value <= 150:
                     print(f"{key}'s,Marks :{value} and Grade : E") 
                elif value <= 250:
                     print(f"{key}'s,Marks :{value} and Grade : D") 
                elif value <= 350:
                     print(f"{key}'s,Marks :{value} and Grade : C") 
                elif value <= 450:
                     print(f"{key}'s,Marks :{value} and Grade : B") 
                else:
                     print(f"{key}'s,Marks :{value} and Grade : A")           
            
def main():    
    while True:
        print()
        print(" ..Student grade management system by Sarnendu.. ") 
        print("1.Display list")
        print("2.Add student")
        print("3.Update marks")
        print("4.Overall Grades")
        print("5.Delete student")
        print("6.Exit")
        choice = int(input("Enter your choice(1-5): "))
        if choice == 1:
            view(class_list)
        elif choice == 2:
            add_Student(class_list)
        elif choice == 3:
            upadate(class_list)
        elif choice == 4:
            overall_grades(class_list)
        elif choice == 5:
            delete(class_list)
        elif choice == 6:
            print("Thank You for using our system.")
            break
        else:
            print("Invalid Choice")
            
            
if __name__ == "__main__":
    main()
            