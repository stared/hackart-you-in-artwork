<template>
    <!--<li id="topic" v-on:click="$emit('topic-selected', topic)" class="mdl-list__item">-->
        <!--<span class="mdl-list__item-primary-content">-->
            <!--<i class="material-icons mdl-list__item-icon">star</i>{{topic.title}}-->
        <!--</span>-->
    <!--</li>-->
    <li id="topic" v-on:click="$emit('topic-selected', topic)" class="mdl-list__item">
        <span class="mdl-list__item-primary-content" data-badge="1">
            <i class="material-icons mdl-list__item-icon">star</i>{{topic.title}}
        </span>
    </li>
</template>

<script>
    export default {
        name: "topic",
        props: ['topic']
    }
</script>

<style scoped>

</style>