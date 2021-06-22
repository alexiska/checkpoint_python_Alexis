def get_points(emp):
    points = 0
    for key, val in emp.items():
        if key == 'calls':
            points += val*10
            if val > 150:
                points += 100 # I assume that they will only get 100p once they reach obove the criteria for calls
        elif key == 'meetings':
            points += val*30
            if val > 20:
                points += 100 # I assume that they will only get 100p once they reach obove the criteria for meetings
        else:
            points += val*100
            if val > 5:
                points += 100 # I assume that they will only get 100p once they reach obove the criteria for sales
    print(f"Total points: {points}")
        
jordan_belfort = {"calls": 178, "meetings":17,  "sales":6}
bill_bull = {"calls": 138, "meetings":41,  "sales":4}
get_points(jordan_belfort)
get_points(bill_bull)