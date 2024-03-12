from tkinter import *
import customtkinter
from game_logic import GameLogic
import time
import re

gl = GameLogic()
match_details = gl.get_match_details()


class MatchMetaControlFrame(customtkinter.CTkFrame):
    # bat_short_name_entry = None
    # ball_short_name_entry = None
    # total_overs_entry = None
    # balls_perover_entry = None

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame, for example:
        self.bat_short_name_lbl = customtkinter.CTkLabel(self, text="Bat. Team Short Name")
        self.bat_short_name_lbl.grid(row=0, column=0, padx=20, pady=10)

        self.bat_short_name_entry = customtkinter.CTkEntry(master=self, placeholder_text="")
        self.bat_short_name_entry.grid(row=0, column=1, sticky="nsew", pady=10)

        self.ball_short_name_lbl = customtkinter.CTkLabel(self, text="Ball. Team Short Name")
        self.ball_short_name_lbl.grid(row=0, column=2, padx=20, pady=10)

        self.ball_short_name_entry = customtkinter.CTkEntry(master=self, placeholder_text="CTkEntry")
        self.ball_short_name_entry.grid(row=0, column=3, sticky="nsew", pady=10)

        self.total_overs_lbl = customtkinter.CTkLabel(self, text="Overs")
        self.total_overs_lbl.grid(row=0, column=4, padx=20, pady=10)

        self.total_overs_entry = customtkinter.CTkEntry(master=self, placeholder_text="CTkEntry")
        self.total_overs_entry.grid(row=0, column=5, sticky="nsew", pady=10, padx=20)

        self.balls_perover_lbl = customtkinter.CTkLabel(self, text="Balls per Over")
        self.balls_perover_lbl.grid(row=0, column=6, padx=20, pady=10)

        self.balls_perover_entry = customtkinter.CTkEntry(master=self, placeholder_text="CTkEntry")
        self.balls_perover_entry.grid(row=0, column=7, sticky="nsew", pady=10, padx=20)

        self.submit_meta_btn = customtkinter.CTkButton(master=self, text="Update Meta",
                                                       font=customtkinter.CTkFont(size=14), fg_color="teal",
                                                       command=self.update_meta)
        self.submit_meta_btn.grid(row=0, column=8, sticky="nsew", padx=3, pady=3)

    def update_meta(self):
        match_details["batting_team"]["short_name"] = self.bat_short_name_entry.get()
        match_details["bowling_team"]["short_name"] = self.ball_short_name_entry.get()
        match_details["total_overs"] = int(self.total_overs_entry.get())
        match_details["balls_per_over"] = int(self.balls_perover_entry.get())
        gl.write_match_details(match_details)
        UpdateUI()


class StatsShowFrame(customtkinter.CTkFrame):
    # bat_team_lbl = None
    # main_score_entry = None
    # main_overs_entry = None
    # striker_lbl = None
    # non_striker_lbl = None
    # bowler_lbl = None

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.bat_team_lbl = customtkinter.CTkLabel(self, text="", font=customtkinter.CTkFont(size=40))
        self.bat_team_lbl.grid(row=0, column=0, padx=20, )

        self.main_score_entry = customtkinter.CTkEntry(master=self, placeholder_text="0/0",
                                                       font=customtkinter.CTkFont(size=40))
        self.main_score_entry.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.main_overs_entry = customtkinter.CTkEntry(master=self, placeholder_text="0.0",
                                                       font=customtkinter.CTkFont(size=40))
        self.main_overs_entry.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)

        self.striker_lbl = customtkinter.CTkLabel(self, text="*Batsman1 10(10)", font=customtkinter.CTkFont(size=18))
        self.striker_lbl.grid(row=0, column=3, padx=20, )

        self.non_striker_lbl = customtkinter.CTkLabel(self, text="Batsman1 10(10)", font=customtkinter.CTkFont(size=18))
        self.non_striker_lbl.grid(row=0, column=4, padx=20, )

        self.divider_lbl = customtkinter.CTkLabel(self, text="|", font=customtkinter.CTkFont(size=18))
        self.divider_lbl.grid(row=0, column=5, padx=20, )

        self.bowler_lbl = customtkinter.CTkLabel(self, text="Bowler 0.0 2 0 5", font=customtkinter.CTkFont(size=18))
        self.bowler_lbl.grid(row=0, column=6, padx=20, )

        self.ball_team_lbl = customtkinter.CTkLabel(self, text="", font=customtkinter.CTkFont(size=40))
        self.ball_team_lbl.grid(row=0, column=7, padx=20, )


