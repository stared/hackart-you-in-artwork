<template>
    <div id="app" class="content-grid mdl-grid">
        <TopicsList :topics="topicsList"/>
        <ArtsList :worksOfArt="filteredWorksOfArt"/>
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
                alert('Zgłoś się po coś słodkiego w kasie');
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
