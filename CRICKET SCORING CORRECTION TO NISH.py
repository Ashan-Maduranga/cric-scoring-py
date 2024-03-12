import tkinter as tk
from tkinter import *
from game_logic import GameLogic
ValidBalls = 0


class Cricket:
    gl = GameLogic() 
    current_runs = 0

    def __init__(self,root):
        self.match_details = self.gl.get_match_details()
        
        self.root=root
        self.root.geometry('1270x800+0+0')
        self.root.config(bg="green")
        
#============### Frame-1 SCORE LT ###================================
        frame1=Frame(self.root)
        frame1.place(x=50,y=50,width=350,height=50)

#=========================================================================    

        #==========***TEAM NAME*** =============
        self.team_name=StringVar()
        self.team_name.set("TEAM ")
        self.teamnamelbl=Label(frame1,text="",textvariable=self.team_name,font=("",28,"bold")) 
        self.teamnamelbl.pack(side=LEFT)


        #===========***TOTAL*** =================
        self.Total=StringVar()
        self.Total.set("0")
        self.Scorelbl=Label(frame1,text="",textvariable=self.Total,font=("",30,"bold")) 
        self.Scorelbl.pack(side=LEFT,padx=(10,0))
       

        #===========***WICKETS***=================
        self.Wickets=StringVar()
        self.Wickets.set("/0")
        self.Wicketslbl=Label(frame1,text="",textvariable=self.Wickets,font=("",30,"bold")) 
        self.Wicketslbl.pack(side=LEFT)

        #===========***OVERS & BALLS***=================
              #===== Play_Overs ========
        self.Play_Overs=StringVar()
        self.Play_Overs.set("0")
        self.Play_Overs_lbl=Label(frame1,text="",textvariable=self.Play_Overs,font=("",25,"bold")) 
        self.Play_Overs_lbl.pack(side=LEFT,padx=(15,0))

             #===== Play_Balls ========
        self.Play_Balls=StringVar()
        self.Play_Balls.set(".0")
        self.Play_Balls_lbl=Label(frame1,text="",textvariable=self.Play_Balls,font=("",25,"bold")) 
        self.Play_Balls_lbl.pack(side=LEFT)


