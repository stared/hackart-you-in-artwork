<template>
    <div id="app" class="content-grid mdl-grid">
        <TopicsList v-if="topicSelection" :topics="topicsList"/>
        <div v-if="!topicSelection" class="mdl-tabs mdl-js-tabs mdl-js-ripple-effect">
            <button class="mdl-button mdl-js-button" v-on:click="topicSelection=true">
                <i class="material-icons back-button">arrow_back</i>
            </button>
            <ArtsList :worksOfArt="filteredWorksOfArt"/>
        </div>
    </div>
</template>

<script>
    import TopicsList from './components/TopicsList.vue'
    import ArtsList from './components/ArtsList.vue'
    import worksOfArt from './assets/data.json'
    import topicsList from './assets/topics.json'
    import {EventBus} from './main.js';

    export default {
        name: 'app',
        created: function () {
            EventBus.$on('topic-selected', (topic) => {
                this.selectedTopic = topic
                this.topicSelection = false;
            });
            EventBus.$on('saw-all', () => {
                alert('Zgłoś się do kasy po coś słodkiego');
            });
        },
        components: {
            TopicsList, ArtsList
        },
        data: function () {
            return {
                worksOfArt,
                topicsList,
                selectedTopic: null,
                topicSelection: true
            };
        },
        computed: {
            filteredWorksOfArt: function () {
                if (this.selectedTopic != null) {
                    const list1 = topicsList[this.selectedTopic.id];
                    console.log('for', this.selectedTopic.title,  'shall show', list1.images);
                    const list2  = worksOfArt.filter(function (img) {
                        return list1.images.indexOf(img.fname) !== -1
                    });
                    return list2;
                } else {
                    return worksOfArt;
                }
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

    .back-button {

    }
</style>
