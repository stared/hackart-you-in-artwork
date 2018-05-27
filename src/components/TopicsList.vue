<template>
    <ul id="topics-list" class="mdl-list">
        <topic
                v-for="topic in topics"
                v-bind:key="topic.id"
                v-bind:topic="topic"
                v-on:topic-selected="onTopicSelected"
        ></topic>
    </ul>
</template>

<script>
    import Topic from './Topic.vue'

    export default {
        name: "topics-list",
        props: ['topics'],
        data: function () {
            return {
                selectedTopic: null
            };
        },
        methods: {
            onTopicSelected: function(topic) {
                
            }
        },
        components: {
            Topic
        }
    }
</script>

<style scoped>

</style>