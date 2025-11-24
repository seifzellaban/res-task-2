def get_grades():
    """
    Asks the user to input grades one by one and returns a list of those grades.
    """
    # TODO: Initialize an empty list to store the grades
    grades = []

    while True:
        # TODO: Take input from the user
        grade = input("Enter grades (type 'done' or '-1' to finish): ")

        # TODO: Check if the user wants to stop
        # Check if the input is 'done' or '-1'. If so, break the loop.
        if grade == "-1" or grade == "done":
            break

        # TODO: Convert the input to a number (integer or float)
        float_grade = float(grade)

        # TODO: Add the number to your grades list
        grades.append(float_grade)

    # TODO: Return the populated list of grades
    # This is crucial so the other function can use this data.
    return grades


def analyze_grades(sl):
    """
    Analyzes a list of scores to find the average,
    number of passing grades, and number of failing grades.
    """
    # TODO: Check if the list is empty before proceeding
    # (To avoid dividing by zero later!)
    if sl.isEmpty():
        return []

    # TODO: Initialize variables (sum, pass_count, fail_count)
    sum = 0
    pass_count = 0
    fail_count = 0

    # TODO: Loop through sl and calculate stats
    for score in sl:
        sum = sum + score
        if score >= 60:
            pass_count += 1
        else:
            fail_count += 1

    # TODO: Calculate Average and Print results
    avg = sum / len(sl)


# --- Main Execution ---

# TODO: Call the get_grades function and store the result in a variable

# TODO: Call the analyze_grades function passing the list you just created
