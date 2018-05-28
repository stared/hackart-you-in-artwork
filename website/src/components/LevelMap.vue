<template>
    <svg xmlns="http://www.w3.org/2000/svg" 
       :width="width+'px'"
       :height="height+'px'">

        <rect v-for="room in rooms" v-bind:key="room.nr"
                :x="5 + 15 * room.x"
                :y="5 + 15 * room.y"
                :width="15 * room.w"
                :height="15 * room.h"
                class="room"/>

    </svg>
</template>

<script>
    export default {
        name: "level-map",
        props: ['rooms', 'width', 'height']
    }
</script>

<style scoped>
    .room {
      fill: steelblue;
      stroke: black;
      stroke-width: 3px;
    }

    .room:hover {
      fill: coral;
    }
</style>