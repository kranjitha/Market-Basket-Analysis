import pickle
import operator
from collections import defaultdict
import itertools
import tqdm
baskets = []
unique_elements_one = []
freq_one = {}
freq_two = defaultdict(int)
freq_three=defaultdict(int)
confidence_abc=defaultdict(int)
frequency_one = {}
significant_one = defaultdict(int)
significant_two = defaultdict(int)
significant_three=defaultdict(int)
file=open("browsing.txt","r")
for line in file:
    baskets.append(line.split())
# for i in baskets:
#     for j in i:
#         if j not in unique_elements_one:
#             unique_elements_one.append(j)
# print(unique_elements_one)
# pickle.dump(unique_elements_one,open("unique_lst.p","wb"))
# with open('unique_lst.txt', 'w') as f:
#     for item in unique_elements_one:
#         f.write("%s\n" % item)
unique_elements_one = pickle.load(open("unique_lst.p","rb"))
for i in unique_elements_one:
    frequency_one[i] = 0
for items in baskets:
    for element in items:
        frequency_one[element]+=1
#pickle.dump(frequency_one,open("support_individual.p","wb"))
frequency_one=pickle.load(open("support_individual.p","rb"))
# with open("support_individual.txt",'w') as f:
#     for item in frequency_one:
#         f.write(item+" "+str(frequency_one[item]))
#         f.write("\n")

for items in frequency_one:
    if frequency_one[items]>100:
        significant_one[items]=frequency_one[items]
#
# for basket in baskets:
#     basket_subset = sorted([item for item in basket if item in significant_one])
#     pairs = itertools.combinations(basket_subset,2)
#
#
#     for item in pairs:
#         freq_two[item]+=1

# pairs = list(itertools.combinations(significant_one , 2))
# print(x)

#
# for line in baskets:
#     for i in x:
#         if i[0] in line and i[1] in line:
#             freq_two[i]+= 1
#             #print(freq_two)
#pickle.dump(freq_two,open("support_pair.p","wb"))

frequency_two=pickle.load(open("support_pair.p","rb"))
# with open("support_pair.txt" ,"w") as f:
#     for item in freq_two:
#         f.write(item[0])
#         f.write(" ")
#         f.write(item[1])
#         f.write("\t")
#         f.write(str(freq_two[item]))
#         f.write("\n")
for i in frequency_two:
    if frequency_two[i]>100:
        significant_two[i]=frequency_two[i]
confidence_ab=defaultdict(int)
confidence_ba=defaultdict(int)
# for i in significant_two:
#     temp=(i[1],i[0])
#     confidence_ab[i]= significant_two[i]/significant_one[i[0]]
#     confidence_ab[temp] = significant_two[i] / significant_one[i[1]]


#pickle.dump(confidence_ab,open("confidence_pair.p","wb"))
confidence_ab=pickle.load(open("confidence_pair.p","rb"))
sorted_dictionary = sorted(confidence_ab.items(), key=lambda x: -x[1])
# with open("confidence_pair.txt" ,"w") as f:
#     for item in sorted_dictionary:
#
#         f.write(item[0][0])
#         f.write(" ")
#         f.write(item[0][1])
#         f.write("\t")
#         f.write(str(item[1]))
#         f.write("\n")
sig_two=[]
for item in significant_two:
    x=item[0]
    y=item[1]
    if x not in sig_two:
        sig_two.append(x)
    if y not in sig_two:
        sig_two.append(y)
for basket in baskets:
    basket_subset = sorted([item for item in basket if item in sig_two])
    triplets = itertools.combinations(basket_subset,3)
    for items in triplets:
        freq_three[items]+=1
for i in freq_three:
    if freq_three[i]>100:
        significant_three[i]=freq_three[i]
# for i in significant_three:
#     temp1= (i[0],i[1],i[2])
#     temp2= (i[0], i[2], i[1])
#     temp3= (i[1], i[2], i[0])
#     confidence_abc[temp1]= significant_three[i] / significant_two[(i[0],i[1])]
#     confidence_abc[temp2]=significant_three[i]/significant_two[(i[0],i[2])]
#     confidence_abc[temp3]=significant_three[i]/significant_two[(i[1],i[2])]
# pickle.dump(confidence_abc,open("confidence_triplets.p","wb"))
confidence_abc=pickle.load(open("confidence_triplets.p","rb"))
confidence_abc_sorted= sorted(confidence_abc.items(), key=lambda x: -x[1])
print(confidence_abc_sorted)


# for line in baskets:
#     for i in x:
#         if i[0] in line and i[1] in line:
#             freq_two[i]+= 1
#             #print(freq_two)
# pickle.dump(freq_three,open("support_triplets.p","wb"))
# with open("support_triplets.txt" ,"w") as f:
#     for item in freq_three:
#         f.write(item[0])
#         f.write(" ")
#         f.write(item[1])
#         f.write(" ")
#         f.write(item[2])
#         f.write("\t")
#         f.write(str(freq_three[item]))
#         f.write("\n")

with open("confidence_triplets.txt" ,"w") as f:
    for item in confidence_abc_sorted:

        f.write(item[0][0])
        f.write(" ")
        f.write(item[0][1])
        f.write(" ")
        f.write(item[0][2])
        f.write("\t")
        f.write(str(item[1]))
        f.write("\n")