#============### Frame-2 SCORE CONTROL PALLETE #### =====================
        frame2=Frame(self.root)
        frame2.place(x=30,y=120,width=410,height=500)
        frame2.config(bg="black")  
    #========================================================================
         ####***UPDATE TEAM NAME***#### 
         #LABEL
        Team_Short_name_lbl=Label(frame2,text="BAT TEAM (SHORT NAME) ",font=("",12,'bold')).place(x=18,y=20)
         #ENTRY
        self.TeamShortnameentry=Entry(frame2,font=("",15,'bold'))
        self.TeamShortnameentry.place(x=237,y=20,width=75,height=25)
         #BUTTON
        TeamShortname=Button(frame2,text="UPDATE",font=("",12,'bold'),command=self.Team_score_bug_name)
        TeamShortname.place(x=320,y=15) 
        TeamShortname.config(bg="RED")
         #################################################
         ####***UPDATE BALLS TO OVER***####
         #LABEL
        BallspToOverlbl=Label(frame2,text="BALLS TO OVER ",font=("",12,'bold')).place(x=18,y=55)
         #ENTRY
        self.BallsToOventry=Entry(frame2,font=("",18,'bold'))
        self.BallsToOventry.place(x=237,y=55,width=75,height=25)
         #BUTTON
        BallsToOventry=Button(frame2,text="UPDATE",font=("",12,'bold'),command=self.Balls_To_Over)
        BallsToOventry.place(x=320,y=52)
        BallsToOventry.config(bg="RED")
         #UPDATE BALLS TO OVER DISPLAY CONFIRMATION
        self.BallsToOver=StringVar()
        self.BallsToOver.set("0")
        self.BallsToOverlbl=Label(frame2,text="",textvariable=self.BallsToOver,font=("",15,"bold")) 
        self.BallsToOverlbl.pack(side=LEFT)
        self.BallsToOverlbl.place(x=160,y=55,width=75,height=25)
        self.BallsToOverlbl.config(bg="Yellow")
    #############################################################
         ####***UPDATE VALID SCORE***####


         #BUTTON BALL
        self.Legal=StringVar()
        self.Legal.set("")

        Validball=Button(frame2,text=" BALL ",font=("",20,'bold'),command=self.Main_Score_Valid_Ball_Overs_Update)
        Validball.place(x=320,y=88,width=82,height=155)
        Validball.config(bg="BLUE")
        Validball.config(fg="Yellow")
        
         #LABEL
        ValidRunslbl=Label(frame2,text="BATTERS RUNS UPDATE",foreground="black", background="green",font=("",15,'bold')).place(x=18,y=90,width=295,height=25)

       
        
         #BUTTON 0
        Run0btn=Button(frame2,text="+0",font=("",15,'bold'),command=lambda:self.update_runs(0))
        Run0btn.place(x=20,y=120)
        Run0btn.config(bg="green")
         #BUTTON 1
        Run1btn=Button(frame2,text="+1",font=("",15,'bold'),command=lambda:self.update_runs(1))
        Run1btn.place(x=70,y=120)
        Run1btn.config(bg="green")
         #BUTTON 2
        Run2btn=Button(frame2,text="+2",font=("",15,'bold'),command=lambda:self.update_runs(2))
        Run2btn.place(x=120,y=120)
        Run2btn.config(bg="green")
         #BUTTON 3
        Run3btn=Button(frame2,text="+3",font=("",15,'bold'),command=lambda:self.update_runs(3))
        Run3btn.place(x=170,y=120)
        Run3btn.config(bg="green")
         #BUTTON 4
        Run4btn=Button(frame2,text="+4",font=("",15,'bold'),command=lambda:self.update_runs(4))
        Run4btn.place(x=220,y=120)
        Run4btn.config(bg="green")
         #BUTTON 6
        Run5btn=Button(frame2,text="+6",font=("",15,'bold'),command=lambda:self.update_runs(6))
        Run5btn.place(x=270,y=120)
        Run5btn.config(bg="green")

     #############################################################################
        #####****UPDATE BUYS & LEGBUYS
         #LABEL
        ValidRunslbl=Label(frame2,text="LEG BUYS & BUYS UPDATE",foreground="RED", background="LightBlue",font=("",15,'bold')).place(x=18,y=170,width=295,height=25)

         #LB & B 1
        Run0btn=Button(frame2,text="+1",foreground="RED", background="LightBlue",font=("",15,'bold'),command=self.buys_Lb_1)
        Run0btn.place(x=20,y=200)
        Run0btn.config(bg="lightblue")
         #LB & B 2
        Run1btn=Button(frame2,text="+2",foreground="RED", background="LightBlue",font=("",15,'bold'),command=self.buys_Lb_2)
        Run1btn.place(x=70,y=200)
        Run1btn.config(bg="lightblue")
         #LB & B 3
        Run2btn=Button(frame2,text="+3",foreground="RED", background="LightBlue",font=("",15,'bold'),command=self.buys_Lb_3)
        Run2btn.place(x=120,y=200)
        Run2btn.config(bg="lightblue")
         #LB & B
        Run3btn=Button(frame2,text="+4",foreground="RED", background="LightBlue",font=("",15,'bold'),command=self.buys_Lb_4)
        Run3btn.place(x=170,y=200)
        Run3btn.config(bg="lightblue")
         #LB & B
        Run4btn=Button(frame2,text="+5",foreground="RED", background="LightBlue",font=("",15,'bold'),command=self.buys_Lb_5)
        Run4btn.place(x=220,y=200)
        Run4btn.config(bg="lightblue")
         #LB & B
        Run5btn=Button(frame2,text="+6",foreground="RED", background="LightBlue",font=("",15,'bold'),command=self.buys_Lb_6)
        Run5btn.place(x=270,y=200)
        Run5btn.config(bg="lightblue")
        


    #############################################################################

         ####***EXTRA RUNS UPDATE***####
         #LABEL
        ExtraRunslbl=Label(frame2,text="EXTRA RUNS ",foreground="white", background="brown",
                           font=("",15,'bold')).place(x=18,y=250,width=180,height=32)
         #ENTRY
        self.ExtraRunsentry=Entry(frame2,font=("",18,'bold'))
        self.ExtraRunsentry.place(x=207,y=250,width=55,height=32)

         #BUTTON
        ExtraRunsentry=Button(frame2,text="ADD TO TOTAL",font=("",12,'bold'),command=self.Extra_add)
        ExtraRunsentry.place(x=270,y=250)
        ExtraRunsentry.config(bg="yellow")

    #############################################################################
        
        ####***CORRECTIONS***####

        #LABEL
        Correctionslbl=Label(frame2,text="CORRECTIONS ",foreground="white", background="RED",
                           font=("",15,'bold')).place(x=18,y=300,width=380,height=35)
    #############################################################################
         ####***UPDATE MANUAL SCORE***####
        
         # ENTRY FOR MANUAL SCORE
        ManualRunslbl=Label(frame2,text=" UPDATE RUNS  ",font=("",12,'bold')).place(x=18,y=345)
        self.ManualRunsentry=Entry(frame2,font=("",18,'bold'))
        self.ManualRunsentry.place(x=168,y=345,width=50,height=25)

         #BUTTON ADD
        ManualRunsAddbtn=Button(frame2,text="ADD ",font=("",13,'bold'),command=self.Runs_add)
        ManualRunsAddbtn.place(x=225,y=345,width=80,height=27)
        ManualRunsAddbtn.config(bg="green")
         #BUTTON REMOVE
        ManualRunsRemovebtn=Button(frame2,text="REMOVE ",font=("",13,'bold'),command=self.Runs_removed)
        ManualRunsRemovebtn.place(x=315,y=345,width=80,height=27)
        ManualRunsRemovebtn.config(bg="RED")

     #############################################################################
         ####***OVERS ADD Or REMOVE***####       

        # ENTRY FOR MANUAL OVERS
        ManualRunslbl=Label(frame2,text=" UPDATE OVERS ",font=("",12,'bold')).place(x=18,y=375)
        self.ManualOversentry=Entry(frame2,font=("",18,'bold'))
        self.ManualOversentry.place(x=168,y=375,width=50,height=25)

         #BUTTON ADD
        ManualOversAddbtn=Button(frame2,text="ADD ",font=("",13,'bold'),command=self.Overs_add)
        ManualOversAddbtn.place(x=225,y=375,width=80,height=27)
        ManualOversAddbtn.config(bg="green")
         #BUTTON REMOVE
        ManualOversRemovebtn=Button(frame2,text="REMOVE ",font=("",13,'bold'),command=self.Overs_removed)
        ManualOversRemovebtn.place(x=315,y=375,width=80,height=27)
        ManualOversRemovebtn.config(bg="RED")

     #############################################################################
         ####***BALLS ADD Or REMOVE***####          
        # ENTRY FOR MANUAL BALLS
        ManualBallslbl=Label(frame2,text=" UPDATE BALLS ",font=("",12,'bold')).place(x=18,y=405)
        self.ManualBallsentry=Entry(frame2,font=(".0",18,'bold'))
        self.ManualBallsentry.place(x=168,y=405,width=50,height=25)

         #BUTTON ADD
        ManualBallsAddbtn=Button(frame2,text="ADD ",font=("",13,'bold'),command=self.Balls_add)
        ManualBallsAddbtn.place(x=225,y=405,width=80,height=27)
        ManualBallsAddbtn.config(bg="green")
         #BUTTON REMOVE
        ManualBallsRemovebtn=Button(frame2,text="REMOVE ",font=("",13,'bold'),command=self.Balls_removed)
        ManualBallsRemovebtn.place(x=315,y=405,width=80,height=27)
        ManualBallsRemovebtn.config(bg="RED")        

     #############################################################################
        #### CLEAR #####

         #BUTTON ADD
        CLEARMATCHdbtn=Button(frame2,text="CLEAR ALL ",font=("",10,'bold'),command=self.Clear_All_Data)
        CLEARMATCHdbtn.place(x=295,y=465,width=100,height=20)
        CLEARMATCHdbtn.config(bg="#B2BEB5")
        
