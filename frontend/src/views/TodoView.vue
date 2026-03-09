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
        @edit="editTodo"
      />
    </ul>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import TodoItem from "../components/TodoItem.vue";

const newTodo = ref("");
const todos = ref([]);
const filter = ref("all");

async function loadTodos() {
  const res = await fetch("http://127.0.0.1:5000/todos");
  const data = await res.json();

  todos.value = data.map(t => ({
    id: t.id,
    text: t.title,
    done: Boolean(t.completed)
  }));
}

onMounted(loadTodos);

const filteredTodos = computed(() => {
  if (filter.value === "active") {
    return todos.value.filter(t => !t.done);
  }
  if (filter.value === "completed") {
    return todos.value.filter(t => t.done);
  }
  return todos.value;
});

async function addTodo() {
  if (!newTodo.value.trim()) return;

  await fetch("http://127.0.0.1:5000/todos", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title: newTodo.value })
  });

  newTodo.value = "";
  loadTodos();
}

async function toggleTodo(id) {
  const todo = todos.value.find(t => t.id === id);
  if (!todo) return;

  const newState = !todo.done;

  await fetch(`http://127.0.0.1:5000/todos/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      title: todo.text,
      completed: newState
    })
  });

  todo.done = newState;
}

async function removeTodo(id) {
  await fetch(`http://127.0.0.1:5000/todos/${id}`, {
    method: "DELETE"
  });

  todos.value = todos.value.filter(t => t.id !== id);
}

async function editTodo(id, newText) {
  const todo = todos.value.find(t => t.id === id)
  if (!todo) return

  await fetch(`http://127.0.0.1:5000/todos/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      title: newText,
      completed: todo.done
    })
  })

  loadTodos()
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