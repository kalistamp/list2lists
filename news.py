#  TEST TEST ONE TWO
# By: калиштамп

import webbrowser
import time

x = ' '
print(x*2)

cstop = [        'https://therecap.org/',
        'https://psw1234.com/news/',
        'https://www.trickster.dev/',
        'https://news.ycombinator.com/',
        'https://www.reddit.com/r/privacy/',
        'https://www.reddit.com/r/Piracy/',
        'https://www.hackingarticles.in',
        'https://www.ibtimes.com',
        'https://www.theepochtimes.com/',
        'https://www.mintpressnews.com/',
        'https://therecord.media/',]

tech = [       'https://krebsonsecurity.com/',
        'https://dumpoir.com/v/llllap3xllll',
        'https://www.producthunt.com/',
        'https://securityaffairs.co/wordpress/',
        'https://cybersecurity-magazine.com/',
        'https://www.hackerone.com/,vulnerability-and-security-testing-blog',
        'https://telegra.ph/Razvedka-dlya-podgotovki-DDoS-atak-03-05',
        'https://telegra.ph/KORISN%D0%86-POSILANNYA-DLYA-DOPO[        ',
        'https://www.trickster.dev/',
        'https://news.ycombinator.com/',
        'https://www.reddit.com/r/privacy/',
        'https://www.reddit.com/r/Piracy/',
        'https://www.hackingarticles.in',
        'https://www.ibtimes.com',
        'https://www.theepochtimes.com/',
        'https://www.mintpressnews.com/',
        'https://therecord.media/',
        'https://hakin9.org/blog-2/',
        'https://www.hackingarticles.in' ]

xtras = [       'http://unlimitedhangout.com/',
        'https://www.thelastamericanvagabond.com/',
         'https://heystacks.com/hall-of-fame', 
        'https://www.investmentwatchblog.com/author/maizipeng/',
        'https://thegradient.pub/',
        'https://www.sciencedaily.com/',
        'https://www.propublica.org/',
        'https://viewdns.info/iphistory/?domain=therecap.org',]

KITCHEN_TABLE = cstop + tech + xtras 

def open_news():
    choice = input('What Section of news would you like to read? \n [Enter the Letter]: ')
    print(x)
    if choice == 'c':
        for url in cstop:
            time.sleep(2)
            webbrowser.open_new_tab(url)
    elif choice == 't':
        for url in tech:
            time.sleep(2)
            webbrowser.open_new_tab(url)
    elif choice == 'x':
        for url in xtras:
            time.sleep(2)
            webbrowser.open_new_tab(url)
    else:
        print(' [!] It seems you made a typo, that section does not exist')

def print_news():
    choice = input('What Section of news would you like to read? \n [Enter the Letter or type "all" for everything ...]: ')
    print(x)
    if choice == 'c':
        for number, links in enumerate(cstop):
            print(number, links)
    elif choice == 't':
        for number, links in enumerate(tech):
            print(number, links)
    elif choice == 'x':
        for number, links in enumerate(xtras):
            print(number, links)
    elif choice == 'all':
        for number, links in enumerate(KITCHEN_TABLE):
            print(number, links)
    else:
        print(' [!] It seems you made a typo, that section does not exist')



which = input('Would you like to \"open\" or \"view\" News Sections? :    ')

print(x*2)
print('TABLE OF CONTENTS:')
print('cstop(c): The Basics ')
print('tech(t): Tech related News ')
print('Xtras(x): All the Extras ')

if which == 'open':
    open_news()
elif which == 'view':
    print_news()
else:
    print('  [!] It seems you made a typo - that option does not exist')
