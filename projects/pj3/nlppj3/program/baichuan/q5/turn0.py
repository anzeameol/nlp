
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
──┐ └───---──┘ ──
９ ７ ┌──> ８ ┐
6  └┐  ┌─ ９┘
5  │  ├┐   4
4  ┘  ┤ ─┐──┤
３ ┘──┴┘─┘   1 ２
index ═  binary   search   function   ended ______  ________________
1. Write a function to check if a given number is an odd number or an even number. Use the modulo operator (%) to determine the parity of a number (0 for even, non-zero for odd). The function should accept an integer as input and return a string representing the number' s parities. For example, even_number(6) should return "even" and odd_numbe r(5) shou ld return  "odd". You can use the following code as a reference:def even _number (num): if num % ₂ ≠ ０: return 'even' else: retur n 'odd'
even_ number(4)  ⇒  'even’
odd_numb er(7)   ⇒   'odd