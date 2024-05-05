![Vuejs notion](https://github.com/TH-Activities/saturday-hack-night-template/assets/117498997/b879ba9f-2057-431b-99db-e86a0010b1ea)

# BookMyStage

In our college campus  whenever there is an event like a workshop , orientation session , talk sessions , jamming sessions , competitions organized by various clubs and departments , we have to take the permission from the authorities though a request letter , To Make this process more easier for the colleges , we have introduced this platform where  coordinators of events can book a venue for their event online thought a web app and the authorities can verify the request and approve or reject them 
## Team members

1. [Navadeep Satheesh](https://github.com/Navadeep-Satheesh/)
2. [Meenakshi Sudhir](https://github.com/meenakshysudhir)
3. [Jiya Rose Joshy](https://github.com/j1i2y3a4)
4. [Renjith Rajan](https://github.com/Renjith312)




## How it Works ?

1.  There are two apps user app and admin app  , the user app is for the club coordinators and managers of the even where they can book venues 
2. The Person has login using a id and password provided ,
3. They have to select a stage from the list of stages and they will be redirected to the book page where they can see the availability of the venue on the date selected in a timeline chart , 
4. The can do the booking by filling the details and pressing the book button
5. The bookings that we have done and their status can be seen in the bookings tab 
6. The Admin can view the bookings and can either accept it or reject it 


## Images 

### User

#### Login Page


![[screenshots/WhatsApp Image 2024-05-05 at 2.40.51 PM 1.jpeg]]

#### select the desired venue


![[screenshots/WhatsApp Image 2024-05-05 at 2.46.36 PM.jpeg]]

#### Book the Slot

![[screenshots/WhatsApp Image 2024-05-05 at 2.47.53 PM.jpeg]]


#### View Your Bookings


![[screenshots/WhatsApp Image 2024-05-05 at 2.46.56 PM 1.jpeg]]


### Admin

#### approve or reject bookings

![[screenshots/WhatsApp Image 2024-05-05 at 3.02.25 PM.jpeg]]
## Libraries used

1. Vue.js for front end
2. flask as Backend
3. Sqllite as database

## How to configure

run ```
```bash
npm install  # to install the required modules 
vue serve # to run the vue project
```

##### note
vue serve sometimes dont work with powershell , in such case either run it other terminals like git bash and cmd

## How to Run

##### User app

inside the frontend/frontent/ 
run **vue serve** to to run the user app

##### Admin App
inside the admin/ folder
run **vue serve** to run admin app 

##### Backend 

inside the backend folder 
run **python app.py**  to the flask server

### login credentials 

#### for user app

email : tinkerhub@gmail.com
password : 1234

#### for the admin app
email: principal@gmail.com
password : 1234

