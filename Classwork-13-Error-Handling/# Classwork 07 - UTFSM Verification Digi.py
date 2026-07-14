# Classwork 07 - UTFSM Verification Digit

# INPUT - Ask user for the UTFSM student ID (without dash or check digit)
try:
    student_id = input("Enter the UTFSM student ID (without dash or check digit): ")

    if len(student_id) == 0:
        raise ValueError("Input cannot be empty.")

    # PROCESS - Reverse the ID and calculate verification digit using UTFSM algorithm
    reversed_id = student_id[::-1]
    multiplier_pattern = [2, 3, 4, 5, 6, 7]
    total_sum = 0

    for position, number in enumerate(reversed_id):
        current_multiplier = multiplier_pattern[position % len(multiplier_pattern)]
        total_sum += int(number) * current_multiplier

    remainder = total_sum % 11
    verification_digit = 11 - remainder

    # OUTPUT - Print full calculation breakdown and result
    print(f"\nReversed ID:   {reversed_id}")
    print(f"Total sum:     {total_sum}")
    print(f"Sum % 11:      {remainder}")
    print(f"11 - {remainder}:        {verification_digit}")
    print(f"\nFull ID: {student_id}-{verification_digit}")

except ValueError as error:
    print(f"Error: {error} - The student ID must contain only numeric characters.")