#============### Frame-3 BATTERS DETAILS ###================================
        frame3=Frame(self.root)
        frame3.place(x=420,y=50,width=795,height=50)

#==============================================================================
        
        #=============Striker Label=================
        self.Stri=StringVar()
        self.Stri.set("BATA 1")
        self.Bata1lbl=Label(frame3,text="",textvariable=self.Stri,font=("",18,"")) 
        self.Bata1lbl.pack(side=LEFT,padx=(18,0))

        self.StriRuns=StringVar()
        self.StriRuns.set("0")
        self.Bata1Runslbl=Label(frame3,text="",textvariable=self.StriRuns,font=("",18,"")) 
        self.Bata1Runslbl.pack(side=LEFT,padx=(8,0))

        self.StriBalls=StringVar()
        self.StriBalls.set("(0)")
        self.Bata1Ballslbl=Label(frame3,text="",textvariable=self.StriBalls,font=("",12,"")) 
        self.Bata1Ballslbl.pack(side=LEFT)

        self.Strinotout=StringVar()
        self.Strinotout.set("")
        self.Bata1Notoutlbl=Label(frame3,text="",textvariable=self.Strinotout,font=("",20,"")) 
        self.Bata1Notoutlbl.pack(side=LEFT)        
        #=============Non Striker Label=================
        self.Nonstr=StringVar()
        self.Nonstr.set("BATA 2")
        self.Bata2lbl=Label(frame3,text="",textvariable=self.Nonstr,font=("",18,"")) 
        self.Bata2lbl.pack(side=LEFT,padx=(22,0))

        self.NonstrRuns=StringVar()
        self.NonstrRuns.set("0")
        self.Bata2Runslbl=Label(frame3,text="",textvariable=self.NonstrRuns,font=("",18,"")) 
        self.Bata2Runslbl.pack(side=LEFT,padx=(8,0))

        self.NonstrtrBalls=StringVar()
        self.NonstrtrBalls.set("(0)")
        self.Bata2Ballslbl=Label(frame3,text="",textvariable=self.NonstrtrBalls,font=("",12,"")) 
        self.Bata2Ballslbl.pack(side=LEFT)

        self.Nonstrtrnotout=StringVar()
        self.Nonstrtrnotout.set("")
        self.Bata2Notoutlbl=Label(frame3,text="",textvariable=self.Nonstrtrnotout,font=("",20,"")) 
        self.Bata2Notoutlbl.pack(side=LEFT)

