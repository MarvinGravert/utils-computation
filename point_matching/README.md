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
* **hom_matrix**: repeated list. Row major homogenous matrix  

## Usage

Use the docker-compose or start the server.py from the main directory.
