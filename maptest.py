#To Create map and display distance
import gmplot
import tkinter as tk
from tkinter import *
from tkinter import ttk
###############################################

#Edit GUI

my_w = tk.Tk()
my_w.geometry("500x300")  # Size of the window
my_w.title("Route detection")  # Adding a title
filename=PhotoImage(file="gui2.png")
background_label=Label(my_w,image=filename)
background_label.place(x=0,y=0,relwidth=1,relheight=1)
my_w.resizable(False , False)
my_w.attributes('-alpha',0.9)
##################################################

#Creating Selectbox to Select the start point

options = tk.StringVar(my_w)
options.set("minuf") # default value
l1 = tk.Label(my_w,  text='Select Start', width=13,font=("arial",10,"bold"),bg="#006064",fg="white")
l1.place(x=80,y=100)
om1 =tk.OptionMenu(my_w, options, "shebin","minuf", "tala","birket as sab","el-bagour","ashmun","quwaysna","el sadat city","el shohada","Kafr El-Zayat","basioun","tanta","qutur","El-Mahalla El-Kubra","As Santah","Samannoud","zefta","banha","qalyub","Al Qanatir Al Khayriyyah","Shubra Al Khaymah","el khankah","kafr shokr","shibin el qanatir","toukh")
om1.place(x=96,y=135)
start=tk.StringVar(my_w)



#################################################

#Creation SelectBox to select End point
options2 = tk.StringVar(my_w)
options2.set("shebin") # default value
l2 = tk.Label(my_w,  text='Select end', width=13,font=("arial",10,"bold"),bg="#5E35B1",fg="white")
l2.place(x=200,y=100)
om2 =tk.OptionMenu(my_w, options2, "shebin","minuf", "tala","birket as sab","el-bagour","ashmun","quwaysna","el sadat city","el shohada","Kafr El-Zayat","basioun","tanta","qutur","El-Mahalla El-Kubra","As Santah","Samannoud","zefta","banha","qalyub","Al Qanatir Al Khayriyyah","Shubra Al Khaymah","el khankah","kafr shokr","shibin el qanatir","toukh")
om2.place(x=215,y=135)
end=tk.StringVar(my_w)


######################################################
#################################################

#Creation SelectBox to select Alogrithm
options3 = tk.StringVar(my_w)
options3.set("BFS") # default value
l3 = tk.Label(my_w,  text='Select Algorithm', width=13,font=("arial",10,"bold"),bg="#e91063",fg="white" )
l3.place(x=320,y=100)
om3 =tk.OptionMenu(my_w, options3, "BFS","DFS","A*")
om3.place(x=340,y=135)


b3 = tk.Button(my_w,  text='Show Road', command=lambda :my_show2(),bg="#e91063",fg="white",width=48,height=2,font=("arial",8,"bold"))
b3.place(x=80,y=195)
getAlgo=tk.StringVar(my_w)


######################################################
def my_show2():
    end.set(options2.get())
    start.set(options.get())
    getAlgo.set(options3.get())
    my_w.destroy()
    import os
    filename = 'file:///' + os.getcwd() + '/' + 'map.html'
    import webbrowser
    webbrowser.open_new_tab(filename)
#get the selected value and close the window

my_w.mainloop()

