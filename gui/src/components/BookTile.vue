<!-- BookTile.vue -->

<template>
    <div :style="{ backgroundColor: randomColor }" class="book-tile">
        <div class="title-large">{{ book.Titel }}</div>
        <div class="author-small">{{ book.Autor }}</div>
    </div>
</template>

<script lang="ts">
export default {
    props: {
        book: {
            type: Object,
            required: true,
        },
    },
    data() {
        return {
            randomColor: this.getRandomColor(this.stringToSeed(this.book.Titel)),
        };
    },
    methods: {
        stringToSeed(title: string) {
            let seed = 0;
            for (let i = 0; i < title.length; i++) {
                seed = (seed * 31 + title.charCodeAt(i)) & 0xffffffff;
            }
            return seed;
        },
        getRandomColor(seed: number) {
            const random = () => Math.floor(Math.random() * 256);
            const mix: any = { red: 201, green: 191, blue: 165 };

            let red = random();
            let green = random();
            let blue = random();

            const dilution = 12;

            if (mix) {
                red = (red + mix.red) / dilution;
                green = (green + mix.green) / dilution;
                blue = (blue + mix.blue) / dilution;
            }

            return `rgb(${red}, ${green}, ${blue})`;
        },
    },
};
</script>

<style scoped>
.book-tile {
    border: 1px solid #ccc;
    padding: 10px;
    margin: 10px;
    width: 200px;
    height: 200px;
    display: flex;
    flex-direction: column;
}

.title-large {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 5px;
}

.author-small {
    font-size: 14px;
    margin-bottom: 5px;
    align-self: flex-end;
}
</style>
