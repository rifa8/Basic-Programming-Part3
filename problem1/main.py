# input
student_score = 80

# Process: Your Solution Code Here
def konversi_nilai(student_score):
    if 80 <= student_score <= 100:
        return 'Nilai A'
    elif 65 <= student_score <= 79:
        return 'Nilai B+'
    elif 50 <= student_score <= 64:
        return 'Nilai B'
    elif 35 <= student_score <= 49:
        return 'Nilai C'
    elif 0 <= student_score <= 34:
        return 'Nilai D'
    return 'Nilai E'

# Output "Nilai A"
nilai = konversi_nilai(student_score)
print(nilai)
