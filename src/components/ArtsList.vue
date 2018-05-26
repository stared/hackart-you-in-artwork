<template>
    <ul id="ArtsList">
        <WorkOfArt
                v-for="w in worksOfArt"
                v-bind:key="w.id"
                v-bind:workOfArt="w"
        ></WorkOfArt>
    </ul>
</template>

<script>
    import WorkOfArt from './WorkOfArt.vue'

    export default {
        name: "ArtsList",
        props: ['worksOfArt'],
        // data: function () {
        //     return {
        //         workOfArt: [
        //             {id: 0, title: 'Joanna'},
        //             {id: 1, title: 'Natalia'},
        //             {id: 2, title: 'Anna'}
        //         ]
        //     };
        // },
        components: {
            WorkOfArt
        }
    }
</script>

<style scoped>

</style>