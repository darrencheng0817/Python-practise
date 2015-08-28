#Design and implement a hash table using chaining (linked list) to handle all the collsions

hash_map ={}

def insertion(key, value):
    if key not in hash_map:
        hash_map[key] = [value]
    else:
        hash_map[key] = hash_map[key] + [value]

def main():
    insertion(1, "hehe")
    insertion(2, "haha")
    insertion(1, "xixi")
    print hash_map
   
if __name__ == "__main__":
    main()
    
    
    