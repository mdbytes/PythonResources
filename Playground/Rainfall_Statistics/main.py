def main():
    months = ["Jan", "Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    rainfall = get_monthly_input(months)
    statistics = calculate_stats(rainfall)
    display_results(statistics)

def get_monthly_input(months):
    rainfall = dict()
    for month in months:
        prompt = "Enter the rainfall for " + month + ": "
        monthly_rain = int(input(prompt))
        rainfall[month] = monthly_rain
    return rainfall

def calculate_stats(rainfall):
    stats = dict()
    stats["total"] = 0
    stats["high"] = 0
    stats["low"] = 1000000
    
    for month in rainfall:
        stats["total"] += rainfall[month]
        if rainfall[month] > stats["high"]:
            stats["high"] = rainfall[month]
            stats["high month"] = month
        if rainfall[month] < stats["low"]:
            stats["low"] = rainfall[month]
            stats["low month"] = month
    
    stats["average"] = stats["total"]/12

    return stats

def display_results(stats):
    print("\n\nRainfall Statistics\n")
    print(format("Total Rainfall:",'24'),stats["total"],"inches")
    print(format("Average Rainfall:",'24'),format(stats["average"],'.2f'),"inches per month")
    print(format("Low Rainfall: ",'24'),stats["low"],"inches the month of",stats["low month"])
    print(format("High Rainfall: ",'24'),stats["high"],"inches the month of",stats["high month"],"\n\n")


main()

