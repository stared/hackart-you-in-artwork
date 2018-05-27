<template>
    <div class="mdl-cell mdl-cell--4-col">
        <div id="work" class="demo-card-image mdl-card mdl-shadow--2dp"
             v-bind:style="{background: 'url(images/' + workOfArt.fname + ') center / cover'}">
            <div class="mdl-card__title mdl-card--expand"></div>
            <div class="mdl-card__actions">
                <div style="width: 80%">
                    <span class="demo-card-image__filename">{{workOfArt.title}}</span>
                </div>
                <button class="mdl-button mdl-js-button mdl-button--fab mdl-button--mini-fab mdl-button--colored add-button"
                        v-on:click="markSeen" v-if="!seen"
                >
                    <i class="material-icons">add</i>
                </button>
                <i class="material-icons seen-icon" v-if="seen">done</i>
            </div>
            <!--<div class="mdl-card__menu">-->
            <!--<label class="mdl-checkbox mdl-js-checkbox mdl-js-ripple-effect" for="checkbox-1">-->
            <!--<input type="checkbox" id="checkbox-1" class="mdl-checkbox__input">-->
            <!--</label>-->
            <!--</div>-->
        </div>
    </div>
</template>

<script>
    export default {
        name: 'work',
        props: ['workOfArt', 'saw'],
        data: function () {
            return {seen: false};
        },
        methods: {
            markSeen: function () {
                this.seen = true;
                this.$emit('work-seen', this.workOfArt);
            }
        }
    }
</script>

<style scoped>
    .demo-card-image.mdl-card {
        width: 300px;
        height: 300px;
    }

    .demo-card-image > .mdl-card__actions {
        height: 64px;
        padding: 16px;
        background: rgba(0, 0, 0, 0.2);
        text-align: left;
    }

    .demo-card-image__filename {
        color: #fff;
        font-size: 14px;
        font-weight: bold;
    }

    .add-button {
        position: absolute;
        bottom: 12px;
        right: 12px;;
    }
    .seen-icon {
        color: #fff;
        position: absolute;
        bottom: 18px;
        right: 18px;;
    }
</style>