def items_after_four(iter: list) -> int:
   
    if len(iter) <= 4:
        return 0
    else:
        return len(iter) - 4

if __name__ == "__main__":
    
    print(items_after_four([1, 2, 3, 4]))       
    print(items_after_four([1, 2, 3, 4, 5, 6]))  
    print(items_after_four(['a', 'b', 'c', 'd', 'e', 'f', 'g']))  
