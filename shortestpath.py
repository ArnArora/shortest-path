##needed for sys.maxsize
import sys
##needed for permutations
from itertools import permutations
##make a list of lists with distances between points
##the (i,j) entry in the list is the distance between list[i] and list[j]
def distance(list, length):
    total_distances = []
    for i in range(length):
        sub_distances = []
        for j in range(length):
            ##Pythagorean Theorem
            dist = ((list[i][0]-list[j][0])**2+(list[i][1]-list[j][1])**2)**0.5
            sub_distances.append(dist)
        total_distances.append(sub_distances)
    return total_distances
##returns all permutations of a list that have the same start and end
def permutate(list):
    permutated_list = []
    ##all permutations
    permutated_item = permutations(list)
    for item in permutated_item:
        ##check that the start point and end point are the same as the original list
        if item[0]==list[0] and item[-1]==list[-1]:
            permutated_list.append(item)
    return permutated_list
def main(list):
    ##define the length of the list as n
    ##n is also the number of points in the coordinate plane
    n = len(list)
    ##largest integer
    best = sys.maxsize
    ##list of points leading to shortest path
    best_perm = []
    ##dictionary that will assign each coordinate a number
    new_dict = {}
    num = 0
    ##list of list of distances
    distance_list = distance(list, n)
    ##assign each coordinate a number
    for coor in list:
        new_dict[coor] = num
        num+=1
    ##for each permutation, check the distance between adjacent points
    for perm in permutate(list):
        sum = 0
        for i in range(n-1):
            ##get the coordinates of adjacent points
            coor1 = perm[i]
            coor2 = perm[i+1]
            ##add the distance to total distance
            sum+=distance_list[new_dict[coor1]][new_dict[coor2]]
        ##check if the permutation is the best one so far
        if sum<best:
            ##if so, replace best and best_perm with sum and perm respectively
            best = sum
            best_perm = perm
    return best_perm


            

    
    
    
    
    



    

