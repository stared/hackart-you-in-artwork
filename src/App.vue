<template>
    <div id="app">
        <TopicsList/>
        <ArtsList :worksOfArt="worksOfArt"/>
    </div>
</template>

<script>
    import HelloWorld from './components/HelloWorld.vue'
    import TopicsList from './components/TopicsList.vue'
    import ArtsList from './components/ArtsList.vue'
    import worksOfArt from './assets/data.json'

    export default {
        name: 'app',
        components: {
            HelloWorld, TopicsList, ArtsList
        },
        data: function () {
            return {
                worksOfArt
            };
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
</style>
