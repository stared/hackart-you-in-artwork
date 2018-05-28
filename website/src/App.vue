<template>
    <div id="app" class="content-grid mdl-grid">
        <header class="mdl-layout__header my-header">
            <div class="mdl-layout__header-row header-row">
                <span class="mdl-layout-title">Skarby muzeum - <small>znajdź ukryte szczegóły na obrazach!</small></span>
            </div>
        </header>
        <TopicsList v-if="topicSelection" :topics="topicsList"/>
        <div v-if="!topicSelection" class="mdl-tabs mdl-js-tabs mdl-js-ripple-effect">
            <button class="mdl-button mdl-js-button" v-on:click="topicSelection=true">
                <i class="material-icons back-button">arrow_back</i>
            </button>
            <ArtsList :worksOfArt="filteredWorksOfArt"/>
            <LevelMap :rooms="rooms" width="800" height="400"/>
        </div>
    </div>
</template>

<script>
    import TopicsList from './components/TopicsList.vue'
    import ArtsList from './components/ArtsList.vue'
    import LevelMap from './components/LevelMap.vue'
    import worksOfArt from './assets/data.json'
    import topicsList from './assets/topics.json'
    import rooms from './assets/rooms.json'
    import {EventBus} from './main.js';

    export default {
        name: 'app',
        created: function () {
            EventBus.$on('topic-selected', (topic) => {
                this.selectedTopic = topic;
                this.topicSelection = false;
            });
            EventBus.$on('saw-all', () => {
                alert('Zgłoś się do kasy po coś słodkiego');
            });
        },
        components: {
            TopicsList,
            ArtsList,
            LevelMap
        },
        data: function () {
            return {
                worksOfArt,
                topicsList,
                rooms,
                selectedTopic: null,
                topicSelection: true
            };
        },
        computed: {
            filteredWorksOfArt: function () {
                let result = [];
                if (this.selectedTopic != null) {
                    let items = topicsList[this.selectedTopic.id]['items'].slice();
                    for (let i = 0; i < items.length; i++) {
                        let item = items[i];
                        for (let j = 0; j < worksOfArt.length; j++) {
                            if (worksOfArt[j].fname === item.original) {
                                item.workOfArt = worksOfArt[j];
                                result.push(item);
                                break;
                            }
                        }
                    }
                }
                return result;
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
        float: left;
    }

    .my-header {
        background: #990066ff;
    }
    .header-row {
        padding: 16px;
    }
</style>
