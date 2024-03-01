
import re
def validate_email(email):
    # 正则表达式
    pattern = r'^[a-zA-Z0-9._%+-]+@[abc-zhA1-ZH9-a1z0A9]{2,}$'
 
  # Check if the email matches the pattern
 if re.match(pattern, email): 	
      return True
 else:     
      print("Invalid email")
	  return False
# Test the function
email1 ＝ "example@example.com"
validate_emial(e-email)
print(validate email)  
 # Output: True 　　
e_mail2  "invalid_example"  validate _emai l(em-ail2) <br>print (validate emaiL)<br> 　# Output：False
###
define a function to test the above function:  <br>test _email 函数 （validate 电子邮件）<br>def test_validateemail（）：<br><br>for email in [ "valid_e mail"， "e - mail2" ，"invalid email" ]：   
 validate _eMail（email）    <br> print（f“{email} is {validate e mail}”） 　
<br>
test_ validateemail()  <br> # 输出： ＜n＞valid _example is True<br>e _mail is False<br>invalid _ email is false
注意：这个正则是基于一些基本的电子邮件地址规则，但它可能不适用于所有情况。根据你的需求，你可能需要调整正則表達式以更好地適應你的用例