<template>
    <div>
        <h1>Book List</h1>
        <div v-for="book in books" :key="book.Titel" class="book-box">
            <div class="title">{{ book.Titel }}</div>
            <div class="author">{{ book.Autor }}</div>
            <div class="year">{{ book.Veröffentlichungsjahr }}</div>
            <div class="genre">{{ book.Genre }}</div>
        </div>
    </div>
</template>

<script lang="ts">
import axios from 'axios';

type Book = {
    Titel: string,
    Autor: string,
    Veröffentlichungsjahr: number,
    Genre: string
};

export default {
    data() {
        return {
            books: Array<Book>(),
        };
    },
    async created() {
        const response = await axios.get('http://localhost:8000/books')
        console.log(response.data);
        this.books = response.data;
    },
};
</script>
