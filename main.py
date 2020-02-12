import requests
from bs4 import  BeautifulSoup
 


def run():
    try:
        site_link = 'https://khatrimaza1.k33.club'
        Get = requests.get(site_link)
    except:
        site_link = input('Enter the latest url of khatrimaza: ')
        Get = requests.get(site_link)

    soup = BeautifulSoup(Get.content, 'html.parser')
    movie_list = soup.find(class_="home-wrapper thumbnail-wrapper").find_all(class_="thumb col-md-2 col-sm-4 col-xs-6")

    for mov in movie_list:
        URL_l = requests.get('{}'.format(mov.find_all('a')[0].get('href')))
        soup_l = BeautifulSoup(URL_l.content, 'html.parser')
        movie_body = soup_l.find(class_="page-body")

        Img_link = movie_body.find(class_="aligncenter").get('src') # Img link
        Mov_name  = movie_body.find(class_="aligncenter").get('alt') # Movie/file name 

        body = []
        for i in movie_body.find_all('strong'): # Body
            body.append(i.get_text())


        d_link = movie_body.find_all(class_="dbuttn blue") #LINK
        LINK = []
        for i in d_link: # LINK
            try:
                LINK_URL = requests.get('{}'.format(i.get('href')))
                LINK_SOUP = BeautifulSoup(LINK_URL.content, 'html.parser')
                LINK_BODY = LINK_SOUP.find(class_="page-body")
                link = LINK_BODY.find(class_="link_container").find('a').get('href')         
                LINK.append(link)

            except:

                try:
                    LINK_URL = requests.get('{}'.format(i.get('href')))
                    LINK_SOUP = BeautifulSoup(LINK_URL.content, 'html.parser')
                    LINK_BODY = LINK_SOUP.find(class_="page-body").find_all('a')[0]
                    S_LINK_URL = requests.get('{}'.format(LINK_BODY.get('href')))
                    S_LINK_SOUP = BeautifulSoup(S_LINK_URL.content, 'html.parser')
                    S_LINK_BODY = S_LINK_SOUP.find(class_="page-body")
                    link = S_LINK_BODY.find(class_="link_container").find('a').get('href')
                    LINK.append(link)

                except:
                    print('error\nnew')
                    LINK.append('{}'.format(i.get('href')))

            print( Mov_name, Img_link, LINK, body)
run()