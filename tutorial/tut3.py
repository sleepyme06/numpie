import numpy as np
import matplotlib.pyplot as plt

# Data structure: [restaurant_id, 2021, 2022, 2023, 2024]
sales_data = np.array([
    [1, 150000, 180000, 220000, 250000],  # Paradise Biryani
    [2, 120000, 140000, 160000, 190000],  # Beijing Bites
    [3, 200000, 230000, 260000, 300000],  # Pizza Hub
    [4, 180000, 210000, 240000, 270000],  # Burger Point
    [5, 160000, 185000, 205000, 230000]   # Chai Point
])
print("===== Zomato Sales Analysis ====")
print("shape:",sales_data.shape)
print("first 3 restaurant sales:\n",sales_data[:3])#[:,1:]
print("total sales per year:",np.sum(sales_data,axis=0))
print("yearly total:",np.sum(sales_data[:,1:],axis=0))
print("minimum sales per restaurant:",np.min(sales_data[:,1:],axis=1))
print("maximum sales per year:",np.max(sales_data[:,1:],axis=0))
print("average sales per restaurant:",np.mean(sales_data[:,1:],axis=1))
print("cumilative sales:",np.cumsum(sales_data[:,1:],axis=1))

plt.figure(figsize=(10,6))
years = [2021, 2022, 2023, 2024]
plt.plot(years, np.mean(sales_data[:,1:], axis=0))
plt.title("Average cumulative sales across all restaurants")
plt.xlabel("years")
plt.ylabel("sales")
plt.grid(True)
plt.show()

vector1=np.array([1,2,3,4,5])
vector2=np.array([6,7,8,9,10])
print("add:",vector1+vector2)
print("multiply:",vector1*vector2)
print("dot multiply:",np.dot(vector1,vector2))
print("angles:",np.arccos(np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))))

restaurant_type=np.array(['biriyani','chinese','pizza','burger','cafe'])#3*3 imagine
vectorized_upper=np.vectorize(str.upper)
print("vectprized upper",vectorized_upper(restaurant_type))

monthly_avg=sales_data[:,1:]/12
#scalernum broadcast
print(monthly_avg)
