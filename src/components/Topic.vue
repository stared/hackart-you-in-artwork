<template>
    <li id="topic" v-on:click="$emit('topic-selected', topic)" class="mdl-list__item">
        <div>
            <div>
                <img class="category-button" :src="iconPath"/><br/>
                <span>{{topic.title}}</span>
            </div>
        </div>

    </li>
</template>

<script>
    export default {
        name: "topic",
        props: ['topic', 'active'],
        computed: {
            iconPath: function () {
                return "cropped/" + this.topic.icon;
            }
        }
    }
</script>

<style scoped>
    .category-button {
        clip-path: circle(120px at center);
        display: block;
        width: 240px;
        height: 240px;
    }
</style>