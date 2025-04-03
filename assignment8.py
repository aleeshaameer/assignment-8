import matplotlib.pyplot as plt
import seaborn as sns


years = [2010, 2011, 2012, 2013, 2014, 2015, 2016]
city_a = [500000, 550000, 600000, 650000, 700000, 750000, 800000]
city_b = [800000, 850000, 900000, 950000, 1000000, 1050000, 1100000]
city_c = [1000000, 1050000, 1100000, 1150000, 1200000, 1250000, 1300000]
city_d = [1200000, 1250000, 1300000, 1350000, 1400000, 1450000, 1500000]

plt.plot(years, city_a, label="City A")
plt.plot(years, city_b, label="City B")
plt.plot(years, city_c, label="City C")
plt.plot(years, city_d, label="City D")
plt.xlabel("Years")
plt.ylabel("Population")
plt.title("Population of Cities Over Time")
plt.legend()
plt.show()


hours_studied = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_scores = [93, 57, 61, 54, 51, 53, 87, 81, 83, 85]

sns.scatterplot(x=hours_studied, y=test_scores)
plt.xlabel("Hours Studied")
plt.ylabel("Test Scores")
plt.title("Relationship Between Hours Studied and Test Scores")
plt.show()


months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = [11860, 10480, 4997, 5523, 13965, 6011, 13158, 9533, 5158, 9058, 11346, 6675]

plt.bar(months, sales)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Total Sales for Each Month")
plt.show()