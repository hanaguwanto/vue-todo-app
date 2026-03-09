<script setup>
import { ref, watch } from "vue"

const props = defineProps({
  todo: Object
})

const emit = defineEmits(["toggle", "remove", "edit"])

const editing = ref(false)
const newText = ref(props.todo.text)

watch(() => props.todo.text, v => newText.value = v)

function startEdit() {
  editing.value = true
}

function saveEdit() {
  emit("edit", props.todo.id, newText.value)
  editing.value = false
}
</script>

<template>
  <li>
    <input
      type="checkbox"
      :checked="todo.done"
      @change="$emit('toggle', todo.id)"
    />

    <span v-if="!editing">{{ todo.text }}</span>

    <input
      v-else
      v-model="newText"
    />

    <button v-if="!editing" @click="startEdit">Edit</button>
    <button v-else @click="saveEdit">Save</button>

    <button @click="$emit('remove', todo.id)">Delete</button>
  </li>
</template>

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
