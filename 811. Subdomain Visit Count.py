#https://leetcode.com/problems/subdomain-visit-count/

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count_domains = collections.defaultdict(int)
        domains_with_count = []
        for domain in cpdomains:
            times, full_domain = domain.split()[0], domain.split()[1]
            
            
            count_domains[full_domain] += int(times)
            index = full_domain.find('.')
            while index != -1:
                full_domain = full_domain[index + 1:]
                count_domains[full_domain] += int(times)
                index = full_domain.find('.')
            
        for domain, times in count_domains.items():
            domains_with_count.append(" ".join((str(times), domain)))
        return domains_with_count
