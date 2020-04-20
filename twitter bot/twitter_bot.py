import tweepy
import requests
import json
import shutil
import scrapy

from bs4 import BeautifulSoup

from PIL import ImageFont, ImageDraw, Image
import numpy as np

import arabic_reshaper

# install: pip install python-bidi
from bidi.algorithm import get_display

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import cv2

import io
import binascii

import os
from os import listdir
from os.path import isfile, join


import numpy as np
import shutil

from langdetect import detect

import re
import json
import base64

#
# # Authenticate to Twitter
# auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
# auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")
#
# # Create API object
# api = tweepy.API(auth)
#
# # Create a tweet
# api.update_status("Hello Tweepy")
#


def detect_lang_type(x):
    lang_type=(detect(x))

    return lang_type

def delete_all():
    shutil.rmtree('./croped')
    shutil.rmtree('./imgs_GET')
    shutil.rmtree('./meme_generated')

def reading_twitter():
    pass


def meme():
    url = "https://ronreiter-meme-generator.p.rapidapi.com/meme"

    querystring = {"font": "Impact", "font_size": "50", "meme": "Condescending-Wonka", "top": "Top text",
                   "bottom": "Bottom text"}

    headers = {
        'x-rapidapi-host': "ronreiter-meme-generator.p.rapidapi.com",
        'x-rapidapi-key': "6e87be2830mshc6af982aaf38aa5p19e324jsnbb83594f19aa"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).content
    with open('image_name.jpg', 'wb') as handler:
        handler.write(response)



def dowload_twitter_img(url , name):
#     https://twitter.com/iFIHIDz/status/1246411092638793729/photo/1
#     url = "https://pbs.twimg.com/media/EUwkRp1WkAAr8gJ.jpg"

    querystring = {"font": "Impact", "font_size": "50", "meme": "Condescending-Wonka", "top": "Top text",
               "bottom": "Bottom text"}

    headers = {
    'x-rapidapi-host': "ronreiter-meme-generator.p.rapidapi.com",
    'x-rapidapi-key': "6e87be2830mshc6af982aaf38aa5p19e324jsnbb83594f19aa"
}
    fils= [f for f in listdir('./imgs_GET') if isfile(join('./imgs_GET', f))]

    response = requests.request("GET", url).content
    with open('./imgs_GET/'+name+'.jpg', 'wb') as handler:

        if (name not in fils):
            handler.write(response)
def pix_meme():

    # Draw some funny text on top & button of the famous Michael Jordan crying face.
    # https://pixlab.io/cmd?id=drawtext is the target command
    req = requests.get('https://api.pixlab.io/drawtext&key=c130aaz85chm25syjx9teudef16nq7', params={
        'img': 'https://pixlab.io/images/jdr.jpg',
        'top': 'someone bumps the table',
        'bottom': 'right before you win',
        'cap': True,  # Capitalize text,
        'strokecolor': 'black',
        'key': 'Pix_Key',
    })
    reply = req.json()

    print (req)
    if reply['status'] != 200:
        print(reply['error'])
    else:
        print("Meme: " + reply['link'])


def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)



def get_twitter_img_url():
    raw_html = simple_get('https://twitter.com/iFIHIDz/status/1246410982047481856')
    html = BeautifulSoup(raw_html, 'html.parser')


    urls=[]

    str_html = str(html)

    result = str_html.split(' ')

    for i in range(len(result)):
        if result[i].startswith('data-image-url'):
            print(result[i].split('"')[1])

            urls.append(result[i].split('"')[1])

    return urls

def split_posts():
    cmnd_tag = ""
    meme_img_url = ""

    raw_html = simple_get('https://twitter.com/iFIHIDz/status/1251892647872118784')
    html = BeautifulSoup(raw_html, 'html.parser')


    urls = []

    str_html = str(html)

    result = str_html.split('<div class="js-tweet-text-container">')



    return result


def get_tweet_id(post , posts):

    id_indx=-1

    soup = BeautifulSoup(str(post), "html.parser")


    #print (post)



    r=soup.find("span", {"class": "ProfileTweet-actionCountForAria"})
    r=r.__str__()

    r=r.split(" ")



    for st in range(len(r)):
        if "profile-tweet-action-reply-count-aria-" in r[st]:
            id_indx=st
            break

    r = r[id_indx].split("\"")


    r = r[1].split("-")





    return r[-1]


def add_as_processed(id):
    with open("posts_processed.txt", "a") as myfile:
        myfile.write(str(id)+"\n")



def check_isProcessed(id):



    result=False


    # with open("test.txt", "a") as myfile:
    #     myfile.write("appended text")

    f = open("posts_processed.txt", "r")
    ids= f.read()

    ids = ids.split("\n")




    for pid in ids:

        if pid==id:
            result=True


    return result







