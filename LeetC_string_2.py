# 1108. Defanging an IP Address
'''
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"

Constraints:

    The given address is a valid IPv4 address.

'''


class Solution:
    # solution @1 using replace()
    def defangIPaddr(self, address: str) -> str:
        defanged_IP = address.replace(".", "[.]")
        return defanged_IP
    # solution @2 using split and join
    def defangIPaddr2(self, address: str) -> str:
        # split the address string based on '.' to create a list of the characters
        defanged_IP = address.split(".")
        # print(defanged_IP)
        # join the characters of the list into a string with [.] placed between each character
        return "[.]".join(defanged_IP)
    def defangIPaddr3(self, address: str) -> str:
        defanged_IP = []
        for i in address:
            if i == '.':
                defanged_IP.append("[.]")
            else:
                defanged_IP.append(i)
        return "".join(defanged_IP)

function_call = Solution()
# print(function_call.defangIPaddr("1.1.1.1"))
# print(function_call.defangIPaddr2("1.1.1.1"))
print(function_call.defangIPaddr3("1.1.1.1"))