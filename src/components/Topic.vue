<template>
    <li id="topic" v-on:click="$emit('topic-selected', topic)">{{topic.title}}</li>
</template>

<script>
    export default {
        name: "topic",
        props: ['topic']
    }
</script>

<style scoped>

</style>