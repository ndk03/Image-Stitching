import random

import math

def solution(input_points, t, d, k):

    """

    :param input_points:

           t: t is the perpendicular distance threshold from a point to a line

           d: d is the number of nearby points required to assert a model fits well, you may not need this parameter

           k: k is the number of iteration times

           Note that, n for line should be 2

           (more information can be found on the page 90 of slides "Image Features and Matching")

    :return: inliers_name, outliers_name

    inliers_name and outliers_name is two list, each element of them is str type.

    For example: If 'a','b' is inliers and 'c' is outlier_point.

    the output should be two lists of ['a', 'b'], ['c'].

    Note that, these two lists should be non-empty.

    """

    nc2 = math.factorial(len(input_points)) / (math.factorial(len(input_points) - 2) * math.factorial(2))

    chosen_points = []

    inliers_total = []

    outliers_total = []

    best_err = float("inf")

    for i in range(k):

        inliers = []

        outliers = []

        if(len(chosen_points) == nc2):

            break

        while(True):

            p1 = random.randint(0, 7)

            p2 = random.randint(0, 7)

            if ((p1 != p2) and not((p1, p2) in chosen_points) and not((p2, p1) in chosen_points)):

                chosen_points.append((p1, p2))

                break        

        inliers.append(input_points[p1]['name'])

        inliers.append(input_points[p2]['name'])

        m = (input_points[p2]['value'][1] - input_points[p1]['value'][1]) / (input_points[p2]['value'][0] - input_points[p1]['value'][0] + 0.0000001)

        c = input_points[p2]['value'][1] - m * input_points[p2]['value'][0]

        err = 0 

        for pt in [pt for pt in input_points if (pt != input_points[p1] and pt != input_points[p2])] :

            dist = abs(-m * pt['value'][0] + pt['value'][1] - c) / (m**2 + 1)**0.5

            if (dist <= t):

                inliers.append(pt['name'])

                err += dist

            else:

                outliers.append(pt['name'])

        if(len(inliers) > d):

            if(err < best_err):

                inliers_total.clear()

                outliers_total.clear()

                inliers_total = inliers

                outliers_total = outliers

                best_err = err

    # print('Inliers :', inliers_total)

    # print('Outliers :', outliers_total)

    return(inliers_total, outliers_total)

       



if __name__ == "__main__":

    input_points = [{'name': 'a', 'value': (0.0, 1.0)}, {'name': 'b', 'value': (2.0, 1.0)},

                    {'name': 'c', 'value': (3.0, 1.0)}, {'name': 'd', 'value': (0.0, 3.0)},

                    {'name': 'e', 'value': (1.0, 2.0)}, {'name': 'f', 'value': (1.5, 1.5)},

                    {'name': 'g', 'value': (1.0, 1.0)}, {'name': 'h', 'value': (1.5, 2.0)}]

    t = 0.5

    d = 3

    k = 100

    inliers_name, outliers_name = solution(input_points, t, d, k)  # TODO

    assert len(inliers_name) + len(outliers_name) == 8  

    f = open('./results/task1_result.txt', 'w')

    f.write('inlier points: ')

    for inliers in inliers_name:

        f.write(inliers + ',')

    f.write('\n')

    f.write('outlier points: ')

    for outliers in outliers_name:

        f.write(outliers + ',')

    f.close()





