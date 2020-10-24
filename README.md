# twitter-bot
# MeMes generator

this service generate mems based in twitter post, main thread have to be specified in the twitter-bot file (inside ```def split_posts()```). 

this service will listen to any update on the threads and check if the post already processed or not. as its crawler, email needed inside the post to send the generated image to. 
```diff
- Note: this program based on information retreival not an API. Due to that, if many posts posted in the target thread will lead to unable the scroll down component which makes the crawler cant get the lateset posts.
```
## content of tweet - en

top: top text here

tpos: 10 

bot: bottom text comes here

bpos: 80 

font: 2

email:to_email@gmail.com

[image here]


Example of putput

![EU-h8FIXkAAYCwT](https://user-images.githubusercontent.com/6011793/97081992-f3c41800-160e-11eb-84c8-da11abe6b09b.jpg)


## content of tweet - ar

اعلى:النص هذا في الاعلى
 
اسفل: 

موقع الخط السفلي:70 

موقع الخط العلوي:30 

الخط:3 

الحجم:30

email:to_email@gmail.com

[image here]

example of output

![EV-f5pDWAAAgKJf](https://user-images.githubusercontent.com/6011793/97082022-30900f00-160f-11eb-9a02-901bab52c1c3.jpg)



## License
[MIT](https://choosealicense.com/licenses/mit/)
