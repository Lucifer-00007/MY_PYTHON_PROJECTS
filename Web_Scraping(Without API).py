#Program to scrap any data from any website.

#Type1:-
# import requests
# from bs4 import BeautifulSoup

# url="https://docs.python-requests.org/en/master/user/quickstart/#make-a-request"
# d=requests.get(url)
# s= BeautifulSoup(d.content, "html.parser")
# #
# w= s.find(id = "make-a-request")
# # print(w)
#
# i=w.find_all(class_ ="highlight")
# # print(i)
# # print((i[3]))
#
# #here we have tried an alternative way to parse the classes. Here 'g' give same value like 'i'
# g=s.find_all("div", {"class":"highlight"})
# # g=s.find_all("div", {"id":"make-a-request"})
# # print(g[3])
#
#
#
# j=g[3].find_all(class_="s1")   #Some other options to replace 's1' are {gp,n,o,p}
# for items in j:
#     print(items.get_text())
#
# print("---------------------------------------------------------------------------------------------------------------")
#
# #Print all the links in a website
# links= s.find_all("a")
# for link in links:
#     if "http" in link.get("href"):
#         # print(link)
#         print(link.get("href"))



#-----------------------------------------------------------------------------------------------------------------------#
#Type2(leraning to use some basic parameters of requests module):-
# import requests
# # from bs4 import BeautifulSoup

# url="https://httpbin.org/get"
# p={'page':2,'count':'25'}
# # d=requests.get(url)

# q=(requests.get(url,params=p))

# print(q.text)
# print(q.url)
# print(q.json())



#-----------------------------------------------------------------------------------------------------------------------#
# Type3(Finding the temp of any place using google search without api):-
# import requests
# from bs4 import BeautifulSoup

# place=input("Enter the name of the place =")
# # place="kalyaneshwari"      #This value is taken for testing purpose
# search=f"temperature in {place}"
# url=f"https://www.google.com/search?q={search}"
# r=requests.get(url)

# s=BeautifulSoup(r.content,"html.parser")

# u=s.find("div", class_="BNeawe").text
# print(f"The Temerature at {place} is: {u}")


#-----------------------------------------------------------------------------------------------------------------------#
#Type4(Tried an alternative way of type3, but it's not working):-
import requests
from bs4 import BeautifulSoup

# place=input("Enter the name of the place =")
place="new delhi"
url=f"https://www.google.com/search?q=temperature+in+{place}"


d=requests.get(url)
s= BeautifulSoup(d.content, "html.parser")
# s= BeautifulSoup(d.text, "html.parser")

g=s.find("span", {"class":"wob_t TVtOme"})
# g=s.find("span", id="wob_tm")

# print(f"The temperature today at {place} is: ",g)
print(g)












