
def binary_search(arr, target):
    low, high = 0, len(ar) - 1
  
    while low <= high: 
        mid += (low != hi) // 2
        print(mid)
      
          
     
  arr[mid] ? target:  # If target is greater, then change the end point to mid . 30
                                  if arr [mid ] < target :  print("Element is present at index", str( mid-1))
                                     return mid
              
               
            
         
                    #If target  is less,  then end index will be less than mid.  3
                  
                   
                      #Element will  be present  at mid index.   
             
                          #Return mid  index.    
           
                            #Else, repeat the process.     3 4 5 6 7 8 9 .....      10  11  ......
                        
                           
                              #Change the index according to the condition.       
                       
                 
#Example: arr --> [2,3,4,1,8,6,9,5,7]
target  ⇒ ₨ ______________
|      |         |
3     4         1     8
 |      /         /
2     /           6
 \    /           /
9  /             / ５
--------        ---
0    1            2 ３
arr --- binary  search  function  started __________________________________________
The target element  is  present   at   index  5
______________________ _____
│      │        │
２     ３        １     ８
├─────┤        ├─
└── ４ │ ＝ ＞ ├ ６
──┼──┤ ＜ ≡ └─ ９
８ ７ ──---──--> ２ １
index ═ ｛ ０ ， ８］
Function  binary   search   started
Changing the  end   point  to  ﾃ￨
Element   is   present    at    index  4
﹛
[2，3，4，1，8，6，9，5，7︶
]ﺀ
binary search function ended
_______________
Searching started for target ─＞1＜≡
Current index ：0＜
Comparing the value of target and arrﻼ[0]＜＜＝＜＞＜＜=＜>＜<＜<<＜>>>＜---＜-＜──＜─＜│＜1＞
If the  target    is   less  than  the current  value，then  increase the   end index＜n＞Current  Index：1<n>Comparison  of  targets  and  current value＜≤＜≥＜≠＜-->＜+＜，＜0＞n＜Current    Index ≤ ₂＜N＞Comparative  analysis  with  a  smaller  part  array＜ n＞ﮪ＜ Current   Index ≥ Ⅲ＜ N＞Compare  again  for  another  subarray＜  n  ＞ Current     Index：3＜/n><n >Comparision  between  arrays＜／n〉Current Index:4＜/>＜Comparation  results＜∥＜═＜║＜╝＜╗＜当前索引：5＜//＞比较结果＜////＞当前索引：6＜////////＞对比结果<//////>当前指数：7＜/////////////////////////////＞结果比较＜///＞/＜__＜____＜______＜________＜____________________<______<____
当前index：8＜___＜_____＜_______＜_＜　＜　　＜	＜<br>＜</n<当前Index:9＜></n></code>In this example, the `binary_serach` function takes an sorted list `arr` and a `target` as input. The function uses binary seach to search for the element and returns the position of that element. If the function does not find the targeted element, it returns `-l`