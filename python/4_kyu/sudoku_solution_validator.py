import numpy

def validSolution(board):
    np_list = numpy.array(board)
    
    np_horizontal_sudoku_0 = numpy.array(np_list[0,:])
    np_horizontal_sudoku_1 = numpy.array(np_list[1,:])
    np_horizontal_sudoku_2 = numpy.array(np_list[2,:])
    np_horizontal_sudoku_3 = numpy.array(np_list[3,:])
    np_horizontal_sudoku_4 = numpy.array(np_list[4,:])
    np_horizontal_sudoku_5 = numpy.array(np_list[5,:])
    np_horizontal_sudoku_6 = numpy.array(np_list[6,:])
    np_horizontal_sudoku_7 = numpy.array(np_list[7,:])
    np_horizontal_sudoku_8 = numpy.array(np_list[8,:])

    np_horizontal_sudoku_0 = numpy.sort(np_horizontal_sudoku_0)
    np_horizontal_sudoku_1 = numpy.sort(np_horizontal_sudoku_1)
    np_horizontal_sudoku_2 = numpy.sort(np_horizontal_sudoku_2)
    np_horizontal_sudoku_3 = numpy.sort(np_horizontal_sudoku_3)
    np_horizontal_sudoku_4 = numpy.sort(np_horizontal_sudoku_4)
    np_horizontal_sudoku_5 = numpy.sort(np_horizontal_sudoku_5)
    np_horizontal_sudoku_6 = numpy.sort(np_horizontal_sudoku_6)
    np_horizontal_sudoku_7 = numpy.sort(np_horizontal_sudoku_7)
    np_horizontal_sudoku_8 = numpy.sort(np_horizontal_sudoku_8)
    
    np_vertical_sudoku_0 = numpy.array(np_list[:,0])
    np_vertical_sudoku_1 = numpy.array(np_list[:,1])
    np_vertical_sudoku_2 = numpy.array(np_list[:,2])
    np_vertical_sudoku_3 = numpy.array(np_list[:,3])
    np_vertical_sudoku_4 = numpy.array(np_list[:,4])
    np_vertical_sudoku_5 = numpy.array(np_list[:,5])
    np_vertical_sudoku_6 = numpy.array(np_list[:,6])
    np_vertical_sudoku_7 = numpy.array(np_list[:,7])
    np_vertical_sudoku_8 = numpy.array(np_list[:,8])

    np_vertical_sudoku_0 = numpy.sort(np_vertical_sudoku_0)
    np_vertical_sudoku_1 = numpy.sort(np_vertical_sudoku_1)
    np_vertical_sudoku_2 = numpy.sort(np_vertical_sudoku_2)
    np_vertical_sudoku_3 = numpy.sort(np_vertical_sudoku_3)
    np_vertical_sudoku_4 = numpy.sort(np_vertical_sudoku_4)
    np_vertical_sudoku_5 = numpy.sort(np_vertical_sudoku_5)
    np_vertical_sudoku_6 = numpy.sort(np_vertical_sudoku_6)
    np_vertical_sudoku_7 = numpy.sort(np_vertical_sudoku_7)
    np_vertical_sudoku_8 = numpy.sort(np_vertical_sudoku_8)
    
    np_three_by_three_0 = numpy.array(np_list[0:3,0:3])
    np_three_by_three_1 = numpy.array(np_list[0:3,3:6])
    np_three_by_three_2 = numpy.array(np_list[0:3,6:9])

    np_three_by_three_0 = np_three_by_three_0.flatten()
    np_three_by_three_1 = np_three_by_three_1.flatten()
    np_three_by_three_2 = np_three_by_three_2.flatten()

    np_three_by_three_0 = numpy.sort(np_three_by_three_0)
    np_three_by_three_1 = numpy.sort(np_three_by_three_1)
    np_three_by_three_2 = numpy.sort(np_three_by_three_2)

    np_three_by_three_3 = numpy.array(np_list[3:6,0:3])
    np_three_by_three_4 = numpy.array(np_list[3:6,3:6])
    np_three_by_three_5 = numpy.array(np_list[3:6,6:9])

    np_three_by_three_3 = np_three_by_three_3.flatten()
    np_three_by_three_4 = np_three_by_three_4.flatten()
    np_three_by_three_5 = np_three_by_three_5.flatten()

    np_three_by_three_3 = numpy.sort(np_three_by_three_3)
    np_three_by_three_4 = numpy.sort(np_three_by_three_4)
    np_three_by_three_5 = numpy.sort(np_three_by_three_5)

    np_three_by_three_6 = numpy.array(np_list[6:9,0:3])
    np_three_by_three_7 = numpy.array(np_list[6:9,3:6])
    np_three_by_three_8 = numpy.array(np_list[6:9,6:9])

    np_three_by_three_6 = np_three_by_three_6.flatten()
    np_three_by_three_7 = np_three_by_three_7.flatten()
    np_three_by_three_8 = np_three_by_three_8.flatten()

    np_three_by_three_6 = numpy.sort(np_three_by_three_6)
    np_three_by_three_7 = numpy.sort(np_three_by_three_7)
    np_three_by_three_8 = numpy.sort(np_three_by_three_8)
    
    check_list = [1,2,3,4,5,6,7,8,9]
    np_check_list = numpy.array(check_list)

    if numpy.array_equal(np_check_list, np_horizontal_sudoku_0) == True and \
       numpy.array_equal(np_check_list, np_horizontal_sudoku_1) == True and \
       numpy.array_equal(np_check_list, np_horizontal_sudoku_2) == True and \
       numpy.array_equal(np_check_list, np_horizontal_sudoku_3) == True and \
       numpy.array_equal(np_check_list, np_horizontal_sudoku_4) == True and \
       numpy.array_equal(np_check_list, np_horizontal_sudoku_5) == True and \
       numpy.array_equal(np_check_list, np_horizontal_sudoku_6) == True and \
       numpy.array_equal(np_check_list, np_horizontal_sudoku_7) == True and \
       numpy.array_equal(np_check_list, np_horizontal_sudoku_8) == True and \
       numpy.array_equal(np_check_list, np_vertical_sudoku_0) == True and \
       numpy.array_equal(np_check_list, np_vertical_sudoku_1) == True and \
       numpy.array_equal(np_check_list, np_vertical_sudoku_2) == True and \
       numpy.array_equal(np_check_list, np_vertical_sudoku_3) == True and \
       numpy.array_equal(np_check_list, np_vertical_sudoku_4) == True and \
       numpy.array_equal(np_check_list, np_vertical_sudoku_5) == True and \
       numpy.array_equal(np_check_list, np_vertical_sudoku_6) == True and \
       numpy.array_equal(np_check_list, np_vertical_sudoku_7) == True and \
       numpy.array_equal(np_check_list, np_vertical_sudoku_8) == True and \
       numpy.array_equal(np_check_list, np_three_by_three_0) == True and \
       numpy.array_equal(np_check_list, np_three_by_three_1) == True and \
       numpy.array_equal(np_check_list, np_three_by_three_2) == True and \
       numpy.array_equal(np_check_list, np_three_by_three_3) == True and \
       numpy.array_equal(np_check_list, np_three_by_three_4) == True and \
       numpy.array_equal(np_check_list, np_three_by_three_5) == True and \
       numpy.array_equal(np_check_list, np_three_by_three_6) == True and \
       numpy.array_equal(np_check_list, np_three_by_three_7) == True and \
       numpy.array_equal(np_check_list, np_three_by_three_8) == True:
        return True
    else:
        return False