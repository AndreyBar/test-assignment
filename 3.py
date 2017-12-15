# Function that takes a list of tuples as a parameter
# and returns sorted list by name / age / height / weight
# everything is ascending
def list_sort(lst):
    return sorted(lst, key=lambda x: (x[0], x[1], x[2], x[3]))

# Same function but it sorts by 
# name (ascending) / age (ascending) / height (descending) / weight (ascending)
def advanced_list_sort(lst):
    sorted_list = sorted(lst, key=lambda x: x[3])       # Sorting by weight (asc)
    sorted_list.sort(key=lambda x: x[2], reverse=True)  # Sorting by height (desc)
    sorted_list.sort(key=lambda x: x[1])                # Sorting by age (asc)
    sorted_list.sort(key=lambda x: x[0])                # Final sort by primary key name
    return sorted_list


if __name__ == '__main__':
    lst =  [
            ("Tom", "19", "167", "54"), 
            ("Jony", "23", "180", "69"),
            ("Json", "21", "185", "75"),
            ("John", "27", "190", "87"), 
            ("Jony", "24", "191", "98") 
            ]
    list_sort(lst)
    advanced_list_sort(lst)