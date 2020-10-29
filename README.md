# GMAPS--Graph-Expansion-Contraction
The Project encounters the idea of Graph Expansion and Contraction used in Google Maps and Design software's like AutoCad.

 
Project Report 
GRAPH EXPANSION AND CONTRACTION
DAA | CST352 | 17.10.2020 
Project Report on

“Graph Expansion & Contraction”

Submitted by:
A-40 Atharva Sawarkar
A-52 Kunal Khandelwal
A-86 Yash Telkhade

Under the guidance of:
Dr. Manoj Chandak
HOD, Department of Computer Science

17th October 2020

                               
Dept. of Computer Science & Engineering
                              
Project Description

Problem Statement: 
With the help of created zoomin() and zoomout() functions, display all the points that lie in the path of the source and the destination.
Display the map on the right side of the screen and the Data Structures on the left side of the screen.

Basic Documentation Idea: 

A map consists of layers, where every layer has a specific zoom level. These layers are placed on upon the other. Whenever a map is zoomed in or zoomed out the layer displayed is changed accordingly.
It uses the concept of 3D Matrix which integrates the locations inside the graph depending upon the value of Z (zoom level).
 
 
Our Logic & Implementation:
We have created a node consisting of 3 attributes. 
•	Name of Place (String)
•	Location of Place - Latitudes & Longitudes (int, int)
•	Pointer (int)
 
The Two main functions of the code – 
1.	ZoomIn() – It increments the node pointer of the locations to 1, to print the locations present in between.

2.	ZoomOut() – It decrements the node pointer with value 1 to 0, to make the Zoom out feature of the graph work


Working:
•	Whenever the “+” button is clicked, the Zoomin() function is called, which increases the number of locations displayed on the map, simultaneously the Data Structures tab is updated.

•	Whenever the “-” button is clicked, the Zoomout() function is called, which decreases the number of locations displayed on the map, simultaneously the Data Structures tab is updated. 

All the points which are visible on the map are printed on the left side of the screen.
 


Other Practical Applications of GE&C
•	Computer Aided Design software’s like AutoCAD
•	Solid Face
•	Sketch Art

Video Link –
https://drive.google.com/file/d/1_wJPoYGAupIKQ-2hvjq-zTM1_4yj_jJx/view?usp=sharing

