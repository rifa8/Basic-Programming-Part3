def full_prima(N):
    # your code here
    bbpsd = [0,1,4,6,8,9] #bilangan bukan prima satu digit
    if N < 0:
        return False
    for i in range(2, N):
        if N % i == 0:
            return False
    
    #mengecek setiap digit pada bilangan(N) apakah ada bilangan bukan prima...
    #...dengan menggunakan bantuan list 'bbpsd'
    #'cek_digit' akan menyimpan data berupa True atau False
    cek_digit = any(digit in str(N) for digit in str(bbpsd)) 
    if cek_digit == True:
        return False    #false karena ada digit yang bukan prima pada bilangan(N)
    return True

if __name__ == '__main__':
    print(full_prima(2)) # True
    print(full_prima(3)) # True
    print(full_prima(11)) # False
    print(full_prima(13)) # False
    print(full_prima(23)) # True
    print(full_prima(29)) # False
    print(full_prima(37)) # True
    print(full_prima(41)) # False
    print(full_prima(43)) # False
    print(full_prima(53)) # True
