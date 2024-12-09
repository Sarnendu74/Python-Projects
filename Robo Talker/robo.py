import pyttsx3

while True:
    wel = 'Welcome to Robo Speaker.'
    engine = pyttsx3.init()
    # Speed set
    engine.setProperty('rate',140)
    x = input('Enter Commnad: ')
    engine.say(x)
    engine.runAndWait()
    if x == 'exit':
        print('Thank You.') 
        break
            
        
    
