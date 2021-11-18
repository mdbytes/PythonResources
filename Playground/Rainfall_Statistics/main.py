def main():
    rainfall = get_monthly_input()
    statistics = calculate_stats(rainfall)
    #display_results(statistics)

def get_monthly_input():
    rainfall = dict()
    months = ["Jan", "Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    for month in months:
        prompt = "Enter the rainfall for " + month + ": "
        monthly_rain = int(input(prompt))
        rainfall[month] = monthly_rain
    return rainfall

def calculate_stats(rainfall):
    stats = dict()
    total, hi = 0
    lo = 10000
    for month in rainfall:
        total += 
        


    return stats

main()

