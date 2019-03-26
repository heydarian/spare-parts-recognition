# Spare Part Recognition

![avatar](https://jam4.sapjam.com/profile/vQ2WGFrz1l1cmyPIZX6G8c/documents/exUx6J98mB0A3RqbVkE0W1/thumbnail?max_x=1200&max_y=1200)

Identifying the key business drivers which have a major impact on the performance of a company is essential for the sustainability of a business. In many companies, performance is defined by agile and efficient master data management, where decreasing the amount of man-hour per lookup will lead into increasing the overall business revenue. The rise of disruptive and game-changing innovations lets the world spin faster for such companies and lets them get faster and better results.

One of these lucky winners are service engineers, who never had an easier work life than today. The machines of their customers apply certain standards and have enriched documentations with long lists of predefined maintenance tasks and plans. Multiple customers are being visited from day to day, to let inspect and fix their machines as planned in their maintenance contracts.

But what would life be without any challenges. Luckily, we still live in a time in which unprecedented and unexpected issues may appear at anytime, so one challenge still exists in finding the right spare parts in time, outside the regular maintenance windows, without causing additional delays and outages by ordering wrong spare parts which may even harm the machines. This applies for mostly any technician services provided across the globe. Especially for those dealing with a high amount of available spare parts.

![avatar](https://jam4.sapjam.com/profile/6DWIDrLEPbPP75kn8Y3ezL/documents/kR5iWagKZlC5FE1gMPQR8X/thumbnail?max_x=1200&max_y=1200)

Did you know, that an average car has about 30.000 parts? 

After tracking down the root cause of a malfunctional machine to a broken spare part the quest starts to tell what this spare part really is and finally finds it in the inventory of available spare parts. Since there are tens of thousands of spare parts in industrial machines, and hundreds of different brands and models, it is impossible for technicians to remember them all, in order to identify any given spare part. 

With the new spare part recognition prototype inside the SAP Business One Service App, the broken spare parts will be captured with a mobile device and analyzed by SAP’s next gen machine learning capabilities throughout SAP Leonardo within seconds to find the right inventory item to order.

![avatar](https://jam4.sapjam.com/profile/6DWIDrLEPbPP75kn8Y3ezL/documents/eK7TpC2RuWuBdfBAI4Hlm1/thumbnail?max_x=1200&max_y=1200)

The app prototype indicates that this spare part is a pinion gear with a 97% match. 

After suggesting possible replacements for the broken parts, a sales order will be created and signed off to close the service ticket.

With the help of image recognition, service engineers have the right spare part at their fingertips and new employees can be onboarded much faster without the need of learning spare parts by heart. 

As more and more companies empower their employees with smart mobile devices and intelligent enterprise apps during their worktime, the human error gets mitigated and the overall performance is significantly increasing.

## Installation Guide

### Server

#### run main.py to start up server

[python3]
depend on requests, tornado, urllib3

``` bash
pip install -r requirements.txt
python main.py
```

#### run server via docker-compose

``` bash
docker-compose up -d spare-parts-recognition
```