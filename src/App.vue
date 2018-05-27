<template>
    <div id="app" class="content-grid mdl-grid">
        <TopicsList :topics="topicsList"/>
        <div class="mdl-tabs mdl-js-tabs mdl-js-ripple-effect">
            <div class="mdl-tabs__tab-bar">
                <a href="#starks-panel" class="mdl-tabs__tab is-active">Lista</a>
                <a href="#lannisters-panel" class="mdl-tabs__tab">Mapa</a>
            </div>

            <div class="mdl-tabs__panel is-active" id="starks-panel">
                <ArtsList :worksOfArt="filteredWorksOfArt"/>
            </div>
            <div class="mdl-tabs__panel" id="lannisters-panel">
                <ul>
                    <li>Tywin</li>
                    <li>Cersei</li>
                    <li>Jamie</li>
                    <li>Tyrion</li>
                </ul>
            </div>
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
            });
            EventBus.$on('saw-all', () => {
                alert('Zgłoś się do kasy po coś słodkiego');
            });
        },
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
</style>
