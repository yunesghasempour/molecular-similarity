from plot import heatmap 
cols = ["plasma","magma","inferno","coolwarm","cividis","Greens","Blues","hot"]



file_path  = input("Enter your file please: ")


print("your file is OK")

hmi = input("do you want generate heatmap? y/n ")

if hmi =="y":

    hname = input("enter name for you heatmap(name.png)")

    for index, name in enumerate(cols):
        print(index, name)

    color = input("Enter a colormap number: ")
    col=cols[int(color)]


    heatmap(file_path,hname,col)
    print("heatmap generated")



    
elif hmi == "n":
    print("OK heat map didn't generate")
else :
    print("unvalid input")
    

