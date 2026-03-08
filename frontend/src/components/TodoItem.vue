<template>
  <li>
    <input
      type="checkbox"
      :checked="todo.done"
      @change="$emit('toggle', todo.id)"
    />

    <span :class="{ done: todo.done }">
      {{ todo.text }}
    </span>

    <button @click="$emit('remove', todo.id)">✕</button>
  </li>
</template>

<script setup>
defineProps({
  todo: Object,
});
</script>

<style scoped>
li {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 8px 0;
}

.done {
  text-decoration: line-through;
  color: #999;
}

button {
  margin-left: auto;
}
</style>