#============### Frame-4 PLAYERS CONTROL PALLETE #### =====================
        frame4=Frame(self.root)
        frame4.place(x=450,y=120,width=410,height=500)
        frame4.config(bg="black") 
#==================================================================================
# *********  BATA 1 *********       
        # ENTRY FOR BATA1 NAME
        Bata1lbl=Label(frame4,text=" BATTER 1 ",foreground="Black", background="Yellow",font=("",10,'bold')).place(x=10,y=10)
        self.Bata1Nameentry=Entry(frame4,font=(".0",12,'bold'))
        self.Bata1Nameentry.place(x=10,y=45,width=190,height=30)
         #BATA1 NAME UPDATE BUTTON
        Bata1name=Button(frame4,text="UPDATE",font=("",12,'bold'),command=self.Bata1_Name_Update)
        Bata1name.place(x=210,y=45) 
        Bata1name.config(bg="green")

         #BATA1 OUT UPDATE BUTTON
        Bata1name=Button(frame4,text="WICKET",font=("",12,'bold'),command=self.Bata1_OUT)
        Bata1name.place(x=315,y=45) 
        Bata1name.config(bg="RED")

     #===============
# *********  BATA 2 *********           
        # ENTRY FOR BATA2 NAME
        Bata2lbl=Label(frame4,text=" BATTER 2 ",foreground="Black", background="Yellow",font=("",10,'bold')).place(x=10,y=135)
        self.Bata2Nameentry=Entry(frame4,font=(".0",12,'bold'))
        self.Bata2Nameentry.place(x=10,y=170,width=190,height=30)
         #BATA2 NAME UPDATE BUTTON
        Bata2name=Button(frame4,text="UPDATE",font=("",12,'bold'),command=self.Bata2_Name_Update)
        Bata2name.place(x=210,y=170) 
        Bata2name.config(bg="green")

         #BATA2 OUT UPDATE BUTTON
        Bata2name=Button(frame4,text="WICKET",font=("",12,'bold'),command=self.Bata2_OUT)
        Bata2name.place(x=315,y=170) 
        Bata2name.config(bg="RED")

#####@@@@@@@@@Change Strikers@@@@@@@@@@@@####

         #STRIKERS CHANGE BUTTON
        STRIKERCHANGE=Button(frame4,text="< CHANGE STRIKER > ",font=("",16,'bold'),command=self.Striker_Change)
        STRIKERCHANGE.place(x=10,y=90,width=385,height=35) 
        STRIKERCHANGE.config(bg="BLUE")        
        STRIKERCHANGE.config(fg="Yellow")

