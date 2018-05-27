<template>
    <li id="topic" v-on:click="$emit('topic-selected', topic)" class="mdl-list__item">
        <div>
            <div>
                <img class="category-button" src="images/0001.jpg"/><br/>
                <span>{{topic.title}}</span>
            </div>
        </div>

    </li>
</template>

<script>
    export default {
        name: "topic",
        props: ['topic', 'active']
    }
</script>

<style scoped>
    .category-button {
        clip-path: circle(120px at center);
        display: block;
        max-width: 300px;
        max-height: 300px;
        width: auto;
        height: auto;
    }
</style>