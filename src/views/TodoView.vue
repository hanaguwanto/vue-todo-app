<template>
  <div>
    <form @submit.prevent="addTodo">
      <input v-model="newTodo" placeholder="Add new todo" />
      <button>Add</button>
    </form>

  <div class="filters">
    <button @click="filter = 'all'" :class="{ active: filter === 'all' }">
      All
    </button>
    <button @click="filter = 'active'" :class="{ active: filter === 'active' }">
      Active
    </button>
    <button @click="filter = 'completed'" :class="{ active: filter === 'completed' }">
      Completed
    </button>
  </div>


    <ul>
      <TodoItem
        v-for="todo in filteredTodos"
        :key="todo.id"
        :todo="todo"
        @toggle="toggleTodo"
        @remove="removeTodo"
      />
    </ul>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import TodoItem from "../components/TodoItem.vue";

const newTodo = ref("");
const todos = ref([]);
const filter = ref("all");
const filteredTodos = computed(() => {
  if (filter.value === "active") {
    return todos.value.filter(t => !t.done);
  }
  if (filter.value === "completed") {
    return todos.value.filter(t => t.done);
  }
  return todos.value;
});

function addTodo() {
  if (!newTodo.value.trim()) return;

  todos.value.push({
    id: Date.now(),
    text: newTodo.value,
    done: false,
  });

  newTodo.value = "";
}

function toggleTodo(id) {
  const todo = todos.value.find(t => t.id === id);
  if (todo) todo.done = !todo.done;
}

function removeTodo(id) {
  todos.value = todos.value.filter(t => t.id !== id);
}


</script>

<style scoped>
form {
  display: flex;
  gap: 8px;
}

input {
  flex: 1;
  padding: 8px;
}
</style>