startP=start.get()#Start Node
endP=end.get()#End Node
Algo=getAlgo.get()#Algo selected
#print(startP)
#print(endP)
final_list=[]
if ((Algo=="BFS") and (startP!=endP)):
#breath first search
    from queue import Queue

    adj_list = {
        'shebin': ['tala', 'el shohada', 'minuf', 'el-bagour', 'quwaysna', 'birket as sab'],
        'minuf': ['el shohada', 'shebin', 'el-bagour', 'ashmun', 'el sadat city'],
        'tala': ['birket as sab', 'shebin', 'el shohada', 'Kafr El-Zayat', 'tanta', 'As Santah'],
        'birket as sab': ['tala', 'shebin', 'quwaysna', 'As Santah', 'zefta'],
        'el-bagour': ['quwaysna', 'shebin', 'minuf', 'ashmun', 'banha', 'toukh', 'Al Qanatir Al Khayriyyah'],
        'ashmun': ['el-bagour', 'minuf', 'el sadat city', 'Al Qanatir Al Khayriyyah', 'toukh'],
        'quwaysna': ['birket as sab', 'shebin', 'el-bagour', 'zefta', 'kafr shokr', 'banha'],
        'el sadat city': ['ashmun', 'minuf'],
        'el shohada': ['tala', 'shebin', 'minuf'],
        'Kafr El-Zayat': ['basioun', 'tanta', 'tala'],
        'basioun': ['qutur', 'tanta', 'Kafr El-Zayat'],
        'qutur': ['basioun', 'tanta', 'El-Mahalla El-Kubra'],
        'El-Mahalla El-Kubra': ['qutur', 'tanta', 'As Santah', 'zefta', 'Samannoud'],
        'Samannoud': ['El-Mahalla El-Kubra', 'As Santah', 'zefta'],
        'zefta': ['Samannoud', 'El-Mahalla El-Kubra', 'As Santah', 'quwaysna', 'birket as sab', 'kafr shokr'],
        'As Santah': ['Samannoud', 'El-Mahalla El-Kubra', 'birket as sab', 'tanta'],
        'tanta': ['tala', 'Kafr El-Zayat', 'basioun', 'qutur', 'El-Mahalla El-Kubra', 'As Santah'],
        'kafr shokr': ['zefta', 'quwaysna', 'banha'],
        'banha': ['kafr shokr', 'quwaysna', 'el-bagour', 'toukh', 'shibin el qanatir'],
        'toukh': ['banha', 'el-bagour', 'ashmun', 'Al Qanatir Al Khayriyyah', 'qalyub', 'shibin el qanatir'],
        'Al Qanatir Al Khayriyyah': ['toukh', 'ashmun', 'Shubra Al Khaymah', 'qalyub'],
        'Shubra Al Khaymah': ['Al Qanatir Al Khayriyyah', 'qalyub', 'el khankah'],
        'qalyub': ['el khankah', 'shibin el qanatir', 'toukh', 'Al Qanatir Al Khayriyyah', 'Shubra Al Khaymah'],
        'shibin el qanatir': ['banha', 'toukh', 'qalyub', 'el khankah'],
        'el khankah': ['shibin el qanatir', 'qalyub', 'Shubra Al Khaymah'],
    }


    def BFS(data, startP, endP):
        # bsf code
        visited = {}
        level = {}
        parent = {}
        bfs_traversal_output = []
        queue = Queue()
        for node in data.keys():
            visited[node] = False
            parent[node] = None
            level[node] = -1
        s = startP
        visited[s] = True
        level[s] = 0
        queue.put(s)
        while not queue.empty():
            u = queue.get()
            bfs_traversal_output.append(u)
            # --------------------
            # i don't use this
            # by use it you get the breadth path that may be not the shortest path
            # if u==end : break
            # --------------------
            for v in adj_list[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    level[v] = level[u] + 1
                    queue.put(v)

        # ----------------------------
        # this add in my code
        # in this code i use parent list to get shortest path not breads first search path
        path = []
        while endP is not None:
            path.append(endP)
            endP = parent[endP]
        path.reverse()

        # ----------------------------
        # return(bfs_traversal_output)
        return path
    final_list = BFS(adj_list, startP, endP)
    #print(final_list)
elif ((Algo=="DFS") and (startP!=endP)):
#Deth first seaech
    adj_list = {
        'shebin': ['tala', 'el shohada', 'minuf', 'el-bagour', 'quwaysna', 'birket as sab'],
        'minuf': ['el shohada', 'shebin', 'el-bagour', 'ashmun', 'el sadat city'],
        'tala': ['birket as sab', 'shebin', 'el shohada', 'Kafr El-Zayat', 'tanta', 'As Santah'],
        'birket as sab': ['tala', 'shebin', 'quwaysna', 'As Santah', 'zefta'],
        'el-bagour': ['quwaysna', 'shebin', 'minuf', 'ashmun', 'banha', 'toukh', 'Al Qanatir Al Khayriyyah'],
        'ashmun': ['el-bagour', 'minuf', 'el sadat city', 'Al Qanatir Al Khayriyyah', 'toukh'],
        'quwaysna': ['birket as sab', 'shebin', 'el-bagour', 'zefta', 'kafr shokr', 'banha'],
        'el sadat city': ['ashmun', 'minuf'],
        'el shohada': ['tala', 'shebin', 'minuf'],
        'Kafr El-Zayat': ['basioun', 'tanta', 'tala'],
        'basioun': ['qutur', 'tanta', 'Kafr El-Zayat'],
        'qutur': ['basioun', 'tanta', 'El-Mahalla El-Kubra'],
        'El-Mahalla El-Kubra': ['qutur', 'tanta', 'As Santah', 'zefta', 'Samannoud'],
        'Samannoud': ['El-Mahalla El-Kubra', 'As Santah', 'zefta'],
        'zefta': ['Samannoud', 'El-Mahalla El-Kubra', 'As Santah', 'quwaysna', 'birket as sab', 'kafr shokr'],
        'As Santah': ['Samannoud', 'El-Mahalla El-Kubra', 'birket as sab', 'tanta'],
        'tanta': ['tala', 'Kafr El-Zayat', 'basioun', 'qutur', 'El-Mahalla El-Kubra', 'As Santah'],
        'kafr shokr': ['zefta', 'quwaysna', 'banha'],
        'banha': ['kafr shokr', 'quwaysna', 'el-bagour', 'toukh', 'shibin el qanatir'],
        'toukh': ['banha', 'el-bagour', 'ashmun', 'Al Qanatir Al Khayriyyah', 'qalyub', 'shibin el qanatir'],
        'Al Qanatir Al Khayriyyah': ['toukh', 'ashmun', 'Shubra Al Khaymah', 'qalyub'],
        'Shubra Al Khaymah': ['Al Qanatir Al Khayriyyah', 'qalyub', 'el khankah'],
        'qalyub': ['el khankah', 'shibin el qanatir', 'toukh', 'Al Qanatir Al Khayriyyah', 'Shubra Al Khaymah'],
        'shibin el qanatir': ['banha', 'toukh', 'qalyub', 'el khankah'],
        'el khankah': ['shibin el qanatir', 'qalyub', 'Shubra Al Khaymah'],
    }


    def DFS(data, startP, endP):
        color = {}
        value = ''
        parent = {}
        dfs_travers_out = []
        for node in data.keys():
            color[node] = 'w'
            parent[node] = None

        def loops(u):
            color[u] = 'g'
            dfs_travers_out.append(u)
            for v in data[u]:
                # if v==end : break
                if color[v] == 'w':
                    parent[v] = u
                    loops(v)
            color[u] = 'b'

        loops(startP)
        dfs_travers_out.append(endP)
        path = []
        # return dfs_travers_out

        # ----------------------------------
        # dfs_travers_out this is the path from start point to visite all point in graph
        # path list this is the list is slice from dfs_travers_out but not path for all point that is path from start point to end point
        for point in dfs_travers_out:
            # print(point)
            path.append(point);
            if point == endP:
                break
        # -----------------------------------
        return path


    final_list = DFS(adj_list, startP, endP)
    #print(final_list)
elif(startP!=endP):
#A* Algorithm
    if __name__ == '__main__':
        cities = {'shebin': {'tala': 18, 'el shohada': 16.5, 'minuf': 16.4, 'el-bagour': 14.6, 'quwaysna': 18.7,
                             'birket as sab': 14},
                  'minuf': {'el shohada': 18.2, 'shebin': 16.1, 'el-bagour': 11.4, 'ashmun': 27, 'el sadat city': 55.9},
                  'tala': {'birket as sab': 18.1, 'shebin': 18, 'el shohada': 14.4, 'Kafr El-Zayat': 25.6,
                           'tanta': 15.3, 'As Santah': 29.2},
                  'birket as sab': {'tala': 18.1, 'shebin': 14, 'quwaysna': 13.3, 'As Santah': 16, 'zefta': 24.5},
                  'el-bagour': {'quwaysna': 29.8, 'shebin': 14.9, 'minuf': 11.5, 'ashmun': 22.5, 'banha': 26.6,
                                'toukh': 39.7, 'Al Qanatir Al Khayriyyah': 30.8},
                  'ashmun': {'el-bagour': 23.8, 'minuf': 27.1, 'el sadat city': 61.7, 'Al Qanatir Al Khayriyyah': 23.5,
                             'toukh': 56.3},
                  'quwaysna': {'birket as sab': 13.9, 'shebin': 18.1, 'el-bagour': 18.1, 'zefta': 21.1,
                               'kafr shokr': 26.8, 'banha': 15.1},
                  'el sadat city': {'ashmun': 73.8, 'minuf': 54.5},
                  'el shohada': {'tala': 14.4, 'shebin': 17.5, 'minuf': 18.2},
                  'Kafr El-Zayat': {'basioun': 20.2, 'tanta': 27.6, 'tala': 25.6},
                  'basioun': {'qutur': 16.8, 'tanta': 28.8, 'Kafr El-Zayat': 20.2},
                  'qutur': {'basioun': 17.1, 'tanta': 16.3, 'El-Mahalla El-Kubra': 28.8},
                  'El-Mahalla El-Kubra': {'qutur': 30.8, 'tanta': 31.5, 'As Santah': 30.8, 'zefta': 33.3,
                                          'Samannoud': 7.7},
                  'Samannoud': {'El-Mahalla El-Kubra': 7.8, 'As Santah': 46.6, 'zefta': 33.1},
                  'zefta': {'Samannoud': 35, 'El-Mahalla El-Kubra': 32.7, 'As Santah': 17.9, 'quwaysna': 21.1,
                            'birket as sab': 25.3, 'kafr shokr': 27.9},
                  'As Santah': {'Samannoud': 48.7, 'El-Mahalla El-Kubra': 30.3, 'birket as sab': 16.2, 'tanta': 25.3},
                  'tanta': {'tala': 15, 'Kafr El-Zayat': 26.4, 'basioun': 28.3, 'qutur': 16,
                            'El-Mahalla El-Kubra': 29.2, 'As Santah': 25.9},
                  'kafr shokr': {'zefta': 32.7, 'quwaysna': 23.1, 'banha': 13.4},
                  'banha': {'kafr shokr': 17.7, 'quwaysna': 17.8, 'el-bagour': 29.4, 'toukh': 15.6,
                            'shibin el qanatir': 28.8},
                  'toukh': {'banha': 17.5, 'el-bagour': 40, 'ashmun': 57.5, 'Al Qanatir Al Khayriyyah': 25,
                            'qalyub': 22, 'shibin el qanatir': 14},
                  'Al Qanatir Al Khayriyyah': {'toukh': 24.7, 'ashmun': 23.5, 'Shubra Al Khaymah': 18.5, 'qalyub': 7.6},
                  'Shubra Al Khaymah': {'Al Qanatir Al Khayriyyah': 18.4, 'qalyub': 11.6, 'el khankah': 22.4},
                  'qalyub': {'el khankah': 26.9, 'shibin el qanatir': 20.6, 'toukh': 22.7,
                             'Al Qanatir Al Khayriyyah': 7.6, 'Shubra Al Khaymah': 12.1},
                  'shibin el qanatir': {'banha': 29.8, 'toukh': 14, 'qalyub': 20.4, 'el khankah': 17.6},
                  'el khankah': {'shibin el qanatir': 15.9, 'qalyub': 27.4, 'Shubra Al Khaymah': 24.4},
                  }


    def find_paths(startP, endP, cities, path, distance, visited=set()):
        #     pa = []
        visited.add(startP)  # keep track of visited nodes
        path.append(startP)

        #     count = 0 # avoid adding end paths twice
        for city in cities[startP].keys():  # only recurse on children not the whole list
            visited.add(city)
            path.append(city)
            if city == endP:
                break
            elif city not in visited:
                visited.add(city)
                path.append(city)
                find_paths(city, endP, cities, path, distance, visited)
        if endP not in visited:
            visited.add(endP)
            path.append(endP)


    final_list = []
    find_paths(startP, endP, cities, final_list, 0)
    #print(final_list)
    # ////////////
else:
    print("Start Can not Equal The End")
###############################################
#Real coordanitas
Coordinates = {
#el menofia
"shebin":[30.554928799816988, 31.012393143088957],
"minuf":[30.45841991481536, 30.933867041463532],
"tala":[30.683127111837056, 30.950034191578247],
"birket as sab": [30.627495984801378, 31.07244250380298],
"el-bagour":[30.43186671298956, 31.031983255977398],
"ashmun":[30.300117313578117, 30.97564036423758],
"quwaysna":[30.56765698894867, 31.149568418149613],
"el sadat city":[30.362811748009076, 30.533153025293895],
"el shohada": [30.59768043193886, 30.895758793318098],
#el gharbia
"Kafr El-Zayat":[30.828935887979828, 30.81468363315086],
"basioun":[30.941234859668185, 30.819787152459256],
"tanta":[30.78236661466976, 31.003931835360497],
"qutur":[30.97124133198592, 30.952896608684792],
"El-Mahalla El-Kubra":[30.969841036674914, 31.166019730570685],
"As Santah":[30.749281457375343, 31.129532111290036],
"Samannoud":[30.96202482138702, 31.241725792395766],
"zefta":[30.714483753839744, 31.240197668420624],
#el kalubia
"banha":[30.46954041758182, 31.18372798445176],
"qalyub":[30.180143566835696, 31.20638419614639],
"Al Qanatir Al Khayriyyah":[30.194609758641715, 31.13391214967144],
"Shubra Al Khaymah":[30.124142365522676, 31.260465002556664],
"el khankah":[30.22039965655326, 31.368612270866304],
"kafr shokr":[30.552839823187284, 31.255430468410704],
"shibin el qanatir":[30.31214792794175, 31.32292278281032],
"toukh":[30.353756127836252, 31.2014138527108]
}
###############################################
####################################################
lat = []
lang = []
#Get Lang and Lat
for v in final_list:
    lat.append(Coordinates[v][0])
    lang.append(Coordinates[v][1])

####################################################
#print(lat)
#print(lang)
if startP != endP:
    gmapOne = gmplot.GoogleMapPlotter( 30.637468, 30.914927, 8)
    gmapOne.scatter(lat, lang, size=50, color="red")
    fistLa=[]
    fistLng=[]
    endLa=[]
    endLng=[]
    fistLa.append(lat[0])
    fistLng.append(lang[0])
    endLa.append(lat[len(lat)-1])
    endLng.append(lang[len(lang)-1])
    gmapOne.scatter(fistLa, fistLng, size=50, color="green")
    gmapOne.scatter(endLa, endLng, size=50, color="purple")
    gmapOne.plot(lat, lang, 'blue',edge_width=2.5)
    gmapOne.draw("map.html")
