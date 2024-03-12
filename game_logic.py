import json
import copy


class GameLogic:
    empty_batsman = {
        "name": "",
        "runs": 0,
        "balls": 0,
        "is_out": False,
        "is_striker": False,
        "is_playing": False}
    batsmen = []
    bowlers = []
    match_details = None

    def __init__(self) -> None:

        self.batsmen = [
            {"name": "batsman_1", "runs": 0, "balls": 0, "is_striker": True, "is_out": False},  # object = dictonery
            {"name": "batsman_2", "runs": 0, "balls": 0, "is_striker": False,
             "is_out": False}]  # array(list) of objects (dictoneries)

        self.bowlers = [
            {"name": "bowler_1", "overs": "0.0", "balls": 0, "maidens": 0, "runs": 0, "wickets": 0,
             "is_current_bowler": True}]

        self.match_details = {
            "batting_team": {
                "short_name": "",
                "long_name": "",
                "image": "",
                "batsmen": [],
                "stats": {
                    "score": 0,
                    "overs": 0.0,
                    "RR": 0.0,
                    "wickets": 0
                }
            },
            "bowling_team": {
                "short_name": "",
                "long_name": "",
                "image": "",
                "bowlers": self.bowlers,
                "stats": {
                    "score": 0,
                    "overs": 0.0,
                    "RR": 0.0,
                    "wickets": 0
                }
            },
            "balls_per_over": 0,
            "match_balls": 0,
            "total_overs": 0,
            "last_over": [],
            "this_over": []
        }
        print(self.get_match_details())

    def get_match_details(self):
        try:
            with open('sample.json', 'r') as file:
                # Load JSON data from the file
                match_details = json.load(file)

                return match_details
        except:
            self.write_match_details(self.match_details)
            return self.match_details

    def write_match_details(self, match_details):
        json_object = json.dumps(match_details, indent=4)

        # Writing to sample.json
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)

    def update_ball(self, runs, is_wicket, match_details):
        match_details["batting_team"]["stats"]["score"] = match_details["batting_team"]["stats"]["score"] + runs
        match_details["match_balls"] = match_details["match_balls"] + 1
        is_over_end, match_details["batting_team"]["stats"]["overs"] = self.is_over_end(match_details["match_balls"],
                                                                                        match_details["balls_per_over"])
        match_details["this_over"].append(runs)
        for batsman in match_details["batting_team"]["batsmen"]:
            if batsman["is_out"] == False and batsman["is_striker"] == True:
                batsman["runs"] += runs
                batsman["balls"] += 1

                if runs % 2 == 1:
                    batsman["is_striker"] = False
                    continue


            elif batsman["is_out"] == False and batsman["is_striker"] == False:
                if runs % 2 == 1:
                    batsman["is_striker"] = True

        for bowler in match_details["bowling_team"]["bowlers"]:
            if bowler["is_current_bowler"]:
                bowler["balls"] = bowler["balls"] + 1
                bowler["runs"] = bowler["runs"] + runs
                bowler["wickets"] = bowler["wickets"] + 1 if is_wicket else bowler["wickets"]
                _, bowler["overs"] = self.is_over_end(bowler["balls"], match_details["balls_per_over"])
                if is_over_end:
                    if all(value == 0 for value in match_details["this_over"]):
                        bowler["maidens"] = bowler["maidens"] + 1

        if is_over_end:
            match_details["last_over"] = copy.deepcopy(match_details["this_over"])
            match_details["this_over"] = []
            self.change_striker(match_details)

        self.write_match_details(match_details)
        return match_details

    def is_over_end(self, current_balls, balls_per_over):
        over = current_balls // balls_per_over
        ball = current_balls % balls_per_over
        if ball == 0:
            formatted_over = f"{over - 1}.{balls_per_over}"
            return True, formatted_over
        formatted_over = f"{over}.{ball}"
        return False, formatted_over

        # over = number // balls_per_over
        # ball = number % balls_per_over
        # if ball == 0:
        #     ball = balls_per_over
        # result = f"{over}.{ball}"

    def change_striker(self, match_details):
        for batsman in match_details["batting_team"]["batsmen"]:
            if batsman["is_out"] == False and batsman["is_striker"] == True:
                batsman["is_striker"] = False
                continue
            elif batsman["is_out"] == False and batsman["is_striker"] == False:
                batsman["is_striker"] = True
        self.write_match_details(match_details)
        return match_details

    def get_striker(self, match_details):
        for batsman in match_details["batting_team"]["batsmen"]:
            if not batsman["is_out"] and batsman["is_striker"] and batsman["is_playing"]:
                return batsman

    def get_non_striker(self, match_details):
        for batsman in match_details["batting_team"]["batsmen"]:
            if not batsman["is_out"] and not batsman["is_striker"] and batsman["is_playing"]:
                return batsman

    def get_current_bowler(self, match_details):
        for bowler in match_details["bowling_team"]["bowlers"]:
            if bowler["is_current_bowler"]:
                return bowler

    # def add_new_batsman(self, batsman, match_details):
    #     match_details["batting_team"]["batsmen"].append(batsman)
    #     return match_details

    def add_new_batsman(self, batsman, match_details):
        for index, temp_batsman in enumerate(match_details["batting_team"]["batsmen"]):
            if batsman["name"] == temp_batsman["name"]:
                del match_details["batting_team"]["batsmen"][index]
                break
        match_details["batting_team"]["batsmen"].append(batsman)
        return match_details


GameLogic()
