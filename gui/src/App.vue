<!-- App.vue -->

<template>
  <div id="app">
    <book-tile v-for="book in books" :key="book.id" :book="book" />
  </div>
</template>

<script lang="ts">
import BookTile from './components/BookTile.vue';
import axios from 'axios';

const response = await axios.get('http://localhost:8000/books');
const book_json = response.data;

export default {
  components: {
    BookTile,
  },
  data() {
    return {
      books: book_json,
    };
  },
};
</script>

<style>
#app {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}
</style>
