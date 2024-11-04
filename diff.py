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


def max_difference_with_buckets(sequence):
    n = len(sequence)
    
    if n < 2:
        return 0
    
    global_min, global_max = min(sequence), max(sequence)
    
    if global_min == global_max:
        return 0
  
    bucket_size = (global_max - global_min) / (n - 1)
    buckets = [{'min': None, 'max': None} for _ in range(n)]
    
    for num in sequence:
        index = int((num - global_min) / bucket_size)
        
        if buckets[index]['min'] is None or num < buckets[index]['min']:
            buckets[index]['min'] = num
        if buckets[index]['max'] is None or num > buckets[index]['max']:
            buckets[index]['max'] = num
    
    max_diff = 0
    previous_max = None
    
    for bucket in buckets:
        if bucket['min'] is None:
            continue
        
        if previous_max is not None:
            max_diff = max(max_diff, abs(abs(bucket['min']) - abs(previous_max))) 
        
        previous_max = bucket['max']
    
    return max_diff


sequence = [2, 5.3, 2.7, -20.1, 50]
result = max_difference_with_buckets(sequence)
print("Maximum difference:", result)


sequence = [2, 5.3, 2.7, -20.1, 50]
result = max_difference_with_no_intermediates(sequence)
print("Maximum difference:", result)
