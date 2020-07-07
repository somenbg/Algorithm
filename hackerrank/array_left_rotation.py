arr = [1,2,3,4,5]

rotation = 4

rot_array = [None] * len(arr)

for i in range(len(arr)):

    updated_index = (i + rotation) % len(arr)
    rot_array[i] = arr[updated_index]

print(arr)

print(rot_array)