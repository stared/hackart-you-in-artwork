<template>
    <div class="mdl-cell mdl-cell--4-col">
        <div id="work" class="demo-card-image mdl-card mdl-shadow--2dp"
             v-bind:style="{background: 'url(images/' + workOfArt.fname + ') center / cover'}">
            <div class="mdl-card__title mdl-card--expand"></div>
            <div class="mdl-card__actions">
                <span class="demo-card-image__filename">{{workOfArt.title}}</span>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'work',
        props: ['workOfArt']
    }
</script>

<style scoped>
    .demo-card-image.mdl-card {
        width: 300px;
        height: 300px;
    }

    .demo-card-image > .mdl-card__actions {
        height: 52px;
        padding: 16px;
        background: rgba(0, 0, 0, 0.2);
        text-align: left;
    }

    .demo-card-image__filename {
        color: #fff;
        font-size: 14px;
        font-weight: bold;
    }
</style>