import random
import statistics
random_no = [random.randint(1, 10) for _ in range(25)]

print("random generated list ", random_no)

mean = statistics.mean(random_no)
median = statistics.median(random_no)
mode = statistics.mode(random_no)


print("the mean is : ", mean)
print("the median is : ", median)
print("the mode is : ", mode)