class ScoreControllFrame(customtkinter.CTkFrame):
    current_runs = 0

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        nums = [0, 1, 2, 3, 4, 6]  # Define the numbers for the buttons
        # self.num_buttons = []  # Create a list to store the button instances

        for i, num in enumerate(nums):
            num_btn = customtkinter.CTkButton(master=self, text=str(num), font=customtkinter.CTkFont(size=30), width=50,
                                              command=lambda num=num: self.set_current_run(num))
            num_btn.grid(row=0, column=i, sticky="nsew", padx=3, pady=3)

        self.add_ball_btn = customtkinter.CTkButton(master=self, text="Ball", font=customtkinter.CTkFont(size=25),
                                                    width=150, fg_color="teal",
                                                    command=lambda: self.submit_ball(match_details))
        self.add_ball_btn.grid(row=0, column=6, sticky="nsew", padx=3, pady=3)

        def open_extras_window():
            if self.extras_window is None or not self.extras_window.winfo_exists():
                self.extras_window = ExtrasWindow(self)  # create window if its None or destroyed
            else:
                self.extras_window.focus()  # if window exists focus it

        self.extras_btn = customtkinter.CTkButton(master=self, text="Extras", font=customtkinter.CTkFont(size=25),
                                                  width=150, fg_color="orange", command=open_extras_window)
        self.extras_btn.grid(row=1, column=0, sticky="nsew", padx=3, pady=3, columnspan=7)

        self.extras_window = None

    def set_current_run(self, runs):
        self.current_runs = runs

    def submit_ball(self, match_details):
        match_details = gl.update_ball(self.current_runs, False, match_details)
        UpdateUI()


class BattersControlFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        batsman_1 = match_details["batting_team"]["batsmen"][0]
        batsman_2 = match_details["batting_team"]["batsmen"][1]
        self.single_batter_frame_1 = SingleBatterFrame(master=self, batsman=batsman_1, index=0)
        self.single_batter_frame_1.grid(row=0, column=0, padx=20, pady=4, sticky="nsew")

        self.single_batter_frame_2 = SingleBatterFrame(master=self, batsman=batsman_2, index=1)
        self.single_batter_frame_2.grid(row=1, column=0, padx=20, pady=4, sticky="nsew")
        # self.single_batter_frame = SingleBatterFrame(master=self)
        # self.single_batter_frame.grid(row=0, column=0, padx=20, pady=20 ,sticky="nsew" )
        # match_details["batting_team"]["batsmen"]
        # count = len(match_details["batting_team"]["batsmen"]) + 1

        # add batsman button
        # self.add_batsman_batters_control_frame = customtkinter.CTkButton(master=self, text="+",
        #                                                                  font=customtkinter.CTkFont(size=15), width=100,
        #                                                                  command=lambda: self.add_new_batsman(count,
        #                                                                                                       gl.empty_batsman))
        # self.add_batsman_batters_control_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        # for index, batsman in enumerate(match_details["batting_team"]["batsmen"]):
        #     self.add_new_batsman(index, batsman)

    def add_new_batsman(self, count, batsman):  # adds a new batsman frame
        self.single_batter_frame = SingleBatterFrame(master=self, batsman=batsman)
        self.single_batter_frame.grid(row=count, column=0, padx=20, pady=4, sticky="nsew")

        self.single_batter_frame = SingleBatterFrame(master=self, batsman=batsman)
        self.single_batter_frame.grid(row=count, column=0, padx=20, pady=4, sticky="nsew")
        # if not batsman["name"] == "":
        #     self.single_batter_frame.single_batsman_update_btn.grid_remove()
        #     self.single_batter_frame.single_batsman_play_out_btn.configure(
        #         text='out' if batsman["is_playing"] else "Play",
        #         command=lambda: self.single_batter_frame.update_play_out(batsman, match_details))
        #     # if not batsman["is_playing"] and batsman["is_out"]:
        #     #     self.single_batter_frame.single_batsman_play_out_btn.grid_remove()
        # self.add_batsman_batters_control_frame.grid(row=count + 1, column=0, sticky="nsew", padx=10, pady=10)


class BowlersControlFrame(customtkinter.CTkFrame):
    count = 0

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # self.single_batter_frame = SingleBatterFrame(master=self)
        # self.single_batter_frame.grid(row=0, column=0, padx=20, pady=20 ,sticky="nsew" )

        self.add_batsman_bowlers_control_frame = customtkinter.CTkButton(master=self, text="Add Bowler",
                                                                         font=customtkinter.CTkFont(size=15), width=100,
                                                                         command=lambda: self.add_new_bowler(
                                                                             self.count))
        self.add_batsman_bowlers_control_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    def add_new_bowler(self, count):
        self.single_bowler_frame = SingleBowlerFrame(master=self)
        self.single_bowler_frame.grid(row=count, column=0, padx=20, pady=4, sticky="nsew")
        self.count = count + 1
        self.add_batsman_bowlers_control_frame.grid(row=self.count + 1, column=0, sticky="nsew", padx=10, pady=10)


