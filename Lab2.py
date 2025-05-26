
def display_main_menu() : 
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input() : 
    num_in = input()
    numList = num_in.split(",")
    n_list = []
    for num in numList: 
        n_list.append(float(num))
    return n_list


def calc_average(numList) :
    total = 0
    avg = 0  
    for num in numList: 
        total += num
    
    avg = total / len(numList)

    return avg
def find_min_max(numList) : 
    max_n = max(numList)
    min_n = min(numList)
    return ([min_n, max_n])

#def sort_temperature() :

#def calc_median_temperature() : 

def main() : 
    display_main_menu()
    numList = get_user_input() 
    print("Average : ", calc_average(numList))
    print("Minimum and Maximum value : ", find_min_max(numList))

if __name__ == "__main__" : 
    main()