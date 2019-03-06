

classes = ["Tin can", "Bottle", "Box", "Human", "Human leg", "Chair", "Tree"]
processed_images = []
newlines = []

annotation_file = 'annotation.txt'
with open(annotation_file) as f:
    lines = f.readlines()

lines = [x.strip() for x in lines] 
newline_counter = -1

for line in lines:

    chars = list(line)
    chars[34] = " "
    line = "".join(chars)

    curr_class = line.rsplit(',', 1)[1]
    class_num = classes.index(curr_class)

    line = line.rsplit(',', 1)[0]
    line = line + "," + str(class_num)

    img_name = line.rsplit(' ', 1)[0]

    if img_name in processed_images:
        newlines[newline_counter] = newlines[newline_counter] + " " + line.rsplit(' ', 1)[1]
    else:
        newline_counter = newline_counter + 1
        newlines.append(line)
        processed_images.append(img_name)

f.close()

with open('google_annotations.txt', 'a') as f:
    for line in newlines:
        f.write(line + '\n')
f.close()


