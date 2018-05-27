<template>
    <li id="topic" v-on:click="$emit('topic-selected', topic)" class="mdl-list__item">
        <button class="mdl-button mdl-js-button
                       mdl-button--raised
                       mdl-js-ripple-effect
                       mdl-button--accent">
            <i class="material-icons mdl-list__item-icon">star</i>{{topic.title}}
        </button>
    </li>
</template>

<script>
    export default {
        name: "topic",
        props: ['topic', 'active']
    }
</script>

<style scoped>
    .mdl-button:hover {
        background-color: #b77d89
    }
</style>