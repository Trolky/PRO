def max_difference_with_no_intermediates(sequence):
    max_diff = 0
    
    # Loop through each pair of elements in the sequence
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            a, b = sequence[i], sequence[j]
            diff = abs(abs(a)-abs(b))
          
            min_val, max_val = min(a, b), max(a, b)
            
            intermediate_exists = any(min_val < sequence[k] < max_val for k in range(len(sequence)) if k != i and k != j)
            
        
            if not intermediate_exists and diff > max_diff:
                max_diff = diff
    
    return max_diff

sequence = [2, 5.3, 2.7, -20.1, 50]
result = max_difference_with_no_intermediates(sequence)
print("Maximum difference with no intermediates:", result)
