<template>
    <!--<li id="work">{{workOfArt.title}}</li>-->
    <img v-bind:src="workOfArt.img" width="160"/>
</template>

<script>
    export default {
        name: 'work',
        props: ['workOfArt']
    }
</script>

<style scoped>

</style>