#++++++++++++++++++++++++++++++#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Helper Methods For Bata Score Change========================
    def batsmen_runs(self,runs:int,is_striker_change:bool):
   
        print("runs ",runs , "| striker change ",is_striker_change)

    
        for batsman in self.batsmen:
                if batsman["is_striker"] == True:
                        batsman ["Batascore"] += runs


                        if is_striker_change == True:
                            batsman ["is_striker"] = False


                else:
                    if is_striker_change == True:
                            batsman["is_striker"] = True




#=======================================================================================
        print(self.batsmen[1]["Batascore"])
        print(self.batsmen[0]["Batascore"])
#Helper Methods For Bata Balls Change===============================================================

    def batsmen_balls(self,balls:int,is_striker_change:bool):
   
        print("balls ",balls , "| striker change ",is_striker_change)
    
        for striballs in self.bataballs: 
                if striballs["is_striker"] == True: 
                        striballs ["Bataballs"] += balls
                      


                        if is_striker_change == True:
                            striballs ["is_striker"] = False


                       
              
                else:
                    if is_striker_change == True:
                            striballs["is_striker"] = True
#==================================================================================
        print(self.bataballs[1]["Bataballs"])
        print(self.bataballs[0]["Bataballs"]) 
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#=====ACTIVE BUTTONS TO COMMAND========================
    #COMMAND TEAM NAME
    def Team_score_bug_name (self):
        print("hhhhh")
        batting_short_name = self.TeamShortnameentry.get()
        if (len(batting_short_name)>2):
          self.team_name.set(batting_short_name)
          self.match_details["batting_team"]["short_name"] = batting_short_name
          self.gl.write_match_details(self.match_details)
        else:
          print("Team name should be atleast 3 charactor long")
    #______________________________________________
        
     #COMMAND BALLS TO OVER ENTRY (DISPLAY)
    def Balls_To_Over (self):
        balls_per_over = int(self.BallsToOventry.get())
       
        if (balls_per_over>0):
              self.BallsToOver.set(balls_per_over) 
              self.match_details["balls_per_over"]= balls_per_over
              self.gl.write_match_details(self.match_details)
        else:
             print("balls_per_over should be more than 0")
             
    #_________________________________________________    
 
