<!-- BookTile.vue -->

<template>
    <div :style="{ backgroundColor: randomColor, color: textColor }" class="book-tile">
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
            randomColor: this.getRandomColor(),
            textColor: this.calculateTextColor(this.getRandomColor()),
        };
    },
    methods: {
        getRandomColor() {
            const random = () => Math.floor(Math.random() * 256);
            const mix: any = { red: 0, green: 0, blue: 255 };

            let red = random();
            let green = random();
            let blue = random();

            const rgbrand = Math.max(0, Math.min(0, 1));

            if (mix) {
                red = red + mix.red * (1 - rgbrand);
                green = green + mix.green * (1 - rgbrand);
                blue = blue + mix.blue * (1 - rgbrand);
            }

            return `rgb(${red}, ${green}, ${blue})`;
        },
        calculateTextColor(color: string) {
            const rgb: any = color.match(/\d+/g);
            const brightness = (parseInt(rgb[0]) * 299 + parseInt(rgb[1]) * 587 + parseInt(rgb[2]) * 114) / 1000;
            return brightness >= 128 ? 'black' : 'white';
        },
    },
    watch: {
        randomColor(newColor: string) {
            this.textColor = this.calculateTextColor(newColor);
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
