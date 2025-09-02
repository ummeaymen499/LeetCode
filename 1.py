def alternative_array(string1, string2):
    merged_string=""
    i,j=0,0
    while i< len(string1) or j< len(string2):
        if i<len(string1):
            merged_string=merged_string+string1[i]
            i=i+1
        if j<len(string2):
            merged_string=merged_string+string2[j]
            j=j+1

    return merged_string

result=alternative_array("abc", "123")
print(result)