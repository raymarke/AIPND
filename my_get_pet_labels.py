import os
filename = 'pet_images'
dog_file_names = os.listdir(filename)
#dog name is 1-3 words with numbers at the end
full_dog_name = []
results_dic = {}
for all_names in dog_file_names:
    # split_names = all_names.lower().split("_", maxsplit=1)
    split_names = all_names.lower().rsplit('_', 1)[0]
    split_names = split_names.replace('_',' ')
    results_dic[all_names] = [split_names]
    #print('dog name is: {} and length is {}'.format(split_names, len(split_names)))
    print(results_dic)
# extricate the dog Name
# format the dog name (see above)
    #   results_dic - Dictionary with 'key' as image filename and 'value' as a 
    #   List. The list contains for following item: