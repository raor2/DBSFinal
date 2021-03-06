
title = "\n\n\t\t\t\tExploration of Crime and Employment Data for New York"

title = title.center(24)

print("Loading Data...")
exec(open('load_data.py').read())
print("Data Loaded")
print(title)
print("Team Members:\nYang Zhang\nDan Southwick\nZhengneng Chen\nRyan Rao\n\n") #Everyone else add your names here

print("List of Available Features:\n\t1. Explore Crime Data by Area and by County\n\t2. Explore New York Industry Data by Area\n\t3. Visualize Employment and Crime Data For a Given Area\n\t4. Prioritized Living Area Recommendation Based On Crime and Employment")

while(1):
    choice = input("\nEnter a feature choice, q to quit or f to see the features again:\n")

    if(choice == 'q'):
        break
    if(choice == 'f'):
        print("List of Available Features:\n\t1. Explore Crime Data by Area and by County\n\t2. Explore New York Industry Data by Area\n\t3. Visualize Employment and Crime Data For a Given Area\n\t4. Prioritized Living Area Recommendation Based On Crime and Employment ")
    if(choice == '1'):
        print("Feature 1")
        exec(open('database1.py').read())
    if(choice == '2'):
        print("Feature 2")
        exec(open('database2.py').read())
    if(choice == '3'):
        print("Feature 3")
        exec(open('database3.py').read())
    if(choice == '4'):
        print("Feature 4")
        exec(open('database4.py').read())


print("End program")
