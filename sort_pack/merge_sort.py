def merge_sort(array):
    
    def merge(left, right):
        result = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left(i) < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])

        return result
    
    if len(array) < 2:
        return array

    center = len(array) // 2
    left = merge_sort(array[0:center])
    right = merge_sort(array[center:])

    return merge(left, right)