#===============================================================================================        
     #COMMAND VALID SCORE
           
            # @@ AUTO SCORE BUTTONS @@ 
    def update_runs(self,runs):
        self.current_runs = runs
        
    


    ######## BUYS & LEG BUYS AUTO BUTTON####  
            
    def buys_Lb_1(self):
         global MainScore
         MainScore+=1
         self.Legal.set(MainScore)  
         self.batsmen_balls(1,True)
         self.batsmen_runs(0,True)          

    def buys_Lb_2(self):
         global MainScore
         MainScore+=2
         self.Legal.set(MainScore)
         self.batsmen_balls(2,False)          
         self.batsmen_runs(0,False) 

    def buys_Lb_3(self):
         global MainScore
         MainScore+=3
         self.Legal.set(MainScore)
         self.batsmen_balls(3,True) 
         self.batsmen_runs(0,True)

    def buys_Lb_4(self):
         global MainScore
         MainScore+=4
         self.Legal.set(MainScore)
         self.batsmen_balls(4,False) 
         self.batsmen_runs(0,False) 

    def buys_Lb_5(self):
         global MainScore
         MainScore+=5
         self.Legal.set(MainScore)
         self.batsmen_balls(5,True) 
         self.batsmen_runs(0,True)

    def buys_Lb_6(self):
         global MainScore
         MainScore+=6
         self.Legal.set(MainScore)
         self.batsmen_balls(6,False) 
         self.batsmen_runs(0,False) 

    ######## EXTRA RUNS UPDATES BUTTON ####
    def Extra_add(self):
         global MainScore
         MainScore+=int(self.ExtraRunsentry.get())
         self.Total.set(MainScore) 

    ######## MANUAL SCORE CORRECTION BUTTON ####
    def Runs_add(self):
         global MainScore
         MainScore+=int(self.ManualRunsentry.get())
         self.Total.set(MainScore)    
     #
    def Runs_removed(self):
         global MainScore
         MainScore-=int(self.ManualRunsentry.get())
         self.Total.set(MainScore)    

    ######## MANUAL OVERS CORRECTION BUTTON ####
    def Overs_add(self):
         global Overs
         Overs+=int(self.ManualOversentry.get())
         self.Play_Overs.set(Overs)    
     #
    def Overs_removed(self):
         global Overs
         Overs-=int(self.ManualOversentry.get())
         self.Play_Overs.set(Overs)

    ######## MANUAL BALLS CORRECTION BUTTON ####
    def Balls_add(self):
         global ValidBalls
         ValidBalls+=int(self.ManualBallsentry.get())
         self.Play_Balls.set("."+str(ValidBalls))
     #
    def Balls_removed(self):
         global ValidBalls
         
         ValidBalls-=int(self.ManualBallsentry.get())
         self.Play_Balls.set("."+str(ValidBalls))



    #__________________________________________________
         #VALIDATE MAIN SCORE BALLS & OVERS SET      
    def Main_Score_Valid_Ball_Overs_Update(self):
          self.match_details["total_balls"] = self.match_details["total_balls"] +1
          self.match_details["batting_team"]["stats"]["score"] = self.match_details["batting_team"]["stats"]["score"] + self.current_runs
          self.Legal.set(self.match_details["batting_team"]["stats"]["score"])
          
          is_over_end , formatted_over = self.gl.is_over_end(self.match_details["total_balls"],self.match_details["balls_per_over"])
          self.match_details["batting_team"]["stats"]["overs"] = formatted_over
          self.match_details = self.gl.update_balls(self.current_runs,self.match_details)
          
          if is_over_end:
               self.match_details = self.gl.change_striker(self.match_details)
          # print(self.gl.is_over_end(self.match_details["total_balls"],self.match_details["balls_per_over"]))
          
          
     #     self.StriRuns.set(self.batsmen[0]["Batascore"])
     #     self.StriBalls.set(self.bataballs[0]["Bataballs"])

     #     self.NonstrRuns.set(self.batsmen[1]["Batascore"])
     #     self.NonstrtrBalls.set(self.bataballs[1]["Bataballs"])

    def Clear_All_Data (self):
        global MainScore, ValidBalls, Overs
       
        ValidBalls=0
        Overs=0
        MainScore=0
        a="TEAM"
       
        self.team_name.set(a)
        
        self.Total.set(MainScore)
        
        
        self.Wickets.set("/0")
        self.Play_Overs.set(Overs)
        self.Play_Balls.set("."+str(ValidBalls))

    #__________________________________________________
             # STRIKER CHANGE
    def Striker_Change (self):
             self.match_details = self.gl.change_striker(self.match_details)


    #__________________________________________________
         # BATA 1 CONFIG
    def Bata1_Name_Update (self):
         a=self.Bata1Nameentry.get()
         self.Stri.set(a)         

    def Bata1_OUT (self):
          global  Bata1Runs,Bata1Balls,Wickets
          a=""
          self.Stri.set(a)

          Wickets+=1 
          W=self.Wickets.set("/ "+str(Wickets))
          if Wickets==10:
             self.Wickets.set(" ")
             Wickets=0 
          for index, batsman in enumerate(self.batsmen):
               if batsman["is_striker"] == True:
                    self.batsmen[index] = self.empty_batsman
                    self.StriRuns.set(0)
                    self.StriBalls.set(0)
                    self.Stri.set("")






    
    #__________________________________________________
         # BATA 2 CONFIG

    def Bata2_Name_Update (self):
         a=self.Bata2Nameentry.get()
         self.Nonstr.set(a)        

    def Bata2_OUT (self):
          global  Bata1Runs,Bata1Balls,Wickets
          a=""
          self.Stri.set(a)

          Wickets+=1 
          W=self.Wickets.set("/ "+str(Wickets))
          if Wickets==10:
             self.Wickets.set(" ")
             Wickets=0 
          for index, batsman in enumerate(self.batsmen):
               if batsman["is_striker"] == True:
                    self.batsmen[index] = self.empty_batsman
                    self.NonstrRuns.set(0)
                    self.NonstrtrBalls.set(0)
                    self.Stri.set("")

    
  

        
        

        
        

 
          

        



        


        

       



           
           


        
        
       

        
        
        
        
             












if __name__=="__main__": 
    root=Tk()
    root.title('CRICK SCORE')
#     root.iconbitmap('download.ico')
    app=Cricket(root)
    root.mainloop()