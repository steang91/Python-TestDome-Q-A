def unique_names(names1, names2):
    new_menu=names1+names2
    print(new_menu)
    final_new_menu = list(set(new_menu))
    return final_new_menu


if __name__ == "__main__":
    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]
    print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia