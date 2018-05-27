<template>
    <div class="mdl-cell mdl-cell--4-col">
        <div id="work" class="demo-card-image mdl-card mdl-shadow--2dp"
             v-bind:style="{background: background}">
            <div class="mdl-card__title mdl-card--expand"></div>
            <div class="mdl-card__actions">
                <div style="width: 80%">
                    <span class="demo-card-image__filename">{{title}}</span>
                </div>
                <button class="mdl-button mdl-js-button mdl-button--fab mdl-button--mini-fab mdl-button--colored add-button"
                        v-on:click="markSeen" v-if="!seen"
                >
                    <i class="material-icons">done</i>
                </button>
                <i class="material-icons seen-icon" v-if="seen">done</i>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'work',
        props: ['workOfArt'],
        data: function () {
            return {
                seen: false,
                background: 'url(cropped/' + this.workOfArt.element + ') center / cover'
            };
        },
        methods: {
            markSeen: function () {
                this.seen = true;
                this.$emit('work-seen', this.workOfArt);
                if (this.seen) {
                    this.background = 'url(images/' + this.workOfArt.workOfArt.fname + ') center / cover';
                } else {
                    this.background = 'url(cropped/' + this.workOfArt.element + ') center / cover';
                }
            }
        },
        computed: {
            title: function () {
                if (this.seen) {
                    return this.workOfArt.workOfArt.title;
                } else {
                    return "Znajdź!";
                }
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
        right: 12px;
        cursor: pointer;
        transition: transform .3s;
    }

    .add-button:hover {
        transform: scale(1.5);
    }

    .seen-icon {
        color: #fff;
        position: absolute;
        bottom: 18px;
        right: 18px;
    }
</style>