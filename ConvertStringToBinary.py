def convert_str_to_bin(string):
        
        binary="".join(format(ord(ch),"b") for ch in string)
        print("Your String Is :\n{}".format(string)) 
        print("Binary Of {} Is :\n{}".format(string,binary))
convert_str_to_bin("ayoub")