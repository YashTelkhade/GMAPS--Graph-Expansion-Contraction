import matplotlib.pyplot as plt

import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import ImageTk,Image


class node:
  def __init__(self, place, location, point):
    self.place = place
    self.location = location
    self.point = point



win = tk.Tk()

win.title("Map Integration Project")
win.geometry("{0}x{1}+0+0".format(win.winfo_screenwidth(), win.winfo_screenheight()))

load=Image.open('C:\\Users\\dc\\Desktop\\DAAProjectGmaps\\gmapswall.jpg')
#load = load.resize((1900,1100))
render = ImageTk.PhotoImage(load)
img =tk.Label(win,image=render)
img.image = render
img.place(x=0,y=0)


tk.Button(win, text="+", bg="#FC4C00", fg="white", width=5, height=2, command=lambda: zoomin(arr)).place(relx=0.88, rely=0.65, anchor=tk.CENTER)
tk.Button(win, text="-", bg="orange", fg="white", width=5, height=2, command=lambda: zoomout(arr)).place(relx=0.88, rely=0.70, anchor=tk.CENTER)



      
def zoomin(arr):
  ct=0
  for i in range(len(arr)):
    if(arr[i].point == 1):
      pass
    else:
      ct=i
      break
  arr[ct].point=1
  arr[-(ct+1)].point=1
  plotter(arr)
  print("\n")
         
          
def zoomout(arr):
  ct=0
  t=int(len(arr)/2)
  for i in range(t):
    if(arr[i].point==0):
      ct=i-1
      break    
  if(ct==0):
    ct=t
  arr[ct].point=0
  arr[-(ct+1)].point=0
  plotter(arr)
    
def printarr(arr):
    s = "\n         DATA STRUCTURES\n\nPoints Visible on the Map are: \n"
    for i in arr:
        if(i.point==1):
            s =s +"             "+ i.place +str(i.location) + "\n"

    t = tk.Text(win, height=15, width=35, bg="black", fg="white")
    t.insert(tk.INSERT, s)
    t.place(relx=0.20, rely=0.5, anchor=tk.CENTER)
  
def plotter(arr):
    x=[]
    y=[]
    z=[]
    for i in arr:
        if(i.point==1):
            x.append(i.location[0])
            y.append(i.location[1])
            z.append(i.place)
  

    fig, ax = plt.subplots()
    #fig = plt.Figure(figsize=(2,1), dpi=200)
    #ax = fig.add_subplot(111)
    ax.scatter(y, x)

    
    for i, txt in enumerate(z):
        ax.annotate(txt, (y[i], x[i]))
    
    plt.plot(y,x,'-.or')
    plt.axis('off')
    plt.title('MAP')
    
    
    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.draw()
    canvas.get_tk_widget().place(relx=0.70, rely=0.5, anchor=tk.CENTER)
    
    printarr(arr)

    
    
def go():
    return
  


n=4
n=n*2+2
arr=[]
for i in range(0,n):
    k=chr(65+i)
    if(i==0 or i==(n-1)):
        arr.append(node(k,(0,i+1),1))
    else:
        arr.append(node(k,(0,i+1),0))
plotter(arr)
    
win.mainloop() 