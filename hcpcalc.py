#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: hcpcalc.py
# A simple program to calculate your golf handicap
# Made for the Swedish handicap system!
#
# Author:   Daniel Haglund <daniel@asball.se>
# Version:  1.0.(20160801)

import sys


def main():

    # Main function

    if len(sys.argv) < 3:
        print ('Error! You must supply your current HCP and the points you recieved.\nUsage: {0} <current hcp> <accuired points>', sys.argv[0])
        return 1
    else:

        curr_hcp = float(sys.argv[1])
        played_points = int(sys.argv[2])

        if played_points > 36:
            lower_hcp(curr_hcp, played_points)
        elif played_points < 36:
            raise_hcp(curr_hcp, played_points)
        else:
            print ('You played on your exact HCP.\nNo adjustment needed...')


def lower_hcp(current, points):

    # Function to lower hcp
    # print("lower_hcp()")

    pt_counter = points - 36
    hcp = current

    while pt_counter > 0:
        if hcp >= 26.5:
            hcp = hcp - 0.5
        elif hcp >= 18.5:
            hcp = hcp - 0.4
        elif hcp >= 11.5:
            hcp = hcp - 0.3
        elif hcp >= 4.5:
            hcp = hcp - 0.2
        elif hcp < 4.4:
            hcp = hcp - 0.1

        pt_counter = pt_counter - 1

    print ('Lowering from hcp {0:.1f} with {1} points, resulted in hcp {2:.1f}'.format(current, points, hcp))


def raise_hcp(current, points):

    # Function to raise hcp
    # print("raise_hcp()")

    pt_counter = 36 - points
    hcp = current

    while pt_counter > 0:
        if hcp >= 26.5:
            hcp = hcp + 0.2
        else:
            hcp = hcp + 0.1

        pt_counter = pt_counter - 1

    print ('Raising from hcp {0:.1f} with {1} points, resulted in hcp {2:.1f}'.format(current, points, hcp))


if __name__ == '__main__':
    main()


