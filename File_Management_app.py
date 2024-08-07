# importing os
import os

# Define a function to create a file
def create_file(filename):
    try:
        with open(filename,"x") as f:
            print(f'Your file {filename} created successfully !')
    except FileExistsError:
        print(f'Your file {filename} is already existed.')
    except Exception as E:
        print(f'An error occurred: {E}')

# Define a function to view all files
def view_file():
    files = os.listdir()
    if not files:
        print("Files not found !")
    else:
        print("`" * 6,"Files in directory")
        for file in files:
            print("^" * 3,file)

# Define a function to delete file
def delete_file(filename):
    try:
        content = os.remove(filename)
        print(f'Your file {content} successfully deleted.')
    except FileNotFoundError:
        print(f'Your file {filename} is not found !')
        
    except Exception as E:
        print("An error occurred !")
        
# Define a funtion to read a file
def read_file(filename):
    try:
        with open(filename,'r') as f:
            content = f.read()
            print(f"Your file data of {filename} is : \n{content}")
    except FileNotFoundError:
        print(f'Your file {filename} is not found !')
    except Exception:
        print("An error occurred !")
    
# Define a function to edit a file
def edit_file(filename):
    try:
        with open(filename,'a') as f:
            content = input("Enter data you wanna to add: ")
            f.write(content + "\n")
            print(f'Your content added to {filename} successfully.')
    except FileNotFoundError:
        print(f'Your file {filename} is not found !')
    except Exception as E:
        print("An error occurred !")
        
# Define a main function
def main():
      print("*" * 20,"Welcome to our File Management Applctaion","*" * 20)
      print("1.Create a File")
      print("2.Delete File")
      print("3.View all Files")
      print("4.Read File")
      print("5.Edit File")
      print("6.Exit")
      print("$"* 4,"Developed by Sarnendu Ghosh","$"* 4)
      while True:
      # Intialize choice
       choice = int(input("Enter your choice from (1-6): "))
       if choice == 1:
           filename = input("Enter your file name: ")
           create_file(filename)
       elif choice == 2:
           filename = input("Enter your file name: ")
           delete_file(filename)
       elif choice == 3:
           view_file()
       elif choice == 4:
          filename = input("Enter your file name to read: ")
          read_file(filename)
       elif choice == 5 :
           filename = input("Enter your filename you wanna edit: ")
           edit_file(filename)    
       elif choice == 6:
           print("Thank you for using our File Management Application ")
           break
       else:
           print("Invald Choice")

if __name__ == "__main__":
    main()
            
