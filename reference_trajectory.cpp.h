//
//  spaceship.h
//  class1
//
//  Created by Adyant Srinivasan on 06/11/21.
//

#ifndef spaceship_h
#define spaceship_h
#include <math.h>
#include <cmath.h>
class ship{
    double coordinates[3];
    double fcoordinates[3];
public:
    double* rtncoordinates(){
        return coordinates;
    }
    double rtndis(double* objcoordinates){
        return pow(pow(coordinates[0],2)+pow(objcoordinates[0],2)-(2*coordinates[0]*objcoordinates[0]*(sin(coordinates[1])*sin(objcoordinates[1])*cos(coordinates[2]-objcoordinates[2])+cos(coordinates[1])*cos(objcoordinates[1]))),0.5)
    }
    bool chklie(double* objcoordinates){
        double x1=fcoordinates[0]*sin(fcoordinates[2])*cos(fcoordinates[1]), y1=fcoordinates[0]*sin(fcoordinates[2])*sin(fcoordinates[1]), z1=fcoordinates[0]*cos(fcoordinates[2]), x2=coordinates[0]*sin(coordinates[2])*cos(coordinates[1]), y2=coordinates[0]*sin(coordinates[2])*sin(coordinates[1]), z2=coordinates[0]*cos(coordinates[2]), x=objcoordinates[0]*sin(objcoordinates[2])*cos(objcoordinates[1]), y=objcoordinates[0]*sin(objcoordinates[2])*sin(objcoordinates[1]), z=objcoordinates[0]*cos(objcoordinates[2]);
        if((x-x1)/(x1-x2)==(y-y1)/(y1-y2)&&(x-x1)/(x1-x2)==(z-z1)/(z1-z2))
            return true;
        return false;
    }
};

#endif /* spaceship_h */
