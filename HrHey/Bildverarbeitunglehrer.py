import copy


def mirror2(image):
    mirrored = []

    for i in range(len(image)):
        row = copy.deepcopy(image[i])
        row.reverse()
        mirrored.append(row)

    return mirrored


print(greyimage)
new_image = mirror2(greyimage)
print(new_image)
