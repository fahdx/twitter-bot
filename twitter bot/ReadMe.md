# MeMes generator

this service generate mems based in twitter post, main thread have to be specified in the twitter-bot file (inside ```def split_posts()```). 

this service will listen to any update on the threads and check if the post already processed or not. as its crawler, email needed inside the post to send the generated image to. 


## content of tweet - en

top: top text here

tpos: 10 

bot: bottom text comes here

bpos: 80 

font: 2

email:to_email@gmail.com


[image here]

## content of tweet - ar

اعلى:النص هذا في الاعلى
 
اسفل:النص هذا في الاسفل 

موقع الخط السفلي:70 

موقع الخط العلوي:30 

الخط:3 

الحجم:30

email:to_email@gmail.com

[image here]


## License
[MIT](https://choosealicense.com/licenses/mit/)
