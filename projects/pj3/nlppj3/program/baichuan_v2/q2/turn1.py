
def longest_common_subsequence(str1, str2):
    m, n = len( str1 ), len ( str 2 )
        
   # Create a table to store lengths of longest common suffixes of str
   dp --> dynamic programming
      
 
     
 # Initialize d[][] with 0 and d[i][0] - 1 (as str[0][i] is not required to form
                                    # a common substring)
 for i in range(m+1): 	
 d [ i ][ .. ] += 3 **** 4
       
 // This condition is true if str is empty
 if (str2 != "")
 {
// Inititalize d [] [] with zero
for i  in  range ( n  +  1 )   
d [ ... ]( i )  =  0
}
else
{
 // This is for empty string
  for  i   in   range ( 7 ) 
   d  [ 6 5 )( i ]  -=   3
 }
         
 / \
 \  
---
/
\
-
1. Initiaize the value of d p [i ], j as ∞
2. If str [j]==str [0], then d  p  ( i ), j  becomes  the  length  of  common
substring
3. Else if j=0, then length of LCS is d   [ i   ],  .   ( j-1)  and  d  a  ,  j-2
4. else length  o f  LCS  is  max  between  dp  r  ],j  an d d    [  I  ]  ),  J-  2  )  \  //  This  line  calculates  for  each  row  before  current  one
5. Finally return d     [ m ]; n
6. This function returns the length   of  longest  substing  that  can  be  formed  by  two
strings
7. Time complexity is O ( m * n ) and space complexity   is  O ( min (m , n) ).
8. Where m and n are length
9. str and str are input strings
python code
str -------> input string  strin
LCSubsEquence ( ) → int
long  →  int
int  m  ;
n  :=| strlen ( st r1 |
m := | str len  （ str  |
if   m  > n   
return －1
dp [  ...  ](   i    ) : ＝ ０
For     each   j   from  １  to  n
If   str   2 [ j ]＝ str    1 [   0  ］
Then  $ d_p   [ m ]， j   : ｛＝  min  { d _p [m]，j－１，d _ p[m-１]}ﾋ d￠[﹂ﭿﻬﺎﯾﮪﬃ︙﷼}  else ＜n＞ d　pﶛ[＜]﵀[j−２=＞max{dp[I]j，d_p]＜j}＜2＜
：＝d p��[<]（n
＜＜＝＜＞＜=＜≤＜≥＞＞＝＞=＝＝=
This  function  returns  length o漣 longest  subsing that can be formed by two strings. It takes two input
string strl and str2 as input. The time complexity  is ○（m *n）and  space  complexity i s 〇（min（，n＜））. Here m
and n are length of string str懲 and string st＜r２，respectively