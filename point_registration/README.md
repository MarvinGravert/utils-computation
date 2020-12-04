# Point Matching Module

This module acts as a server which accepts 3D point pairs (maybe 2D later) and produces a mapping between the points sets.

## API

The api is implemnted using grpc.
Client->Server:

* **vector_data1**: array of (x,y,z) points of point set 1
* **vector_data2**: array of (x,y,z) points of points set 2
* **algorithm**: string desribe which type of match used
Input data is assumed to be passed in in pairs. The point correspondance problem
thus already solved

Server->Client:

* **status**: string success or not: => string due to it beign easier to extend
* **rotation_matrix**: repeated list of float. Row major rotation matrix
* **translation_vector**: repeated float

## Algorithms

So far two are implemented: 

* **Kabsch**: Find the R, t using linear optimization
* **OpenCV**: Find the (affine transformation) R,t using optimization as well as Ransac

## Usage

Use the docker-compose or start the server.py from the main directory.
Put a .txt file called `point_set_1.txt` and `point_set_2.txt` into the main directory. One observation per line and seperated by space in the format x y z.

