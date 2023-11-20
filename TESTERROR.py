nums = [0,1,2,2,3,0,4,2]
val = 2

k = 0  # Змінна для відстеження нової довжини масиву
# Ітеруємося по елементах масиву
for i in range(len(nums)):
    print(f"i={i}")
    if nums[i] != 2135:
        print(f"nums[i]={nums[i]}")


        k += 1


print(f"{k}, {nums}")