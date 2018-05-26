<template>
    <ul id="topics-list">
        <topic
                v-for="topic in topics"
                v-bind:key="topic.id"
                v-bind:topic="topic"
        ></topic>
    </ul>
</template>

<script>
    import Topic from './Topic.vue'

    export default {
        name: "topics-list",
        data: function () {
            return {
                topics: [
                    {id: 0, title: 'Przyroda'},
                    {id: 1, title: 'Nauka'},
                    {id: 2, title: 'Wojna'}
                ]
            };
        },
        components: {
            Topic
        }
    }
</script>

<style scoped>

</style>