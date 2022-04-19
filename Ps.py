import pandas as pd

data = pd.read_csv("Statistical-Survey-Assessment-_Responses_.csv")  # file read
f = len(data[data["Gender"] == 'F'])  # total count of female students
m = len(data[data["Gender"] == 'M'])  # total count of male students
f_avg_marks = (data[data["Gender"] == 'F']["CGPA"]).mean()  # mean marks of female students
m_avg_marks = (data[data["Gender"] == 'M']["CGPA"]).mean()  # mean marks of male students
print(f"For population, the ratio of avg female CGPA to avg male CGPA is {f_avg_marks / m_avg_marks}")
total_sample = int(input("Enter the number of Samples you want to take from the dataset:\n"))
sample_mean = []
for _ in range(total_sample):
    slice = int(input(f"Enter the Slicing number for {_ + 1} sample:\n"))

    sample_mean.append((data[data["Gender"] == 'F']["CGPA"].iloc[::slice]).mean() / (
        data[data["Gender"] == 'M']["CGPA"].iloc[::slice]).mean())  # append the ratio obtained to list
    print(f"For this sampling, the ratio of avg female CGPA to avg male CGPA is {sample_mean[_]}\n")

print(f"From the provided sample spaces,the mean of all ratio attained is {sum(sample_mean) / len(sample_mean)}")
