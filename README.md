# ENPM661
## Project 3 - Implementation of A Star and Djikstra Algoirthm
#### **Contributors :**
**Alkesh Kumar Srivastava**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Hari Krishna Prannoy Namala** <br />
UID -117451788&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;UID -117507409 <br />
_alkesh@umd.edu_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_pnamala@umd.edu_

Project 3 aimed at introducing the implementation of search algorithms in a *Mobile Robot*. To run this project you need to make sure that your system has the following libraries installed :
* numpy	1.20.1	
* opencv-python	4.5.1.48
* pygame	2.0.1


### Phase 1 :
In phase 1, we implemented A-star and Dijkstra algorithm with non-holonomic constraints. To run the program you need to access the `p3_phase1` folder. In this folder you will need to run the `__main__.py` file.
On running this file in the shell, you will be asked to input X Co-ordinate of the player, Y Co-ordinate of the player and the X and Y co-ordinate of its destination sequentially, as can be seen from the image below :
![Output](https://github.com/alkesh-umd/enpm661-p3/blob/main/uploads/Capture1.PNG)

*NOTE - Please Enter Integer Co-ordinates only.*

The next step will ask you to choose the desired method of path finding. You need to press :
1 for Dijkstra.
2 for A*
![Output](https://github.com/alkesh-umd/enpm661-p3/blob/main/uploads/Capture2.PNG)

As soon as you hit enter, the computer will process the input and will return a return path on the screen. If you see a list of co-ordinate points (as shown below), you have successfully found the path for your mobile robot taking care of 15 units of C-spacing.
![Output](https://github.com/alkesh-umd/enpm661-p3/blob/main/uploads/Capture3.PNG)


It will automatically save a video file in the root folder named `animation.avi`.
The example of the output of this program can be accessed by clicking the link :
<a href="https://drive.google.com/drive/folders/1UoAINFKPDdIG82chyeUXzRa0-S6AzK54?usp=sharing"> Phase 1 Examples - Google Drive Link</a>



### Phase 2 :
Phase 2 is a twisted implementation of A-star for our mobile robot. In phase 2, our robot can move only in 5 directions :

All these informations are requested by the user. Therefore, the robot that we will be building here is very user-friendly. To run this program you need to access the `p3_phase2` folder. In this folder you will only need the `__main__.py` file.
On running this file in the shell, you will be asked to input the co-ordinates of the mobile robot as (x,y, *theta*). Please enter every information as is asked by the program. You will be asked the following :
1. Starting Position and Orientation of the Robot.
2. Goal Position and Orientation of the Robot.
3. Radius of your Mobile Robot.
4. Desired clearance of the Mobile Robot
5. Desired step-size of the Mobile Robot.
6. OPTIONAL : Desired angle between consecutive moves.
![Output](https://github.com/alkesh-umd/enpm661-p3/blob/main/uploads/Capture4.PNG)

The step 6 is optional, if you will leave it as blank and hit Enter the program will assume the consecutive step will move by 30 degrees. As soon as you hit enter, the real-time display of the robot will be shown and on the terminal you will see what neighbors is our robot visiting. The purpose of printing the visited nodes is to make the user aware of the fact that our robot is taking threshold of certain distance from the goal position. This ensures that the robot has reached the destination and is covering the goal point instead of needlessly roaming around the maze in hope to have its geometric centre align with the goal point.

NOTE : You must also note that this program is not taking care of what is the orientation of the robot when it reaches the destination. Although, it can be a requirement in many applications and our program is designed to take care of this need (this is the reason why we are taking goal *theta*). You just need to do copy the commented code (as shown below) to the appropriate location in `a_star` definition present in `real_timeviz.py`:
`and current_cell[2] == goal[2] `

![Output](https://github.com/alkesh-umd/enpm661-p3/blob/main/uploads/Capture6.gif)


When the program ends, you will be able to see the video in the root folder. The examples of output of this program can be found at the link:
<a href="https://drive.google.com/drive/folders/1jz5VxoXAydE1zxKnoIQK9snieuANEJN3?usp=sharing"> Phase 2 Examples - Google Drive Link</a>







In case you encounter any difficulty please feel free to contact the creators - <br/>
***Alkesh K Srivastava*** - `{alkesh@umd.edu}`, University of Maryland, College Park <br/>
***Hari Krishna Prannoy Namala*** - `{pnamala@umd.edu}`, University of Maryland, College Park <br/>
