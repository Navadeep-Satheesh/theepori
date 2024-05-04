<template>
    <div class="all_rooms">


        <div class="rooms_list">

            <div class="single_room" v-for="room in rooms" :key="room[0]">

                <h3>{{ room[1] }}</h3>

            </div>

        </div>


    </div>
</template>


<script>

export default {
    name: "AllRooms",
    data: () => {
        return {

            rooms: [

                [1, "CETAA HALL", ""],
                [2, "Sargam Stage", ""],
                [3, "Gazebo", ""],
                [4, "Dwani Stage", ""],
                [5, "CGPU Hall", ""],
                [6, "DJ Hall", ""],
                [7, "Archi Corner", ""],
                [8, "CS Seminar Hall", ""],
            ]
        }
        }

}

</script>

<style>
.all_rooms {
    background-color: rgb(255, 255, 255);
    height: 100vh;
    width: 100vw;
}

.rooms_list {

    display: grid;
    width: 100%;
    height: 100%;
    padding-top: 150px;
    /*background-color: red;*/
    grid-template-columns: repeat(auto-fit, minmax(300px, 320px));
    align-items: center;
    justify-content: center;
}

.single_room {
    border: 1px solid rgb(209, 209, 209);
    box-shadow: rgba(50, 50, 93, 0.25) 0px 6px 12px -2px, rgba(0, 0, 0, 0.3) 0px 3px 7px -3px;
    width: 300px;
    height: 300px;
    padding: 10px;
}

.single_room h3{
    
}

</style>