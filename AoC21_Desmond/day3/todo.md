import binary data as .txt file

read txt file

for every column in the dataset, read it from top to bottom
    -> keep count of all 0's
    -> keep count of all 1's

    determine gamma rate as HIGHEST count of 12-part binary number:
        1st bit of gamma rate = most recurring bit of 1st row
        2nd bit of gamma rate = most recurring bit of 2nd row
        ....
        12th bit of gamma rate = most recurring bit of 12th row
    return gamma rate

    determine epsilon rate as LOWEST count of 12-part binary number:
        1st bit of epsilon rate = least recurring bit of 1st row
        2nd bit of epsilon rate = least recurring bit of 2nd row
        ....
        12th bit of gamma rate = least recurring bit of 12th row
    return epsilon rate


power consumption = gamma rate * epsilon rate