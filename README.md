# DIP-project-
Controlling the game ( like subway surfer , temple run etc,) using hand contours 

##Install the libraries 
For accessing the this file remember that you have insatlled the libraries from the command prompt :

1. install numpy
2. install open-cv
3. install pyautogui 

##Working
  Firstly we are defining the color of the hand which it have to read from and we have defined the range from lower_Skin to the upper_skin
  
  after that we have simply find the contours relative to that and then find out the area where maximum contours are lying 
  
  the  centre of the maximum area have been find out and according to that a circle is drawn of 10 pixels.
  
  Now i have dividen my video screen into 9 different regions which have been shown in the fig below


![DIP project](https://user-images.githubusercontent.com/93609977/171785445-523f4dfe-8525-42e4-ba67-b8dacb60c58a.png)


We have defined our camera size to be of (300*300)pixels and according to that divided the coordinate 

The whole work which will be implemented in the game will be done by the pyautogui 

You can specify the different task like 

###For (x,y) when x<75  && y<250 && y>200 --> LEFT

###For (x,y) when x>225  && y<250 && y>200 --> RIGHT

###For (x,y) when x>75  && x<255 && y>250 --> DOWN

###For (x,y) when x>75  && x<225 && y<200 --> UP

###For (x,y) when x>75  && x<225 && y<250 && y>200 --> Neutral(no response)
 
 You can specify the different task for the white space on your own 
 
 For that  specify the region and when your(x,y) coordinates comes in that range then it will perform specify task 
 for eg in fighting games you can specify it as a when it will come in the white space it will perform the firring 
 
 
This is all the working 

Now if you want bettre results you can wear a white clothes in your hand and thenplay the game it will give the smoother functioning

### You can apply this whole thing in the games like subway surfer , temple run and any of them of your choice 

### Thanks for reading it 


Have a nice day!!!!!! 
