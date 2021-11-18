def main():
    rainfall = get_monthly_input()
    statistics = calculate_stats(rainfall)
    display_results(statistics)


def get_monthly_input():
    rainfall = dict()
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    for month in months:
        prompt = "Enter the rainfall for " + month + ": "
        monthly_rain = int(input(prompt))
        rainfall[month] = monthly_rain
    return rainfall


def calculate_stats(rainfall):
    stats = dict()
    num_months = 0
    total=0
    hi = 0
    lo = 10000

    for month in rainfall:
        total += rainfall[month]
        if rainfall[month] < lo:
            lo = rainfall[month]
            lo_month = month
        if rainfall[month] > hi:
            hi = rainfall[month]
            hi_month = month
        num_months += 1

    stats["Average"] = total / num_months
    stats["Total"] = total
    stats["High"] = hi
    stats["High month"] = hi_month
    stats["Low"] = lo
    stats["Low month"] = lo_month

    return stats


def display_results(stats):
    print("Rainfall Statistics")
    print("")
    for stat in stats:
        print('{:>10}  {:>10}'.format(stat,stats[stat]))
    print("")

main()