def get_twitter_tweets_url(raw):

    cmnd_tag=""
    meme_img_url=""
    isValid=True
    cmnd_type = []
    cmnd_value = []

    # raw_html = simple_get('https://twitter.com/iFIHIDz/status/1247365192620654597')
    # html = BeautifulSoup(raw, 'html.parser')
    #
    #
    # urls=[]
    #
    # str_html = str(html)
    #
    # #print(raw)
    #
    # result = str_html.split('<div class="js-tweet-text-container">')
    #
    # print (len(result))
    #
    #






    soup = BeautifulSoup(str(raw),"html.parser")




    for strong_tag in soup.find_all('p'):
        cmnd_tag=(strong_tag.text)

        break



    print(cmnd_tag)







    print('------------cmd tag')









    comnds = cmnd_tag.split('\n')


    if len(comnds) !=7:
        isValid=False
        return meme_img_url , cmnd_type , cmnd_value , isValid



    print(comnds)
    for c in comnds:
        cmnd_type.append(c.split(":")[0])
        cmnd_value.append(c.split(':')[1])








    for img_tag in soup.find_all('img'):


        meme_img_url=(img_tag['src'])
        break







    return meme_img_url , cmnd_type , cmnd_value , isValid


def filter_url_get_name(url_lst):

    name=[]

    for l in url_lst:

        name.append(l.split('/')[-1].split('.')[0])

    return name


def conv(image_file):
    try:
        fin = open(image_file, "rb")
        data = fin.read()
        fin.close()
    except IOError:
        print("Image file %s not found" % image_file)
        raise SystemExit
    hex_str = str(binascii.hexlify(data))
    hex_list = []
    bin_list = []
    for ix in range(2, len(hex_str)-1, 2):
        hex = hex_str[ix]+hex_str[ix+1]
        hex_list.append(hex)
        bin_list.append(bin(int(hex, 16))[2:])
    bin_str = "".join(bin_list)
    return(bin_str)


def upload_image_to_processing_service(path):


    print (path)
    path='./imgs_GET/w.jpg'

    img = cv2.imread(path)

    #path=conv(path)



    print(path)




    print('-----start----upload')


    dict = {

        'image': img
    }




    url = "https://ronreiter-meme-generator.p.rapidapi.com/images"
    img = img.tolist()

    payload =dict





    headers = {
        'x-rapidapi-host': "ronreiter-meme-generator.p.rapidapi.com",
        'x-rapidapi-key': "6e87be2830mshc6af982aaf38aa5p19e324jsnbb83594f19aa",

        'content-type': "multipart/form-data"
        #'content-type': "application/json"
    }

    response = requests.request("POST", url,  data=payload, headers=headers)

    print(response.text)
    print (response.headers)

    exit(0)






