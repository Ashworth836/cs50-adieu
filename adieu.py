import inflect

p = inflect.engine()

def main():
    names = []
    
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            print("\n")
            break
        
    num_names = len(names)
    msg = "Adieu, adieu, to "
    
    if num_names == 1:
        msg + names[0]
    else:
        if num_names == 2:
            msg += f"{names[0]} and {names[1]}"
        else:
            msg += ", ".join(names[:-1])
            msg += ", and " + names[-1]
    
    print(msg)
    
    

if __name__ == "__main__":
    main()
    
    