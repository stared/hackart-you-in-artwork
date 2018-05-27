<template>
    <div id="app" class="content-grid mdl-grid">
        <TopicsList :topics="topicsList"/>
        <ArtsList v-on:topic-selected="foo123" :worksOfArt="filteredWorksOfArt"/>
    </div>

    <!--<div id="app">-->
    <!--<TopicsList :topics="topicsList"/>-->
    <!--<ArtsList v-on:topic-selected="foo123" :worksOfArt="filteredWorksOfArt"/>-->
    <!--</div>-->
</template>

<script>
    import TopicsList from './components/TopicsList.vue'
    import ArtsList from './components/ArtsList.vue'
    import worksOfArt from './assets/data.json'
    import topicsList from './assets/topics.json'

    export default {
        name: 'app',
        components: {
            TopicsList, ArtsList
        },
        // state: {
        //     selectedTopic: null
        // },
        data: function () {
            return {
                worksOfArt,
                topicsList,
                selectedTopic: null
            };
        },
        watch: {
            selectedTopic: function (val) {
                console.log("foo");
            }
        },
        computed: {
            filteredWorksOfArt: function () {
                if (this.selectedTopic != null) {
                    const list = topicsList[this.selectedTopic];
                    return worksOfArt.filter(w => list.images.indexOf(w.fname) === -1);
                } else {
                    return worksOfArt;
                }
            }
        },
        methods: {
            foo123: function () {
                console.log("123");
            }
        }
    }
</script>

<style>
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-top: 60px;
    }
    .content-grid {
        max-width: 960px;
    }
</style>
