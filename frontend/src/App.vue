<template>
  <div class="app">
    <h1>Todo App</h1>
    <TodoView />
  </div>
</template>

<script setup>
import TodoView from "./views/TodoView.vue";
</script>

<style>
.app {
  max-width: 600px;
  margin: 60px auto;
  font-family: system-ui, sans-serif;
}
</style>
