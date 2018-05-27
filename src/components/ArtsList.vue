<template>
    <div id="ArtsList" class="mdl-grid">
        <WorkOfArt
                v-for="w in worksOfArt"
                v-bind:key="w.fname"
                v-bind:workOfArt="w"
        ></WorkOfArt>
    </div>
    <!--<ul id="ArtsList">-->
        <!--<WorkOfArt-->
                <!--v-for="w in worksOfArt"-->
                <!--v-bind:key="w.fname"-->
                <!--v-bind:workOfArt="w"-->
        <!--&gt;</WorkOfArt>-->
    <!--</ul>-->
</template>

<script>
    import WorkOfArt from './WorkOfArt.vue'

    export default {
        name: "ArtsList",
        props: ['worksOfArt'],
        components: {
            WorkOfArt
        }
    }
</script>

<style scoped>
</style>