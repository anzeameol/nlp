
import re
def validate_email(email):
    # 1. E-Mail address must start with a letter or '_'
    pattern = r'^[a-zA-Z_]+'  
        
     
 # 2. Must contain an @ symbol
 pattern |=  r'[^@]*@[^\.]' 
 		
  #  3. Can contain a domain name with the following restrictions: -
      #     a. Minimum of 3 characters
       # b. Maximum of  255 characters + 4 characters for the TLD
          # c. At least one letter
          pattern|= re.compile(r"[aA]{3,}\.[\w\-]" . join("|[Aa]") ))
            
#   4. Domain name must end with '.' character
pattern | nd 0
	  pattern2 -->=r"\."
           
 return bool(re.match(pattern+pattern2, email)) != False
email ? validate _email (email)
print("Valid e_mail:", "Valid") if validate e mail (e mail) else "Invalid"	  