def crop(path , f):
    img = cv2.imread(path)
    ## (1) Convert to gray, and threshold
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    th, threshed = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

    ## (2) Morph-op to remove noise
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    morphed = cv2.morphologyEx(threshed, cv2.MORPH_CLOSE, kernel)

    ## (3) Find the max-area contour
    cnts = cv2.findContours(morphed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    cnt = sorted(cnts, key=cv2.contourArea)[-1]

    ## (4) Crop and save it
    x, y, w, h = cv2.boundingRect(cnt)
    dst = img[y:y + h, x:x + w]
    cv2.imwrite("./croped/"+f, dst)

def get_all_images_in_rapid():
    url = "https://ronreiter-meme-generator.p.rapidapi.com/images"

    headers = {
        'x-rapidapi-host': "ronreiter-meme-generator.p.rapidapi.com",
        'x-rapidapi-key': "6e87be2830mshc6af982aaf38aa5p19e324jsnbb83594f19aa",

    }

    response = requests.request("GET", url, headers=headers)

    #print((response.text))

    temp=response.text.replace('[','')
    temp=temp.replace(']','')
    temp = temp.replace('"', '')
    temp = temp.replace(' ', '')

    lst = temp.split(',')

    for l in lst:
        if l.startswith('ja'):
            print(l)
#
# get_all_images_in_rapid()
#
# exit(0)



def generate_meme_ar(path , file_name ,cmnd_type , cmnd_value, tpos=1 , bpos=1 ):

    print('ar meme  start')


    print('start loop on comnds')

    for cmn in range(len(cmnd_type)):


        temp = cmnd_type[cmn]

        print(temp)

        if temp == 'اعلى':
            top_txt = cmnd_value [cmn]
        elif temp == 'اسفل':
            bot_txt  = cmnd_value [cmn]
        elif temp == 'موقع الخط السفلي':
            b_per=int(cmnd_value [cmn])
        elif temp =='موقع الخط العلوي':
            t_per=int(cmnd_value [cmn])
        elif temp =='الخط':
            font=int(cmnd_value [cmn])
        elif temp =='الحجم':
            font_size=int(cmnd_value [cmn])

    print('end loop on comnds')



    img = cv2.imread(path)

    im = img

    im = np.array(im)
    ary = im.copy()

    im = Image.fromarray((im))



    if tpos ==1:# left
        top_pos = 0
    elif tpos ==2:#mid
        top_pos = int(ary.shape[0] / 2)
    else:
        top_pos = int(ary.shape[0])

    if bpos ==1:# left
        bot_pos = 0
    elif bpos ==2:#mid
        bot_pos = int(ary.shape[0] / 2)
    else:
        bot_pos = int(ary.shape[0])


    print(100*ary.shape[1]/100)
    print( int(100*ary.shape[1]/100))
    top_percent = int(t_per*ary.shape[1]/100)
    bot_percent = int(b_per*ary.shape[1]/100)


    x = 'فهد    يبيسسطسسيحبك هههههه'.encode('utf-8')
    # x=u'' + x.decode('utf-8')
    x = x.decode('utf-8')


    if font==1:
        fontpath = "./arabic_fonts/AArghavan.ttf"
        font = ImageFont.truetype(fontpath, font_size)
    elif font==2:
        fontpath = "./arabic_fonts/Changa-SemiBold.ttf"
        font = ImageFont.truetype(fontpath, font_size)
    elif font==3:
        fontpath = "./arabic_fonts/Elegant-ar.ttf"
        font = ImageFont.truetype(fontpath, font_size)
    elif font==4:
        fontpath = "./arabic_fonts/Syria-Alqusair.ttf"
        font = ImageFont.truetype(fontpath, font_size)




    reshaped_text = arabic_reshaper.reshape(x)  # correct its shape
    x = get_display(reshaped_text)

    ############################################## top text reshape it to correct arabic order
    top_txt=top_txt.encode('utf-8')
    top_txt=top_txt.decode('utf-8')

    reshaped_text = arabic_reshaper.reshape(top_txt)  # correct its shape
    top_txt = get_display(reshaped_text)

    ############################################## bot text reshape it to correct arabic order
    bot_txt = bot_txt.encode('utf-8')
    bot_txt = bot_txt.decode('utf-8')

    reshaped_text = arabic_reshaper.reshape(bot_txt)  # correct its shape
    bot_txt = get_display(reshaped_text)

    draw = ImageDraw.Draw(im, )
    draw.text((top_pos, top_percent), top_txt, font=font)
    draw.text((bot_pos, bot_percent), bot_txt, font=font)
    im = np.array(im)
    cv2.imwrite("./meme_generated/" + file_name, im)

    print('ar meme  end')


def generate_meme(path , file_name ,cmnd_type , cmnd_value, tpos=1 , bpos=1 ):



    lang=detect(cmnds_value[0])



    if lang =='ar':
        generate_meme_ar(path , file_name ,cmnd_type , cmnd_value, tpos=1 , bpos=1 )
        return

    for cmn in range(len(cmnd_type)):

        temp = cmnd_type[cmn]

        if temp == 'top':
            top_txt = cmnd_value [cmn]
        elif temp == 'bot':
            bot_txt  = cmnd_value [cmn]
        elif temp == 'bpos':
            b_per=int(cmnd_value [cmn])
        elif temp =='tpos':
            t_per=int(cmnd_value [cmn])
        elif temp =='font':
            font=int(cmnd_value [cmn])
        elif temp =='font size':
            font_size=int(cmnd_value [cmn])




    #tpo
    img = cv2.imread(path)

    ary=np.asarray(img)

    print(ary.shape)


    if tpos ==1:# left
        top_pos = 0
    elif tpos ==2:#mid
        top_pos = int(ary.shape[0] / 2)
    else:
        top_pos = int(ary.shape[0])

    if bpos ==1:# left
        bot_pos = 0
    elif bpos ==2:#mid
        bot_pos = int(ary.shape[0] / 2)
    else:
        bot_pos = int(ary.shape[0])


    print(100*ary.shape[1]/100)
    print( int(100*ary.shape[1]/100))
    top_percent = int(t_per*ary.shape[1]/100)
    bot_percent = int(b_per*ary.shape[1]/100)




    cv2.putText(img, top_txt, (top_pos, top_percent), font, font_size, (255, 255, 255), font_size, cv2.LINE_AA)

    cv2.putText(img, bot_txt, (bot_pos, bot_percent), font, font_size, (255, 255, 255), font_size,  cv2.LINE_AA)


    # Parameters are as follows:
    #
    # cv2.putText(img, text, (org), font, fontScale, color, thickness, linetype)
    #
    # img: your image
    # text: a string of text to print on image
    # org: bottom-left corner of the text string in the image (x,y)
    # font: font type
    # fontScale: font scale
    # color: text color (B,G,R)
    # thickness: text line thickness
    # lineType: line type (8)

    cv2.imwrite("./meme_generated/"+file_name,img)





    # It shows the image on the screen. The first argument is for the image title
    # and the second is for the image variable.



def send_email(to , file , path):
    # Python code to illustrate Sending mail with attachments
    # from your Gmail account

    # libraries to be imported
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    ind=(to.find("pic.twitter.com"))


    if ind != -1:
        to=(to[:ind])




    fromaddr = "zeke25520@gmail.com"
    toaddr = to



    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "generated meme"

    # string to store the body of the mail
    body = "please see the attachment ( ur requested meme)."

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent
    filename = file
    attachment = open(path, "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "1q2345454321F")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()


def anaylize():
    img = cv2.imread("./croped/ee.jpg");

    ary = np.asarray(img)
    print(ary.shape)

    print (ary[0,0,:])

    img = cv2.imread("./imgs_GET/ee.jpg");



    ary = np.asarray(img)

    print(ary.shape)

    print(ary[0, 0, :])

#optional step , delete all imgs
# delete_all()
# exit(0)
# step -1 : split to tweets

while True:

    print("---------------------------start while-------------------------")
    posts = split_posts()

    print("number of posts: "+str(len(posts)))





    #step 0 : check post id if its already proccessed
    del posts[0]
    del posts[0]

    pst=1

    for p in posts:

        print("post number: "+str(pst))
        pst+=1
        print("step 0")
        post_id=get_tweet_id(p , posts)

        temp=check_isProcessed(post_id)

        print("post id="+str(post_id))

        print(temp)
        if temp == False:



            # step 1.5: get one tweet comnds
            print("step 1.5")
            raw_img_url, cmnds_type, cmnds_value , valid = get_twitter_tweets_url(p)

            if valid == True:

                print("its valid")


                img_urls = []
                img_urls.append(raw_img_url)
                # step 2 : filter url to get name
                print("step 2")
                names = filter_url_get_name(img_urls)

                print(names)


                # step 3 : download all images and save them as as ,jpg in img_GET folder
                print("step 3")
                for img in range(len(img_urls)):
                    dowload_twitter_img(img_urls[img], names[img])

                # step 4: generate meem


                fils = [f for f in listdir('./imgs_GET') if isfile(join('./imgs_GET', f))]

                print("crop op")
                crop('./imgs_GET/' + fils[0], fils[0])
                os.remove('./imgs_GET/' + fils[0])

                f=fils[0]

                fils = [f for f in listdir('./croped/') if isfile(join('./croped/', f))]

                print("step 4")
                generate_meme('./croped/' + f, f, cmnds_type, cmnds_value)

                os.remove('./croped/' + fils[0])

                print("get email")
                for cmn in range(len(cmnds_type)):

                    temp = cmnds_type[cmn]

                    if temp == 'email':
                        email = cmnds_value[cmn]
                        send_email(email, f, "./meme_generated/" + f)

                print("-----------------post proccesed----------------------------")

            print("mark as prosecced")
            add_as_processed(post_id)







exit(0)

# step 1 : get all image url from tweet
#img_urls=get_twitter_img_url()




#step 1.5: get one tweet comnds
raw_img_url , cmnds_type,cmnds_value=get_twitter_tweets_url()


print (raw_img_url)


img_urls=[]
img_urls.append(raw_img_url)
# step 2 : filter url to get name
names=filter_url_get_name(img_urls)

print (names)




# step 3 : download all images and save them as as ,jpg in img_GET folder
for img in range(len(img_urls)):
    dowload_twitter_img(img_urls[img] ,names[img] )

#
# # step 4 : upload those images to image processing service to create meme
#
# fils= [f for f in listdir('./imgs_GET') if isfile(join('./imgs_GET', f))]
#
#
# for f in fils:
#     print(f)
#     upload_image_to_processing_service('./imgs_GET/'+f)
#






# step 5 : request service using restful (which is creating meme)


# step 6 : download the meme and save it


# step 7: generate meem

fils= [f for f in listdir('./imgs_GET') if isfile(join('./imgs_GET', f))]

for f in fils:
    print(f)
    crop('./imgs_GET/'+f , f)


fils= [f for f in listdir('./croped/') if isfile(join('./croped/', f))]

for f in fils:
    print(f)
    generate_meme('./croped/'+f , f , cmnds_type , cmnds_value)

    send_email("alhamazani.f@gmail.com",f,"./meme_generated/"+f)





# step 7 : upload modified img (meme)  to twitter agine -----> I am not sure if I can do it :( as its require endpoints

