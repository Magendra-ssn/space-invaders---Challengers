# space-invaders---Challengers
Our team ( Adyant Srinivasan, Jameel Ahamed, Sailesh R, Magendra Kamalnath S A ) - Challengers's solution for the space invaders competition hosted by Indira Gandhi Delhi Technical University for Women (IGDTUW), Delhi

We will be doing a total of 3 checks to find the optimum path of the spaceship covering least distance to reach a destination and also avoiding obstacles.

Check 1 : 

Using the data of spherical coordinates of over 27000 obstacles taken from NASA database and Department of defenses's global space surveillance network (SSN) and with the spherical coordinates of the spaceship and the destination we find the path with least distance and will also ensure this path will not have obstacles ( considering obstales to be stationary ). This will be considered as the " reference trajectory "

Check 2 :

While travelling in the reference trajectory we will also be monitoring the radar in the spaceship. If a obstacle is going to collide, the radars used give a accurate value of the distance to collision ( usually before 1000 mm ) but the radars do not give accurate information about the size of the obstacle.

Check 3 :

To get the size of obstacle : The external tank cameras in the spaceship take pictures every 0.1 seconds and using OpenCV in python we split a image into several pieces and will compare it with existing images of obstacles in various databases ( both private and public ) and using numpy we find the size of the obstacle. This is also another check to ensure no obstacle crosses paths with the spaceship. Moreover if a obstacle like a private spaceship not listed in our list of obstacles is going to cross paths with our spaceship Check 2 and Check 3 will ensure to avoid it.

Action : Once we know the distance to collision and size of the obstacle - Let the distance to collsion be 'a' and size of obstacle be 'b' . The spaceship will deviate from the reference trajectory at a distance of 2*a from the obstacle and deviate by a distance of 2*b mm from the obstacle. We locate all possible coordinates the spaceship can deviate to and check 1 is done with all possible new spherical coordinates of the spaceship to find the trajectory with least obstacles and so the direction of deviation of spaceship is determined and that trajectory is followed to deviate.

This way the spaceship covers least distance to the destination and also has no chance of collision with any form of space debris. 

Note : This project needs real time data and will work in real-world scenarios.
