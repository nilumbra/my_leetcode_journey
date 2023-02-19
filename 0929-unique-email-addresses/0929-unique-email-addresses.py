class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        """
        Two email addresses local1@domain1, local2@domain2 are the same if 
        local1 = local2 and domain1 = domain2
        
        For the domain we just read it literally. 
        For the local name, if we meed a '.', we ignore it and read the next char,
                            if we meed a '+', we stop reading.
                            
        Convert all local names containing . and + to its "canonical" form
        """
        
        email_database = set()
        for email in emails:
          local, domain = email.split("@")
          t = []
          for c in local:
            if c == '.':
              continue
            elif c == '+':
              break
            else:
              t.append(c)
          
          local = ''.join(t)
          email_database.add((local, domain))
        
        return len(email_database)
        