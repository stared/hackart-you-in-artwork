<template>
    <div id="ArtsList" class="mdl-grid">
        <WorkOfArt
                v-for="w in worksOfArt"
                v-bind:key="w.element"
                v-bind:workOfArt="w"
                v-on:work-seen="onWorkSeen($event)"
        ></WorkOfArt>
    </div>
</template>

<script>
    import WorkOfArt from './WorkOfArt.vue'
    import { EventBus } from '../main.js';

    export default {
        name: "ArtsList",
        props: ['worksOfArt'],
        data() {
            return {
                seenWorks: []
            }
        },
        components: {
            WorkOfArt
        },
        methods: {
            onWorkSeen: function (work) {
                if (this.seenWorks.indexOf(work.fname) === -1) {
                    this.seenWorks.push(work.fname);
                }
                if (this.seenWorks.length === this.worksOfArt.length) {
                    EventBus.$emit('saw-all');
                }
            }
        }
    }
</script>

<style scoped>
</style>