def bin_to_dec(binarni_cislo):
    
    bin_str = str(binarni_cislo)
    
    desitkova_hodnota = 0
    delka = len(bin_str)
 
    for i in range(delka):
      
        bit = bin_str[i]
       
        if bit == '1':
            exponent = delka - 1 - i
            desitkova_hodnota += 2 ** exponent
            
    return desitkova_hodnota

def test_bin_to_dec():
    
    print("Spouštění testů pro bin_to_dec...")
    
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21  
    assert bin_to_dec(10000000) == 128
    assert bin_to_dec("10011101") == 157
    assert bin_to_dec(111) == 7
    assert bin_to_dec("11111111") == 255
    
    print("Všechny testy proběhly úspěšně!")

if __name__ == "__main__":
    test_bin_to_dec()

    binarni_cislo = "10011101"
    vysledek = bin_to_dec(binarni_cislo)
    print(f"\nBinární číslo {binarni_cislo} je v desítkové soustavě: {vysledek}") 