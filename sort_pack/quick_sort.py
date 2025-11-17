def quick_sort(array):
    
    if len(array) < 2:
        return array

    def separation(array):
        runner = array[-1]
        result = 0
        for i in range(len(array) - 1):
            if array[i] < runner:
                array[i], array[result] = array[result], array[i]
                result += 1
                
        array[-1], array[result] = array[result], array[-1]
        return array, result

    array, runner = separation(array)
    array[:runner] = quick_sort(array[:runner])
    array[runner + 1:] = quick_sort(array[runner + 1:])
    
    return array