class SingleBatterFrame(customtkinter.CTkFrame):
    def __init__(self, master, batsman, index, **kwargs):
        super().__init__(master, **kwargs)
        self.single_batsman_name_entry = customtkinter.CTkEntry(master=self, placeholder_text=f"Batsman {index}")
        self.single_batsman_name_entry.insert(0, batsman["name"])
        self.single_batsman_name_entry.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.single_batsman_score_entry = customtkinter.CTkEntry(master=self, placeholder_text="0(0)")
        self.single_batsman_score_entry.insert(0, f'{batsman["runs"]}({batsman["balls"]})')
        self.single_batsman_score_entry.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        # self.single_batsman_is_out_btn = customtkinter.CTkButton(master=self, text="OUT",
        #                                                          font=customtkinter.CTkFont(size=15), width=100)
        # self.single_batsman_is_out_btn.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)

        # self.single_batsman_update_btn = customtkinter.CTkButton(master=self, text="Add To List",
        #                                                          font=customtkinter.CTkFont(size=15), width=100,
        #                                                          command=lambda: self.update_batsman_details(
        #                                                              match_details))
        # self.single_batsman_update_btn.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)

        self.single_batsman_play_out_btn = customtkinter.CTkButton(master=self, text="Play",
                                                                   font=customtkinter.CTkFont(size=15), width=100,
                                                                   command=lambda: (gl.write_match_details(
                                                                       self.update_play_out(batsman, match_details,
                                                                                            index)), UpdateUI()))
        self.single_batsman_play_out_btn.grid(row=0, column=3, sticky="nsew", padx=10, pady=10)
        # self.update_play_out(batsman, match_details, index)

    def update_batsman_details(self, match_details):
        batsman = {
            "name": self.single_batsman_name_entry.get(),
            "runs": int(re.findall(r'^(\d+)', self.single_batsman_score_entry.get())[
                            0]) if self.single_batsman_score_entry.get() else 0,
            "balls": int(re.findall(r'\((\d+)\)', self.single_batsman_score_entry.get())[
                             0]) if self.single_batsman_score_entry.get() else 0,
            "is_striker": False,
            "is_playing": False,
            "is_out": False,
        }
        # print(match_details,batsman )
        match_details = gl.add_new_batsman(batsman, match_details)
        gl.write_match_details(match_details)
        UpdateUI()
        # self.single_batsman_update_btn.grid_remove()

    def update_play_out(self, batsman, match_details, index):
        if batsman["name"] == "":
            batsman = {
                "name": self.single_batsman_name_entry.get(),
                "runs": int(re.findall(r'^(\d+)', self.single_batsman_score_entry.get())[
                                0]) if self.single_batsman_score_entry.get() else 0,
                "balls": int(re.findall(r'\((\d+)\)', self.single_batsman_score_entry.get())[
                                 0]) if self.single_batsman_score_entry.get() else 0,
                "is_striker": False,
                "is_playing": False,
                "is_out": False,
            }
        if not batsman["is_playing"] and not batsman["is_out"]:
            batsman["is_playing"] = True
            self.single_batsman_play_out_btn.configure(text='Out')
        elif batsman["is_playing"] and not batsman["is_out"]:
            batsman["is_playing"] = False
            batsman["is_out"] = True
            self.single_batsman_play_out_btn.configure(text='Play')
            self.single_batsman_name_entry.delete(0, "end")
            self.single_batsman_name_entry.insert(0, '')
            self.single_batsman_score_entry.delete(0, "end")
            self.single_batsman_score_entry.insert(0, '0(0)')
            match_details["batting_team"]["batsmen"][index] = gl.empty_batsman
            return match_details
            # self.single_batsman_play_out_btn.grid_remove()
        # match_details = gl.add_new_batsman(batsman, match_details)
        match_details["batting_team"]["batsmen"][index] = batsman
        return match_details
        # self.single_batsman_play_out_btn.configure(
        #     text='out' if batsman["is_playing"] else "Play")
        # gl.write_match_details(match_details)
        # # UpdateUI()


class SingleBowlerFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.single_bowler_name_entry = customtkinter.CTkEntry(master=self, placeholder_text="Bowler")
        self.single_bowler_name_entry.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.single_bowler_stats_entry = customtkinter.CTkEntry(master=self, placeholder_text="0.0 0 0 0")
        self.single_bowler_stats_entry.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.single_bowler_is_current_btn = customtkinter.CTkButton(master=self, text="Current Bowler",
                                                                    font=customtkinter.CTkFont(size=15), width=100)
        self.single_bowler_is_current_btn.grid(row=0, column=2, sticky="nsew", padx=10, pady=10, columnspan=7)


class ExtrasWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x150")

        self.extras_lbl = customtkinter.CTkLabel(self, text="Extras", font=customtkinter.CTkFont(size=18))
        self.extras_lbl.grid(row=0, column=0, padx=20, )

        self.extras_entry = customtkinter.CTkEntry(master=self, placeholder_text="0",
                                                   font=customtkinter.CTkFont(size=40))
        self.extras_entry.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        def extras_radio_event():
            print("radiobutton toggled, current value:", radio_var.get())

        radio_var = IntVar(value=0)
        self.extra_other_radio = customtkinter.CTkRadioButton(master=self, text="Other", command=extras_radio_event,
                                                              variable=radio_var, value=0, width=20)
        self.extra_other_radio.grid(row=0, column=2, sticky="nsew", padx=3, pady=10)
        self.extra_lb_radio = customtkinter.CTkRadioButton(master=self, text="LB/B", command=extras_radio_event,
                                                           variable=radio_var, value=1, width=20)
        self.extra_lb_radio.grid(row=0, column=3, sticky="nsew", padx=3, pady=10)

        self.extras_submit__window_btn = customtkinter.CTkButton(master=self, text="Submit",
                                                                 font=customtkinter.CTkFont(size=20), width=150, )
        self.extras_submit__window_btn.grid(row=1, column=1, sticky="nsew", padx=3, pady=3, columnspan=3)


class UpdateUI(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        match_details = gl.get_match_details()

        app.stats_show_frame.bat_team_lbl.configure(text=match_details["batting_team"]["short_name"])
        app.stats_show_frame.ball_team_lbl.configure(text=match_details["bowling_team"]["short_name"])

        app.stats_show_frame.main_score_entry.delete(0, "end")
        app.stats_show_frame.main_score_entry.insert(0,
                                                     f'{match_details["batting_team"]["stats"]["score"]}/{match_details["batting_team"]["stats"]["wickets"]}')
        app.stats_show_frame.main_overs_entry.delete(0, "end")
        app.stats_show_frame.main_overs_entry.insert(0, f'{match_details["batting_team"]["stats"]["overs"]}')

        striker = gl.get_striker(match_details)
        app.stats_show_frame.striker_lbl.configure(
            text=f'*{striker["name"]} - {striker["runs"]}({striker["balls"]})' if striker else '')

        non_striker = gl.get_non_striker(match_details)
        app.stats_show_frame.non_striker_lbl.configure(
            text=f'{non_striker["name"]} - {non_striker["runs"]}({non_striker["balls"]})' if non_striker else '')

        current_bowler = gl.get_current_bowler(match_details)
        app.stats_show_frame.bowler_lbl.configure(
            text=f'{current_bowler["name"]} - ov.{current_bowler["overs"]} - m.{current_bowler["maidens"]} - r.{current_bowler["runs"]} - w.{current_bowler["wickets"]})')

        app.batters_control_frame.single_batter_frame_1.update_play_out(match_details["batting_team"]["batsmen"][0],
                                                                        match_details, 0)
        app.batters_control_frame.single_batter_frame_2.update_play_out(match_details["batting_team"]["batsmen"][1],
                                                                        match_details, 1)
        # app.batters_control_frame.single_batter_frame_1.single_batsman_name_entry.insert(0,match_details["batting_team"]["batsmen"][0]["name"])
        # app.batters_control_frame.single_batter_frame_1.single_batsman_score_entry.insert(0,f'{match_details["batting_team"]["batsmen"][0]["runs"]}({match_details["batting_team"]["batsmen"][0]["balls"]}')


class App(customtkinter.CTk):
    stats_show_frame = None
    match_meta_controll_frame = None

    def __init__(self):
        super().__init__()
        # self.attributes("-fullscreen", True)

        # self.geometry("1280x760")
        # self.grid_rowconfigure(1, weight=1)  # configure grid system
        self.grid_columnconfigure(6, weight=1)
        self.stats_show_frame = StatsShowFrame(master=self)
        self.stats_show_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew", columnspan=6)
        self.stats_show_frame.bat_team_lbl.configure(text="sss")

        self.match_meta_controll_frame = MatchMetaControlFrame(master=self)
        self.match_meta_controll_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew", columnspan=6)

        self.score_controll_frame = ScoreControllFrame(master=self, width=400)
        self.score_controll_frame.grid(row=2, column=0, padx=20, pady=20, sticky="nsew", columnspan=3)

        self.batters_control_frame = BattersControlFrame(master=self)
        self.batters_control_frame.grid(row=2, column=3, padx=20, pady=20, sticky="nsew")

        self.bowlers_control_frame = BowlersControlFrame(master=self)
        self.bowlers_control_frame.grid(row=2, column=4, padx=20, pady=20, sticky="nsew")


app = App()
UpdateUI()
app.mainloop()
