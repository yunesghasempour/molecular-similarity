from plot import heatmap , tanimoto_hist
from similarity import tanimoto_matrix , matrix_length

#heatmap colors
cols = ["plasma","magma","inferno","coolwarm","cividis","Greens","Blues","hot"]

# creat tanimoto matrix
file_path  = input("Enter your file please: ")
data = tanimoto_matrix(file_path)

# generate heatmap 
l =  matrix_length(file_path)
print("your file is OK")
hmi = input("do you want generate heatmap? y/n ")

if hmi =="y":

    hname = input("enter name for you heatmap(name.png)")

    for index, name in enumerate(cols):
        print(index, name)

    color = input("Enter a colormap number: ")
    col=cols[int(color)]


    heatmap(data,hname,col)
    print("heatmap generated")   
elif hmi == "n":
    print("OK heat map didn't generate")
else :
    print("unvalid input")


 




hst = input("do you want generate Histogram? y/n ")

if hst =="y":

    name = input("enter name for you Histogram(name.png) ")
    tanimoto_hist(data,name)
    print("Histogram generated")   
elif hst == "n":
    print("OK Histogram didn't generate")
else :
    print("unvalid input")


