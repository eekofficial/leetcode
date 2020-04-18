#https://leetcode.com/problems/unique-email-addresses/

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            email_full = email.split('@')
            local_name = list(email_full[0])
            domain_name = email_full[1]
            while '.' in local_name:
                local_name.remove('.')
            if '+' in local_name:
                local_name = local_name[:local_name.index('+')]
            unique_emails.add("{}@{}".format(str(local_name), domain_name))
        return len(unique_emails)
