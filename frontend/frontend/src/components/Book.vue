<template>
    <div class="book">

        <div class="timeline">

            <div class="date_section">

                <input type="date" class = "timeline_date">

            </div>

            <div class="timeline_div">

                <div class="marking_area">

                    <div v-for="booking in bookings" class="booked_area" :key="{ booking }" v-bind:style="{top: `${booking[0]}px` , height:`${booking[1]-booking[0]}px`}"> </div>

                </div>
                <div class="time_stamp_area">

                    <ul>
                        <li v-for="time in times" v-bind:key="time">{{ time }}</li>
                    </ul>

                </div>

            </div>

        </div>

        <div class="book_area">

            <div class="book_div">

                <h2>BOOK SLOT</h2>

                <input type="date" class="select_date">
                <div class="select_time"> <input type="time"> to <input type="time"> </div>
                <input type="text" class="purpose">
                <input type="submit" class="submit" value="BOOK">


            </div>

        </div>


    </div>
</template>

<script>


var bookings = [

    ["9:00 AM", "10:00 AM"],
    ["12:00 PM", "1:00 PM"],
    ["3:00 PM", "5:00 PM"],
]

for( let item of bookings){
    item[0] =   parseInt(convertTime(item[0]))
    item[1] = parseInt( convertTime(item[1]))
}

function convertTime(time) {

    let converted = 0
    let a = time.split(" ")[1]
    let t = time.split(" ")[0]
    let hours = parseInt(t.split(":")[0]) 
    if (a == "PM" && hours < 12) {
        hours += 12
    }

    hours -= 9
    
    let minutes = parseInt(t.split(":")[1])
    converted += hours * 100 + minutes

    

    let final = parseInt((converted / 1200) * (960 + 260))
    console.log(converted , final)

    return final


}

let times = []
let time;
for (let i = 9; i <= 21; i++) {

    let hour = i;
    let a = "AM"
    if (i > 12) {
        hour = i - 12;
        a = "PM"
    }

    time = `${hour}:00 ${a}`
    console.log(time)
    times.push(time)

}

console.log(bookings)


export default {
    name: "BookRoom",
    data: () => {
        return {

            times: times,
            bookings: bookings
        }
    }
}


</script>

<style>
.book {
    width: 100vw;
    height: 100vh;
    padding-top: 120px;
    display: flex;
    justify-content: center;


}

.book_area {
    width: 45%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center
}

.timeline {
    box-shadow: rgba(0, 0, 0, 0.1) 0px 4px 12px;
    border: 1px solid rgb(220, 220, 220);
    width: 45%;
    height: max-content;


}

.book_div {
    width: 90%;
    height: 400px;
    background-color: white;
    box-shadow: rgba(0, 0, 0, 0.1) 0px 4px 12px;
    border: 1px solid rgb(222, 222, 222);

    display: flex;


    flex-direction: column;
}

.book_div h2 {
    margin-left: 50px;
    margin-top: 25px;
    font-size: 29px;
}

.book_div input {
    margin-top: 35px;
    font-size: 16px;
    margin-left: 50px;

}

.timeline_date{

    font-size: 18px;
    padding: 5px;
}


.select_date {
    width: 40%;
    padding: 5px;
}

.select_time input {
    width: 20%;
    padding: 5px;
}

.purpose {
    padding: 5px;
    width: 80%;
}

.submit {

    width: min-content;
    padding: 8px 35px;
    background-color: black;
    color: white;
    border: 0px;
    margin-left: auto;
    border-radius: 5px;
}

.submit:hover {
    background-color: rgb(66, 66, 66);
}


.date_section {

    width: 80%;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px 0px;

}

.date_section input {

    font-size: 14px;

}

.time_stamp_area {

    width: 20%;
    height: 100%;
    background-color: rgb(225, 225, 225);
}

.marking_area {

    border: 1px solid rgb(215, 215, 215);
    width: 80%;
    height: 100%;

}


.timeline_div {

    display: flex;
    flex-direction: row;
    background-color: rgb(241, 241, 241);
   
    width: 45vw;
 
}

.time_stamp_area ul {
    list-style: none;
    display: flex;
    flex-direction: column;
    align-items: center;

}

.time_stamp_area ul li {
    margin-bottom: 80px;
    font-size: 17px;
    color: rgb(76, 76, 76);
    font-weight: 600;
    height: 20px;
  
}



.marking_area{

    position: relative;
  

}

.marking_area div{
    width: 100%;
    position: absolute;
   
  
    background-color: rgb(245, 148, 148);
}

</style>